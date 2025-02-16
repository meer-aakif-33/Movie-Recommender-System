# Movie Recommender System

## Overview
This project is a **Movie Recommender System** built using **Python**, **Machine Learning**, and **Streamlit**. It suggests movies similar to a selected movie based on content similarity using **NLP techniques** and **cosine similarity**. Additionally, it fetches movie details (posters and descriptions) from **The Movie Database (TMDB) API** to enhance the recommendations.

## Features
- Content-based recommendation system using **cosine similarity**.
- **Streamlit** web app for user interaction.
- Fetches movie **posters** and **descriptions** using TMDB API.
- Uses **NLTK & Scikit-Learn** for **text processing** and **vectorization**.
- **Joblib & Pickle** for model serialization.

## Technologies Used
- **Python**
- **Pandas** & **NumPy** (Data Processing)
- **Scikit-Learn** (Machine Learning)
- **NLTK** (Text Processing)
- **Streamlit** (Web App Development)
- **Requests** (Fetching API Data)
- **TMDB API** (Fetching movie details)

## Dataset
We use the **TMDB 5000 Movies Dataset**, which consists of movie details such as **titles, genres, cast, crew, and keywords**. The dataset is preprocessed and merged with credit details to enhance recommendation accuracy.

## Installation
### 1. Clone the repository
```sh
https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```

### 2. Install dependencies
```sh
pip install -r requirements.txt
```

### 3. Setup TMDB API Key
- Create a `.env` file in the project root.
- Add the following line, replacing `YOUR_ACCESS_TOKEN` with your actual TMDB API token:
```sh
TMDB_ACCESS_TOKEN=YOUR_ACCESS_TOKEN
```

### 4. Run the Streamlit app
```sh
streamlit run app.py
```

## Project Structure
```
movie-recommender/
│── app.py                     # Streamlit Web App
│── movies.pkl                 # Preprocessed Movie Data
│── similarity.pkl              # Cosine Similarity Matrix
│── requirements.txt            # Dependencies
│── .env                        # API Key (Not included in GitHub)
│── README.md                   # Project Documentation
│── Machine Learning/
│   │── movie_recommender.ipynb # Jupyter Notebook (Data Processing)
│   
│   
```

## How It Works
1. **Data Preprocessing**
   - Load and merge the TMDB dataset with credit data.
   - Extract useful features: `genres`, `keywords`, `cast`, `crew`.
   - Apply NLP techniques to clean and preprocess text.
   - Convert text into numerical vectors using **CountVectorizer**.
   - Compute **cosine similarity** to measure movie similarity.
   
2. **Model Training & Storage**
   - Train a content-based recommendation model using **cosine similarity**.
   - Save the processed movie data and similarity matrix using **Pickle**.
   
3. **Web Application**
   - Use **Streamlit** for a user-friendly web interface.
   - Allow users to select a movie and get recommendations.
   - Fetch movie posters & descriptions via **TMDB API**.

## Example Output
When a user selects a movie, the system provides 5 similar movie recommendations along with:
- Movie posters
- Movie descriptions

## Improvements & Future Work
- Implement **Collaborative Filtering** for better recommendations.
- Deploy the application using **Heroku** or **AWS**.
- Add **user-based recommendations** based on watch history.
- Improve **UI design** for a better experience.

## Contributors
- **Meer Aakif** ([GitHub](https://github.com/meer-aakif-33))

## License
This project is licensed under the **MIT License**.

## Acknowledgments
- [The Movie Database (TMDB)](https://www.themoviedb.org/) for providing API access.
- [Kaggle](https://www.kaggle.com/) for the dataset.

