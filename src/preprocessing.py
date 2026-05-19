import pandas as pd

def load_data():
    ratings = pd.read_csv('data/raw/ratings.csv')
    movies = pd.read_csv('data/raw/movies.csv')
    return ratings, movies

def create_user_movie_matrix(ratings):

    matrix = ratings.pivot_table(
        index='userId',
        columns='movieId',
        values='rating'
    )
    
    user_means = matrix.mean(axis=1)
    matrix_centered = matrix.sub(user_means, axis=0)
    
    matrix_centered = matrix_centered.fillna(0)
    
    return matrix_centered, user_means