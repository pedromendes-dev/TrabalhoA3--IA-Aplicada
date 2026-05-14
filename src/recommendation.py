from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def get_similar_users(target_ratings, cluster_users, top_n=5):
    """Calcula similaridade de cosseno e retorna os top usuários similares."""
    similarity = cosine_similarity([target_ratings], cluster_users)[0]
    similarity_series = pd.Series(similarity, index=cluster_users.index)

    if target_ratings.name in similarity_series.index:
        similarity_series = similarity_series.drop(target_ratings.name)
        
    return similarity_series.sort_values(ascending=False).head(top_n)

def get_movies_from_similar_users(similar_users, cluster_users, viewed_movies, top_n=5):
    """Extrai os filmes com avaliações acima da média dos usuários similares."""
    recommended_movies = []
    
    for user_id in similar_users.index:
        user_ratings = cluster_users.loc[user_id]
        top_movies = user_ratings[user_ratings > 0].index.tolist()
        
        top_movies = [m for m in top_movies if m not in viewed_movies]
        recommended_movies.extend(top_movies)
        
    movie_counts = pd.Series(recommended_movies).value_counts()
    return movie_counts.head(top_n).index.tolist()

def recommend_for_existing_user(user_id, matrix, movies, top_n=5):
    """Recomenda filmes para um usuário que já existe na base."""
    cluster = matrix.loc[user_id, 'cluster']
    users_same_cluster = matrix[matrix['cluster'] == cluster].drop('cluster', axis=1)
    
    target_ratings = users_same_cluster.loc[user_id]
    viewed_movies = target_ratings[target_ratings != 0].index.tolist()
    
    similar_users = get_similar_users(target_ratings, users_same_cluster)
    recommended_ids = get_movies_from_similar_users(similar_users, users_same_cluster, viewed_movies, top_n)
    
    return movies[movies['movieId'].isin(recommended_ids)]

def recommend_for_new_user(selected_movie_ids, matrix, kmeans_model, movies, top_n=5):
    """Recomenda filmes para um usuário novo (Cold Start) baseado em uma lista de filmes."""
    movie_columns = matrix.drop('cluster', axis=1).columns
    
    new_user_ratings = pd.Series(0, index=movie_columns, name='new_user')
    
    valid_movies = [m for m in selected_movie_ids if m in new_user_ratings.index]
    new_user_ratings[valid_movies] = 1.0 
    
    cluster = kmeans_model.predict([new_user_ratings])[0]
    
    users_same_cluster = matrix[matrix['cluster'] == cluster].drop('cluster', axis=1)
    similar_users = get_similar_users(new_user_ratings, users_same_cluster)
    recommended_ids = get_movies_from_similar_users(similar_users, users_same_cluster, valid_movies, top_n)
    
    return movies[movies['movieId'].isin(recommended_ids)]