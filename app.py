from flask import Flask, render_template, request
from src.preprocessing import load_data, create_user_movie_matrix
from src.clustering import apply_kmeans
from src.recommendation import recommend_movies

app = Flask(__name__)

ratings, movies = load_data()
matrix = create_user_movie_matrix(ratings)
matrix, model = apply_kmeans(matrix)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = None
    selected_user = None

    if request.method == "POST":
        selected_user = int(request.form["user_id"])
        recommendations = recommend_movies(selected_user, matrix, movies)
        recommendations = recommendations.to_dict(orient="records")

    users = matrix.index.tolist()

    return render_template(
        "index.html",
        users=users,
        recommendations=recommendations,
        selected_user=selected_user
    )

if __name__ == "__main__":
    app.run(debug=True)