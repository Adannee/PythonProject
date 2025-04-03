import pandas as pd
import pickle

# Load trained model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

def get_recommendations(movie_name):
    recommended_movies = model.get(movie_name, ["No recommendations found"])
    return recommended_movies