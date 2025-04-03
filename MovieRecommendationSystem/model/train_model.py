import pandas as pd
import pickle
from surprise import SVD
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split


ratings = pd.read_csv("data/ratings.dat", sep="::", engine="python", names=["userId", "movieId", "rating", "timestamp"])  


reader = Reader(rating_scale=(0.5, 5.0))


data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)


trainset, testset = train_test_split(data, test_size=0.2, random_state=42)


model = SVD()
model.fit(trainset)


with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model training completed & saved as 'model.pkl'")