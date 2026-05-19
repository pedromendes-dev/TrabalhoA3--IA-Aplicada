# Agrupamento de usuários via KMeans.
# Divide os usuários em clusters de gosto similar para reduzir o espaço de busca
# na etapa de recomendação — em vez de comparar com todos os usuários,
# comparamos apenas com os do mesmo cluster.

from sklearn.cluster import KMeans

def apply_kmeans(matrix, n_clusters=5):
    # n_clusters=5: empiricamente equilibra granularidade e cobertura para este dataset.
    # random_state=42: garante reprodutibilidade dos clusters entre execuções.
    # n_init='auto': usa a melhor inicialização automática (sklearn >= 1.2).
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
    clusters = kmeans.fit_predict(matrix)

    # Adiciona a coluna 'cluster' na própria matriz para lookup direto por userId
    matrix_with_clusters = matrix.copy()
    matrix_with_clusters['cluster'] = clusters

    return matrix_with_clusters, kmeans
