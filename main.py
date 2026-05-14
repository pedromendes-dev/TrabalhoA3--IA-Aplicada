from src.preprocessing import load_data, create_user_movie_matrix
from src.clustering import apply_kmeans
from src.recommendation import recommend_for_existing_user

def main():
    ratings, movies = load_data()

    matrix, _ = create_user_movie_matrix(ratings)
    matrix, model = apply_kmeans(matrix)

    user_id = 1 
    recommendations = recommend_for_existing_user(user_id, matrix, movies, top_n=5)

    print("\n🎬 Recomendações para o usuário 1:\n")
    print(recommendations[['title', 'genres']])

if __name__ == "__main__":
    main()