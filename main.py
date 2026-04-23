from src.preprocessing import load_data, create_user_movie_matrix
from src.clustering import apply_kmeans
from src.recommendation import recommend_movies

def main():
    ratings, movies = load_data()

    matrix = create_user_movie_matrix(ratings)
    matrix, model = apply_kmeans(matrix)

    user_id = 1 
    recommendations = recommend_movies(user_id, matrix, movies)

    print("\n🎬 Recomendações:\n")
    print(recommendations[['title', 'genres']])

if __name__ == "__main__":
    main()