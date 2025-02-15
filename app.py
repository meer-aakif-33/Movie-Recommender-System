# import streamlit as st
# import pickle
# import pandas as pd

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

# # def get_movie_images(movie_id):
# #     """Fetch movie poster and backdrop image URLs using TMDB API."""
# #     url = f"{BASE_URL}/movie/{movie_id}"
# #     headers = {
# #         "accept": "application/json",
# #         "Authorization": f"Bearer {ACCESS_TOKEN}"
# #     }
    
# #     response = requests.get(url, headers=headers)
    
# #     if response.status_code == 200:
# #         data = response.json()
# #         poster_url = f"{IMAGE_BASE_URL}{data['poster_path']}" if data.get('poster_path') else None
# #         backdrop_url = f"{IMAGE_BASE_URL}{data['backdrop_path']}" if data.get('backdrop_path') else None
# #         return poster_url, backdrop_url
# #     else:
# #         print(f"Error {response.status_code}: {response.text}")
# #         return None, None  # Return None if there's an error

# # # Example: Fetch images for a movie
# # movie_id = 343611  # Jack Reacher: Never Go Back
# # poster_url, backdrop_url = get_movie_images(movie_id)

# # if poster_url or backdrop_url:  # Check if at least one image exists
# #     print(f"\n🎥 Poster: {poster_url if poster_url else 'No poster available'}")
# #     print(f"🌆 Backdrop: {backdrop_url if backdrop_url else 'No backdrop available'}")
# def get_movie_details(movie_id):
#     """Fetch movie poster, backdrop image, and description using TMDB API."""
#     url = f"{BASE_URL}/movie/{movie_id}"
#     headers = {
#         "accept": "application/json",
#         "Authorization": f"Bearer {ACCESS_TOKEN}"
#     }
    
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         data = response.json()
#         poster_url = f"{IMAGE_BASE_URL}{data['poster_path']}" if data.get('poster_path') else None
#         description = data.get('overview', 'No description available.')
#         return poster_url, description
#     else:
#         print(f"Error {response.status_code}: {response.text}")
#         return None, "No description available."  # Return a default description if error

# # def recommend(movie):
# #     movie_index = movies[movies['title']==movie].index[0]
# #     distances = sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x:x[1])

# #     recommended_movies = []
# #     recommended_movies_posters = []
    
# #     for i in distances[1:6]:
# #         index = i[0]
# #         movie_id = movies.iloc[index]['movie_id']  # Extract correct TMDB movie_id

# #         #fetch poster from API
# #         recommended_movies.append(movies.iloc[index]['title'])
# #         poster, backdrop = get_movie_images(movie_id)
# #         recommended_movies_posters.append(poster)
# #     return recommended_movies, recommended_movies_posters  # Return both

# movies_dict = pickle.load(open('movies.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)

# similarity = pickle.load(open('similarity.pkl', 'rb'))

# st.title('Movie Recommender System')

# selected_movie_name = st.selectbox(
#     'which movie you want to select', movies['title'].values
# )
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])

#     recommended_movies = []
#     recommended_movies_posters = []
#     recommended_movies_descriptions = []  # Store descriptions
    
#     for i in distances[1:6]:
#         index = i[0]
#         movie_id = movies.iloc[index]['movie_id']  # Extract TMDB movie_id

#         # Fetch details from API
#         poster, description = get_movie_details(movie_id)
        
#         recommended_movies.append(movies.iloc[index]['title'])
#         recommended_movies_posters.append(poster)
#         recommended_movies_descriptions.append(description)
    
#     return recommended_movies, recommended_movies_posters, recommended_movies_descriptions



# # if st.button('Recommendation'):
# #     recommended_movies, poster_url = recommend(selected_movie_name)
# #     for i in recommended_movies, poster:
# #         st.image(poster, caption=title, width=200)
# #         st.write(i)
# # if st.button('Recommendation'):
# #     recommended_movies, recommended_movies_posters = recommend(selected_movie_name)  # Corrected return values
    
# #     for title, poster in zip(recommended_movies, recommended_movies_posters):  # Corrected iteration
# #         if poster:  # Ensure the poster is not None
# #             st.image(poster, caption=title, width=200)
# #         st.write(title)  # Display movie title
import streamlit as st
import joblib
import pandas as pd

import os
from dotenv import load_dotenv
import requests

# Load API Token from .env
load_dotenv()
ACCESS_TOKEN = os.getenv("TMDB_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise ValueError("TMDB_ACCESS_TOKEN is missing. Check your .env file.")

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"  # Use w500 for posters

def get_movie_details(movie_id):
    """Fetch movie poster, backdrop image, and description using TMDB API."""
    url = f"{BASE_URL}/movie/{movie_id}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        poster_url = f"{IMAGE_BASE_URL}{data['poster_path']}" if data.get('poster_path') else None
        description = data.get('overview', 'No description available.')
        return poster_url, description
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None, "No description available."  # Return a default description if error

# # Load data using joblib
# movies_dict = joblib.load("movies.pkl")
# joblib.dump(movies_dict, "movies_compressed.pkl", compress=3)  # Save compressed

movies_dict = joblib.load("movies.pkl")  # Load original
movies = pd.DataFrame(movies_dict)


similarity = joblib.load("similarity_compressed.pkl")

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Which movie do you want to select?', movies['title'].values
)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_descriptions = []  # Store descriptions
    
    for i in distances[1:6]:
        index = i[0]
        movie_id = movies.iloc[index]['movie_id']  # Extract TMDB movie_id

        # Fetch details from API
        poster, description = get_movie_details(movie_id)
        
        recommended_movies.append(movies.iloc[index]['title'])
        recommended_movies_posters.append(poster)
        recommended_movies_descriptions.append(description)
    
    return recommended_movies, recommended_movies_posters, recommended_movies_descriptions
if st.button('Recommendation'):
    recommended_movies, recommended_movies_posters, recommended_movies_descriptions = recommend(selected_movie_name)  
    
    st.subheader("Recommended Movies:")
    
    for title, poster, description in zip(recommended_movies, recommended_movies_posters, recommended_movies_descriptions):
        col1, col2 = st.columns([1, 3])  # Creates two columns: one for the image, one for text
        
        with col1:
            if poster:
                st.image(poster, width=150)  # Display the poster

        with col2:
            st.markdown(f"### {title}")  # Movie title
            st.write(description)  # Movie description
            st.markdown("---")  # Adds a horizontal line for separation
