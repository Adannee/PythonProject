import pickle
import pandas as pd
import numpy as np
from surprise import SVD
from surprise import Dataset, Reader
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from model.recommendation import get_recommendations

ratings = pd.read_csv("/Users/ivyadiele/Desktop/PythonProject/MovieRecommendationSystem/data/ratings.dat", sep="::", engine="python", names=["userId", "movieId", "rating", "timestamp"])  
movies = pd.read_csv("/Users/ivyadiele/Desktop/PythonProject/MovieRecommendationSystem/data/movies.dat", sep="::", engine='python', names=["MovieID", "Title", "Genres"], encoding="ISO-8859-1")


ratings.columns = ratings.columns.str.strip()
movies.columns = movies.columns.str.strip()

with open("/Users/ivyadiele/Desktop/PythonProject/MovieRecommendationSystem/model/model.pkl", "rb") as f:
    model_svd = pickle.load(f)


reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(ratings[["userId", "movieId", "rating"]], reader)
trainset = data.build_full_trainset()

# Function to recommend movies for a given user
def recommend_movies(user_id, num_recommendations=5):
    if user_id not in ratings["userId"].unique():
        print(f"User ID {user_id} not found in the dataset.")
        return []

    # Get all unseen movies
    seen_movies = ratings[ratings["userId"] == user_id]["movieId"].unique()
    all_movies = movies["MovieID"].unique()
    unseen_movies = [movie for movie in all_movies if movie not in seen_movies]

    # Predict ratings for unseen movies
    predictions = []
    for movie_id in unseen_movies:
        predicted_rating = model_svd.predict(user_id, movie_id).est
        predictions.append((movie_id, predicted_rating))

    # Sort by highest predicted ratings
    predictions.sort(key=lambda x: x[1], reverse=True)
    recommended_movies = [movies[movies["MovieID"] == movie[0]]["Title"].values[0] for movie in predictions[:num_recommendations]]

    return recommended_movies

# Example usage
if __name__ == "__main__":
    user_id = 1  # Change to test different users
    print(f"\nRecommended movies for User {user_id}:")
    recommendations = recommend_movies(user_id)
    for i, movie in enumerate(recommendations, 1):
        print(f"{i}. {movie}")
