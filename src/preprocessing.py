# Pré-processamento dos dados do MovieLens.
# Responsável por carregar os CSVs e construir a matriz usuário-filme
# normalizada por média (mean-centering), que é a entrada para o KMeans.

import pandas as pd

def load_data():
    # ratings.csv: userId, movieId, rating, timestamp
    # movies.csv:  movieId, title, genres
    ratings = pd.read_csv('data/raw/ratings.csv')
    movies = pd.read_csv('data/raw/movies.csv')
    return ratings, movies

def create_user_movie_matrix(ratings):
    # Pivota: linhas = usuários, colunas = filmes, valores = notas
    matrix = ratings.pivot_table(
        index='userId',
        columns='movieId',
        values='rating'
    )

    # Mean-centering: subtrai a média de cada usuário linha a linha.
    # Remove o viés de escala (usuários que sempre dão notas altas ou baixas)
    # para que a similaridade de cosseno compare padrões de gosto, não magnitude.
    user_means = matrix.mean(axis=1)
    matrix_centered = matrix.sub(user_means, axis=0)

    # Filmes não avaliados viram 0 após o centering — neutros na distância euclidiana
    matrix_centered = matrix_centered.fillna(0)

    return matrix_centered, user_means
