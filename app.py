# Ponto de entrada da aplicação web Flask.
# Carrega e processa os dados uma única vez na inicialização do módulo —
# em produção (Vercel serverless) isso acontece a cada cold start,
# mas é reutilizado em warm requests dentro da mesma instância.

from flask import Flask, render_template, request
import pandas as pd
from src.preprocessing import load_data, create_user_movie_matrix
from src.clustering import apply_kmeans
from src.recommendation import recommend_for_new_user

app = Flask(__name__, template_folder='views')

# ── Inicialização do modelo ──────────────────────────────────────────────────
# Carrega os dados brutos de avaliações e monta a matriz usuário-filme
ratings, _ = load_data()

# movies_pt.csv é a versão enriquecida com títulos traduzidos e URLs de poster
movies = pd.read_csv('data/processed/movies_pt.csv')

# Aplica mean-centering e treina o KMeans — ambos ficam em memória durante a sessão
matrix, _ = create_user_movie_matrix(ratings)
matrix, kmeans_model = apply_kmeans(matrix)
# ────────────────────────────────────────────────────────────────────────────

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = None

    # Serializa apenas as colunas necessárias para o frontend (evita expor dados desnecessários)
    movies_list = movies[["movieId", "title", "title_pt", "poster_url", "genres"]].fillna("").to_dict(orient="records")

    if request.method == "POST":
        selected_titles = request.form.getlist("movies")

        if selected_titles:
            # Converte títulos em português para IDs numéricos do MovieLens
            selected_ids = movies[movies["title_pt"].isin(selected_titles)]["movieId"].tolist()
            recs_df = recommend_for_new_user(selected_ids, matrix, kmeans_model, movies, top_n=12)
            recommendations = recs_df.fillna("").to_dict(orient="records")

    return render_template(
        "index.html",
        movies_list=movies_list,
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)
