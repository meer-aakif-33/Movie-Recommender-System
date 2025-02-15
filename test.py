# import os
# from dotenv import load_dotenv
# import requests

# # Load API Token from .env
# load_dotenv()
# ACCESS_TOKEN = os.getenv("TMDB_ACCESS_TOKEN")

# if not ACCESS_TOKEN:
#     raise ValueError("TMDB_ACCESS_TOKEN is missing. Check your .env file.")

# BASE_URL = "https://api.themoviedb.org/3"
# IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"  # Use w500 for posters

# def get_movie_details(movie_id):
#     """Fetch movie details using TMDB API v4 token."""
#     url = f"{BASE_URL}/movie/{movie_id}"
#     headers = {
#         "accept": "application/json",
#         "Authorization": f"Bearer {ACCESS_TOKEN}"
#     }
    
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Error {response.status_code}: {response.text}")
#         return None

# # Example: Fetch details for a movie
# movie_id = 343611  # Jack Reacher: Never Go Back
# details = get_movie_details(movie_id)

# if details:
#     poster_url = f"{IMAGE_BASE_URL}{details['poster_path']}" if details['poster_path'] else "No poster available"
#     backdrop_url = f"{IMAGE_BASE_URL}{details['backdrop_path']}" if details['backdrop_path'] else "No backdrop available"

#     # print(f"\n🎬 Title: {details['title']}")
#     # print(f"📅 Release Date: {details['release_date']}")
#     # print(f"⌛ Runtime: {details['runtime']} minutes")
#     # print(f"⭐ Rating: {details['vote_average']} ({details['vote_count']} votes)")
#     # print(f"🎭 Genres: {', '.join([genre['name'] for genre in details['genres']])}")
#     # print(f"💰 Budget: ${details['budget']:,}")
#     # print(f"💵 Revenue: ${details['revenue']:,}")
#     # print(f"🌎 Production Countries: {', '.join([country['name'] for country in details['production_countries']])}")
#     # print(f"\n📜 Overview: {details['overview']}")
#     print(f"\n🎥 Poster: {poster_url}")
#     print(f"🌆 Backdrop: {backdrop_url}")
#     # print(f"\n🔗 Homepage: {details['homepage']}" if details['homepage'] else "")
# Compress movies.pkl
import joblib
movies_dict = joblib.load("movies.pkl")  # Load original
joblib.dump(movies_dict, "movies_compressed.pkl", compress=3)  # Save compressed

# Compress similarity.pkl
similarity = joblib.load("similarity.pkl")
joblib.dump(similarity, "similarity_compressed.pkl", compress=3)
