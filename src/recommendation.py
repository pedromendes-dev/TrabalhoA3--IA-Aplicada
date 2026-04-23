from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def recommend_movies(user_id, matrix, movies, top_n=5):
    cluster = matrix.loc[user_id, 'cluster']

    users_same_cluster = matrix[matrix['cluster'] == cluster]
    users_same_cluster = users_same_cluster.drop('cluster', axis=1)

    similarity = cosine_similarity(users_same_cluster)

    similarity_df = pd.DataFrame(
        similarity,
        index=users_same_cluster.index,
        columns=users_same_cluster.index
    )

    similar_users = similarity_df[user_id].sort_values(ascending=False)

    similar_users = similar_users.drop(user_id)
    top_users = similar_users.head(5).index

    recommended_movies = []

    for user in top_users:
        user_ratings = users_same_cluster.loc[user]
        top_movies = user_ratings[user_ratings > 4].index.tolist()
        recommended_movies.extend(top_movies)

    recommended_movies = list(set(recommended_movies))[:top_n]

    return movies[movies['movieId'].isin(recommended_movies)]