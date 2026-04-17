

import os
from dotenv import load_dotenv
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt



# -------------------------
# 1. CARREGAR DADOS
# -------------------------
load_dotenv()

PASTA_BASE = os.path.dirname(__file__)
PASTA_DADOS = os.getenv("DATA_DIR", os.path.join(PASTA_BASE, "data"))
avaliacoes = pd.read_csv(
    os.path.join(PASTA_DADOS, "u.data"),
    sep="\t",
    names=["usuario_id", "filme_id", "nota", "timestamp"]
)
filmes = pd.read_csv(
    os.path.join(PASTA_DADOS, "u.item"),
    sep="|",
    encoding="latin-1",
    usecols=[0, 1],
    names=["filme_id", "titulo"]
)
dados = pd.merge(avaliacoes, filmes, on="filme_id")
print(dados.head())

# -------------------------
# 2. MATRIZ USUÁRIO x FILME
# -------------------------
matriz_usuario_filme = dados.pivot_table(
    index="usuario_id",
    columns="titulo",
    values="nota"
).fillna(0)

# -------------------------
# 3. SIMILARIDADE ENTRE USUÁRIOS
# -------------------------
similaridade = cosine_similarity(matriz_usuario_filme)
df_similaridade = pd.DataFrame(
    similaridade,
    index=matriz_usuario_filme.index,
    columns=matriz_usuario_filme.index
)

# -------------------------
# MÉTODO DO COTOVELO (Escolha ótima de K)
# -------------------------
# Justificativa técnica: Utilizamos o método do cotovelo para determinar o número ideal de clusters no algoritmo K-means, analisando a redução da inércia.
inercias = []
faixa_k = range(1, 15)
for k in faixa_k:
    modelo = KMeans(n_clusters=k, random_state=42)
    modelo.fit(matriz_usuario_filme)
    inercias.append(modelo.inertia_)

plt.plot(faixa_k, inercias)
plt.xlabel("Número de clusters (K)")
plt.ylabel("Inércia")
plt.title("Método do Cotovelo")
plt.show()


# -------------------------
# MÉTRICA DE AVALIAÇÃO
# -------------------------
# Avaliamos o sistema utilizando a média das avaliações reais dos itens recomendados.
def avaliar_recomendacao(usuario_id):
    recomendados = recomendar_filmes(usuario_id, top_n=5)
    avaliacoes_usuario = dados[dados["usuario_id"] == usuario_id]
    notas = []
    for filme in recomendados.index:
        nota = avaliacoes_usuario[avaliacoes_usuario["titulo"] == filme]["nota"]
        if not nota.empty:
            notas.append(nota.values[0])
    if notas:
        return sum(notas) / len(notas)
    else:
        return 0


# -------------------------
# 6. K-MEANS
# -------------------------
kmeans.fit(user_movie_matrix_kmeans)
k = 5  # número de grupos (você pode testar outros)
kmeans = KMeans(n_clusters=k, random_state=42)
matriz_kmeans = matriz_usuario_filme.copy()
kmeans.fit(matriz_kmeans)

# adiciona cluster para cada usuário
usuarios_clusters = pd.DataFrame({
    "usuario_id": matriz_usuario_filme.index,
    "cluster": kmeans.labels_
})




