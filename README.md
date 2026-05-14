# 🎬 Sistema de Recomendação de Filmes com IA

Projeto desenvolvido para a disciplina de Inteligência Artificial.

O sistema recomenda filmes com base em:

- Filtragem colaborativa
- Clusterização de usuários com K-Means
- Dataset MovieLens

---

## 📌 Tecnologias utilizadas

- Python 3
- Flask
- Pandas
- NumPy
- Scikit-learn
- HTML
- CSS

---

## 📂 Estrutura do projeto

```text
TrabalhoA3--IA-Aplicada/
│
├── app.py
├── main.py
├── enrich_dataset.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── movies.csv
│   ├── ratings.csv
│   ├── links.csv
│   └── movies_pt.csv
│
├── src/
│   ├── preprocessing.py
│   ├── clustering.py
│   └── recommendation.py
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## 📥 Download do dataset

Baixe o dataset MovieLens:

https://grouplens.org/datasets/movielens/

Baixar:

**ml-latest-small.zip**

Após extrair, mover para a pasta `data/`:

```text
data/
├── movies.csv
├── ratings.csv
├── links.csv
```

---

## 🚀 Como executar o projeto

### 1. Clonar repositório

```bash
git clone [https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git](https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git)
cd TrabalhoA3--IA-Aplicada
```

---

### 2. Criar ambiente virtual

Windows:

```bash
python -m venv venv
.\venv\Scripts\Activate
```

---

### 3. Instalar dependências

```bash
python -m pip install -r requirements.txt
```

---

### 4. Gerar nomes e imagens em português

*É necessário adicionar sua chave da API no arquivo `enrich_dataset.py` antes de rodar.*

```bash
python enrich_dataset.py
```

---

### 5. Rodar aplicação

```bash
python app.py
```

---

### 6. Abrir navegador

Acesse:

```text
[http://127.0.0.1:5000](http://127.0.0.1:5000)
```

---

## 🧠 Como funciona

### 1. Pré-processamento
O sistema carrega:

- avaliações dos usuários
- lista de filmes

e cria uma matriz:

```text
usuário x filme
```

---

### 2. Clusterização
Utiliza K-Means para agrupar usuários com gostos semelhantes.

Exemplo:

- Cluster 1 → ação
- Cluster 2 → romance
- Cluster 3 → comédia

---

### 3. Filtragem colaborativa
Após encontrar usuários similares:

- identifica filmes bem avaliados
- recomenda ao usuário selecionado

---

## 🎯 Funcionalidades

- Seleção de usuário
- Geração de recomendações
- Interface web
- Exibição de filmes e gêneros

---

## 📊 Exemplo de uso

1. Selecionar usuário na interface
2. Clicar em **Gerar Recomendações**
3. Visualizar filmes sugeridos com pôsteres

---

## ⚠️ Possíveis erros

### Erro: módulo não encontrado

Instalar dependências:

```bash
python -m pip install -r requirements.txt
```

---

### Erro: arquivo não encontrado

Verifique se extraiu corretamente ou se rodou o script da API:

```text
data/movies.csv
data/ratings.csv
data/movies_pt.csv
```

---

## 👨‍💻 Autor

Projeto acadêmico desenvolvido para aplicação de técnicas de IA em sistemas de recomendação.

---

## 📚 Dataset

MovieLens Dataset  
https://grouplens.org/datasets/movielens/

## API Tmdb
https://www.themoviedb.org/settings/api
