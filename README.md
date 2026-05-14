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

```bash
TrabalhoA3--IA-Aplicada/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── movies.csv
│   ├── ratings.csv
│
├── src/
│   ├── preprocessing.py
│   ├── clustering.py
│   ├── recommendation.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
```

---

## 📥 Download do dataset

Baixe o dataset MovieLens:

https://grouplens.org/datasets/movielens/

Baixar:

**ml-latest-small.zip**

Após extrair, mover para a pasta `data/`:

```bash
data/
├── movies.csv
├── ratings.csv
```

---

## 🚀 Como executar o projeto

### 1. Clonar repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

Entrar na pasta:

```bash
cd TrabalhoA3--IA-Aplicada
```

---

### 2. Criar ambiente virtual

Windows:

```bash
python -m venv venv
```

Ativar:

```bash
.\venv\Scripts\Activate
```

---

### 3. Instalar dependências

```bash
python -m pip install -r requirements.txt
```

---

### 4. Rodar aplicação

```bash
python app.py
```

---

### 5. Abrir navegador

Acesse:

```bash
http://127.0.0.1:5000
```

---

## 🧠 Como funciona

### 1. Pré-processamento
O sistema carrega:

- avaliações dos usuários
- lista de filmes

e cria uma matriz:

```bash
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

1. Selecionar usuário
2. Clicar em **Gerar Recomendações**
3. Visualizar filmes sugeridos

---

## ⚠️ Possíveis erros

### Erro: módulo não encontrado

Instalar dependências:

```bash
python -m pip install -r requirements.txt
```

---

### Erro: arquivo não encontrado

Verifique:

```bash
data/movies.csv
data/ratings.csv
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
