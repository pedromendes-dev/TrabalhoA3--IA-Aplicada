# Sistema de Recomendação MovieLens

Este projeto implementa um sistema de recomendação de filmes baseado em filtragem colaborativa e clusterização de usuários (K-Means), utilizando o dataset MovieLens.

## Funcionalidades

- Recomendação baseada em similaridade entre usuários
- Recomendação baseada em clusterização (K-Means)
- API REST com FastAPI para integração com frontend ou testes via Swagger

## Estrutura do Projeto

- `main.py`: Carrega os dados, treina os modelos de recomendação e expõe funções para recomendação
- `api.py`: API REST para servir recomendações
- `data/`: Coloque aqui os arquivos do MovieLens (`u.data`, `u.item`, etc)
- `tests/`: Testes automatizados para garantir a correta funcionalidade

## Como rodar o projeto

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```
Ou, se não houver requirements.txt:
```bash
pip install pandas scikit-learn fastapi uvicorn python-dotenv
```

### 2. Execute o script principal (opcional)

```bash
python main.py
```

### 3. Rode a API

```bash
uvicorn api:app --reload
```

Acesse a documentação automática em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Endpoints disponíveis

- `/` — Status da API
- `/recommend/{user_id}` — Recomendação baseada em similaridade
- `/recommend_cluster/{user_id}` — Recomendação baseada em cluster

## Exemplo de uso

```python
import requests
resp = requests.get('http://127.0.0.1:8000/recommend/1')
print(resp.json())
```

## Arquitetura

```
Frontend (React, etc)
   ↓
FastAPI (Python)
   ↓
Módulo IA (Recomendação + K-means)
   ↓
Dataset MovieLens
```

## Abordagens de IA

- **Filtragem colaborativa**: recomenda filmes com base em usuários similares
- **Clusterização (K-means)**: segmenta usuários em grupos de interesse e recomenda com base no grupo

## Testes Automatizados

Os testes foram separados do código principal e ficam em `tests/test_recommender.py`.

Para rodar os testes automatizados e garantir que as funções principais estão funcionando corretamente:

```bash
python -m unittest tests/test_recommender.py
```

- O arquivo `main.py` contém apenas o código de produção.
- Todos os prints e execuções de teste foram removidos de `main.py`.
- Siga essa estrutura para manter o projeto organizado e facilitar a manutenção.

## Diferencial para apresentação

> "Utilizamos duas abordagens: filtragem colaborativa (similaridade) e clusterização com K-means para segmentação de usuários."

---

Qualquer dúvida ou sugestão, abra uma issue ou entre em contato!
