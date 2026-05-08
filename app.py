from flask import Flask, render_template, request
from src.preprocessing import load_data, create_user_movie_matrix
from src.clustering import apply_kmeans
import pandas as pd

app = Flask(__name__)

ratings, movies = load_data()
matrix = create_user_movie_matrix(ratings)
matrix, model = apply_kmeans(matrix)


def recommend_from_movies(selected_movies):
    selected_ids = movies[
        movies["title"].isin(selected_movies)
    ]["movieId"].tolist()

    similar_users = ratings[
        ratings["movieId"].isin(selected_ids)
    ]["userId"].unique()

    recommendations = ratings[
        ratings["userId"].isin(similar_users)
    ]

    recommendations = recommendations[
        ~recommendations["movieId"].isin(selected_ids)
    ]

    top_movies = (
        recommendations.groupby("movieId")["rating"]
        .mean()
        .sort_values(ascending=False)
        .head(12)
        .index
    )

    return movies[movies["movieId"].isin(top_movies)]


@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = None

    movie_titles = sorted(movies["title"].tolist())[:300]

    if request.method == "POST":
        selected_movies = request.form.getlist("movies")

        if selected_movies:
            recommendations = recommend_from_movies(selected_movies)
            recommendations = recommendations.to_dict(orient="records")

    return render_template(
        "index.html",
        movie_titles=movie_titles,
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)