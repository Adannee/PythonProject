import pandas as pd
import pickle

ratings = pd.read_csv("/Users/ivyadiele/Desktop/PythonProject/MovieRecommendationSystem/data/ratings.dat", sep="::", engine="python", names=["userId", "movieId", "rating", "timestamp"])  

# Load trained model
with open("/Users/ivyadiele/Desktop/PythonProject/MovieRecommendationSystem/model/model.pkl", "rb") as f:
    model_svd = pickle.load(f)

def get_recommendations(user_id):
    if user_id not in ratings["userId"].unique():
        print(f"User ID {user_id} not found in the dataset.")
        return []
