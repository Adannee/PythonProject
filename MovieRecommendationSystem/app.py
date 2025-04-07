from flask import Flask, render_template, request
import pickle
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "model"))

from recommendation import get_recommendations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    if request.method == "POST":
        movie_name = request.form["movie"]
        recommendations = get_recommendations(movie_name)
    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
