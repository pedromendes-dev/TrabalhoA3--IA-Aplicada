from fastapi import FastAPI
from main import recommend_movies, recommend_by_cluster

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API de recomendação rodando"}

@app.get("/recommend/{user_id}")
def recommend(user_id: int):
    recs = recommend_movies(user_id).to_dict()
    return recs

@app.get("/recommend_cluster/{user_id}")
def recommend_cluster(user_id: int):
    recs = recommend_by_cluster(user_id).to_dict()
    return recs
