from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import requests
import logging

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)
CORS(app)

# API & logging setup
TMDB_API_KEY = '1e8e31cfbd232a7ad3e9e5eced2a5a37'
TMDB_API_URL = 'https://api.themoviedb.org/3'
logging.basicConfig(level=logging.DEBUG)

# Load datasets
def load_datasets():
    try:
        movies = pd.read_csv('movies.csv')
        ratings = pd.read_csv('ratings.csv')
        return movies, ratings
    except FileNotFoundError as e:
        logging.error(f"Error loading dataset: {e}")
        return None, None

movies, ratings = load_datasets()
if movies is None or ratings is None:
    @app.route('/recommend', methods=['POST'])
    def recommend():
        return jsonify({'error': 'Dataset files are missing or cannot be loaded'}), 500

# --- Preprocessing ---
movies['genres'] = movies['genres'].str.replace('|', ' ', regex=False)
avg_ratings = ratings.groupby('movieId')['rating'].mean().reset_index()
movies = movies.merge(avg_ratings, on='movieId', how='left')

# --- Content-based Filtering ---
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])
cos_sim = cosine_similarity(tfidf_matrix)
movie_idx = pd.Series(movies.index, index=movies['title'])


def get_content_recommendations(title, top_n=10):
    if title not in movie_idx:
        return []

    idx = movie_idx[title]
    sim_scores = list(enumerate(cos_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies.iloc[movie_indices][['title', 'rating']].values.tolist()

# --- Collaborative Filtering ---
user_item_matrix = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)
movie_user_matrix = user_item_matrix.T
model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
model_knn.fit(movie_user_matrix)

def get_collaborative_recommendations(movie_title, top_n=10):
    if movie_title not in movies['title'].values:
        return []

    movie_id = movies[movies['title'] == movie_title]['movieId'].values[0]
    if movie_id not in movie_user_matrix.index:
        return []

    distances, indices = model_knn.kneighbors([movie_user_matrix.loc[movie_id]], n_neighbors=top_n+1)
    recommended_ids = movie_user_matrix.index[indices.flatten()][1:]
    recommended_movies = movies[movies['movieId'].isin(recommended_ids)][['title', 'rating']]
    return recommended_movies.values.tolist()

# --- Hybrid Recommender ---
def get_hybrid_recommendations(title, top_n=10):
    content_recs = get_content_recommendations(title, top_n * 2)
    collab_recs = get_collaborative_recommendations(title, top_n * 2)

    content_dict = {m[0]: m[1] for m in content_recs}
    collab_dict = {m[0]: m[1] for m in collab_recs}
    
    hybrid_scores = {}
    for movie in set(content_dict) | set(collab_dict):
        c_score = content_dict.get(movie, 0)
        cf_score = collab_dict.get(movie, 0)
        hybrid_scores[movie] = (0.5 * c_score + 0.5 * cf_score)

    sorted_movies = sorted(hybrid_scores.items(), key=lambda x: x[1], reverse=True)[:top_n]

    # Enrich with TMDb posters
    final_recommendations = []
    for movie, score in sorted_movies:
        try:
            search_url = f'{TMDB_API_URL}/search/movie?api_key={TMDB_API_KEY}&query={movie}&language=en-US'
            response = requests.get(search_url).json()
            poster_path = response['results'][0]['poster_path'] if response['results'] else ''
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else ''
        except Exception as e:
            logging.error(f"Error fetching poster for {movie}: {e}")
            poster_url = ''

        final_recommendations.append({
            'title': movie,
            'score': round(score, 2),
            'poster': poster_url
        })

    return final_recommendations

# --- Flask Route ---
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    title = data.get('title')

    if not title:
        return jsonify({'error': 'Movie title is required'}), 400

    recommendations = get_hybrid_recommendations(title)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
