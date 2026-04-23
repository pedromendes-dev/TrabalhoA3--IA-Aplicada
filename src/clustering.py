from sklearn.cluster import KMeans

def apply_kmeans(matrix, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(matrix)

    matrix['cluster'] = clusters
    return matrix, kmeans