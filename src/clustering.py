from sklearn.cluster import KMeans

def apply_kmeans(matrix, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
    clusters = kmeans.fit_predict(matrix)

    matrix_with_clusters = matrix.copy()
    matrix_with_clusters['cluster'] = clusters
    
    return matrix_with_clusters, kmeans