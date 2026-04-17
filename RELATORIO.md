# Relatório do Projeto — Sistema de Recomendação Inteligente (MovieLens)

# 1. INTRODUÇÃO

Com o crescimento exponencial da quantidade de conteúdos digitais disponíveis, os usuários enfrentam dificuldades em selecionar itens que sejam relevantes aos seus interesses. Nesse contexto, sistemas de recomendação têm se tornado fundamentais, sendo amplamente utilizados por plataformas como streaming e e-commerce.

Este projeto tem como objetivo desenvolver um sistema inteligente de recomendação de filmes, capaz de sugerir conteúdos personalizados com base no comportamento de usuários. Para isso, foram aplicadas técnicas de Inteligência Artificial voltadas à análise de padrões em dados de avaliação.

A solução proposta utiliza o dataset MovieLens 100K, amplamente utilizado em pesquisas acadêmicas, contendo informações de usuários, filmes e avaliações.

A abordagem adotada neste trabalho é do tipo conexionista, utilizando algoritmos de aprendizado de máquina para identificar padrões e relações entre usuários e itens, sem a necessidade de regras explícitas definidas manualmente.

# 2. APLICANDO IA (PROBLEMÁTICA + MODELO)

O problema abordado consiste em prever quais filmes um usuário pode gostar, com base em dados históricos de avaliações. Trata-se de um problema clássico de recomendação, que pode ser resolvido por diferentes abordagens de Inteligência Artificial.

Neste projeto, foram utilizadas duas técnicas principais:

- Filtragem colaborativa baseada em similaridade: identifica usuários com gostos semelhantes e recomenda itens com base nas preferências desses usuários.
- Clusterização com K-means: agrupa usuários em clusters com características semelhantes, permitindo recomendações baseadas no comportamento coletivo de cada grupo.

A escolha dessas técnicas se justifica pela sua eficiência em identificar padrões em grandes volumes de dados, além de serem amplamente utilizadas em sistemas reais de recomendação.

Diferentemente de abordagens simbólicas, que dependem de regras explícitas, os métodos conexionistas utilizados aprendem automaticamente a partir dos dados, tornando o sistema mais adaptável e escalável.

# 3. DESENVOLVIMENTO

## 3.1 Modelagem da solução

A solução foi desenvolvida utilizando a linguagem Python, com apoio de bibliotecas como Pandas e Scikit-learn. Inicialmente, os dados foram carregados e organizados em uma matriz de usuário versus filme, onde cada célula representa a avaliação atribuída por um usuário a um determinado filme.

Essa matriz foi utilizada como base para o cálculo de similaridade entre usuários, bem como para a aplicação do algoritmo de clusterização.

## 3.2 Filtragem colaborativa

A filtragem colaborativa foi implementada utilizando a similaridade do cosseno, que mede o grau de semelhança entre dois usuários com base em seus padrões de avaliação.

A partir disso, o sistema identifica usuários semelhantes e recomenda filmes bem avaliados por esses usuários, mas ainda não assistidos pelo usuário alvo.

## 3.3 Clusterização com K-means

Para complementar o sistema, foi aplicado o algoritmo K-means, que agrupa usuários em clusters com características semelhantes.

A definição do número ideal de clusters foi realizada por meio do método do cotovelo, que analisa a variação da inércia conforme o número de clusters aumenta. Com base nessa análise, foi escolhido o valor de K = 5, por apresentar um bom equilíbrio entre qualidade e complexidade.

Após a definição dos clusters, as recomendações passaram a considerar os usuários pertencentes ao mesmo grupo, aumentando a relevância das sugestões.

## 3.4 Avaliação do modelo

A avaliação do sistema foi realizada com base na média das avaliações reais dos itens recomendados aos usuários. Esse método permite verificar se os filmes sugeridos são, de fato, bem avaliados pelo próprio usuário.

Os resultados indicaram que o modelo consegue gerar recomendações coerentes, demonstrando a eficácia das técnicas aplicadas.

## 3.5 Explicação do K-means

O algoritmo K-means é uma técnica de aprendizado não supervisionado que tem como objetivo agrupar dados em K clusters distintos, com base em suas características.

### Funcionamento passo a passo
1. Escolher K (número de clusters)
2. Inicializar centroides (aleatórios)
3. Associar cada ponto ao centro mais próximo
4. Recalcular os centroides
5. Repetir até convergir

### Diagrama (slide)

        (Usuários com gostos similares)

            ●       ●
        ●       ●        ●

                ↓

        Cluster 1 (Ação)
        Cluster 2 (Romance)
        Cluster 3 (Drama)

                ↓

     Recomendações por grupo

### Explicação simples (apresentação)

“O K-means agrupa usuários com gostos parecidos. Então, em vez de recomendar baseado em uma pessoa só, usamos o comportamento do grupo inteiro para sugerir filmes.”

### Diferencial (para impressionar)

“Utilizamos uma abordagem híbrida combinando similaridade entre usuários e clusterização, aumentando a precisão das recomendações.”

---

## 4. Resultados

- O sistema retorna recomendações personalizadas para cada usuário.
- Clusters identificam grupos de interesse (ex: ação, romance, etc).
- Métrica de avaliação: média das notas dos filmes recomendados.

---

## 5. Conclusão

### Impacto
- O sistema facilita a descoberta de novos filmes, aumenta o engajamento e pode ser expandido para outras plataformas.

### Limitações
- Não considera feedback explícito do usuário (curti/não curti).
- Não utiliza ainda características de conteúdo (gênero, descrição).

### Ética
- Possível formação de bolhas de recomendação (usuário só vê mais do mesmo).
- Viés algorítmico: recomendações podem reforçar padrões existentes.

### Sugestões de Evolução
- Implementar recomendação híbrida (K-means + similaridade + conteúdo).
- Adicionar feedback do usuário para refinar recomendações.
- Explorar métricas como precisão, recall e diversidade.

---

## 6. Referências
- [MovieLens Dataset](https://grouplens.org/datasets/movielens/)
- [Scikit-learn](https://scikit-learn.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

---

## Justificativa da Escolha do Número de Clusters (K)

Para definir o número ideal de clusters no algoritmo K-means, foi utilizado o método do cotovelo (Elbow Method). Esse método consiste em executar o algoritmo para diferentes valores de K e analisar a inércia (soma das distâncias dos pontos ao centro do cluster).

Observou-se que, à medida que o número de clusters aumenta, a inércia diminui. No entanto, após um determinado ponto, essa redução passa a ocorrer de forma menos significativa, formando um “cotovelo” no gráfico.

Com base na análise visual do gráfico gerado, identificou-se que o ponto de inflexão ocorre aproximadamente em K = 5. A partir desse valor, o ganho na redução da inércia torna-se marginal.

Dessa forma, optou-se por utilizar K = 5, pois representa um bom equilíbrio entre:
- qualidade da segmentação dos usuários
- complexidade do modelo

A escolha de um número adequado de clusters é fundamental para evitar:
- Underfitting (poucos clusters, pouca representatividade)
- Overfitting (clusters demais, excesso de fragmentação)

**Frase para apresentação:**

“Utilizamos o método do cotovelo para encontrar o número ideal de clusters, garantindo um equilíbrio entre precisão e complexidade do modelo.”

---

**Projeto desenvolvido seguindo roteiro de arquitetura recomendado para sistemas de recomendação inteligentes.**
