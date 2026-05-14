import pandas as pd
import requests
import time

TMDB_API_KEY = "0bed6ec80977a0ea14455719db0b2b86"

movies = pd.read_csv("data/movies.csv")
links = pd.read_csv("data/links.csv")

df_full = pd.merge(movies, links, on="movieId")

df = df_full.copy()

poster_urls = []
titles_pt = []

for index, row in df.iterrows():
    tmdb_id = row["tmdbId"]
    
    if pd.isna(tmdb_id):
        poster_urls.append("")
        titles_pt.append(row["title"])
        continue
        
    url = f"https://api.themoviedb.org/3/movie/{int(tmdb_id)}?api_key={TMDB_API_KEY}&language=pt-BR"
    
    try:
        response = requests.get(url).json()
        
        if "poster_path" in response and response.get("poster_path"):
            poster_urls.append(f"https://image.tmdb.org/t/p/w500{response['poster_path']}")
        else:
            poster_urls.append("")
            
        if "title" in response and response.get("title"):
            titles_pt.append(response["title"])
        else:
            titles_pt.append(row["title"])
            
    except Exception:
        poster_urls.append("")
        titles_pt.append(row["title"])
        
    time.sleep(0.2)

df["poster_url"] = poster_urls
df["title_pt"] = titles_pt

df.to_csv("data/movies_pt.csv", index=False)