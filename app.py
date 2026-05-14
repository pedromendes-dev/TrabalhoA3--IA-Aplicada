from flask import Flask, render_template, request
import pandas as pd
from src.preprocessing import load_data, create_user_movie_matrix
from src.clustering import apply_kmeans
from src.recommendation import recommend_for_new_user

app = Flask(__name__)

ratings, _ = load_data()
movies = pd.read_csv('data/movies_pt.csv')

matrix, _ = create_user_movie_matrix(ratings)
matrix, kmeans_model = apply_kmeans(matrix)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = None
    
    movies_list = movies[["movieId", "title_pt", "poster_url"]].head(300).fillna("").to_dict(orient="records")

    if request.method == "POST":
        selected_titles = request.form.getlist("movies")

        if selected_titles:
            selected_ids = movies[movies["title_pt"].isin(selected_titles)]["movieId"].tolist()
            recs_df = recommend_for_new_user(selected_ids, matrix, kmeans_model, movies, top_n=12)
            recommendations = recs_df.to_dict(orient="records")

    return render_template(
        "index.html",
        movies_list=movies_list,
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)