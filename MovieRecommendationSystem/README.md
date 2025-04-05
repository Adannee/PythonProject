#  Movie Recommendation System

A personalized movie recommendation system built using the **MovieLens dataset** and implemented with **Collaborative Filtering** and **Content-Based Filtering** techniques.

##  Dataset

- **Source:** [MovieLens 100k Dataset](https://grouplens.org/datasets/movielens/)
- **Files:**
  - `movies.dat`: Movie IDs and titles
  - `ratings.dat`: User IDs, movie IDs, ratings, timestamps


## Features

- **Collaborative Filtering** using SVD
- **Movie-based Recommendations** (Content Similarity)
- **Web Interface** built with Flask
- **Model Serialization** with Pickle (`model.pkl`)
- **CLI Support** for offline testing

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Adannee/PythonProject.git
cd PythonProject/MovieRecommendationSystem
```
### 2. Create a Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate 
```
### 3. Install Requirements
```bash
pip install -r requirements.txt
```
### 4. Train the Model
```bash
python model/train_model.py
```
###5. Run the Web App
```bash
cd app
python app.py
```
Then open http://127.0.0.1:5000 in your browser.

---

