from flask import Flask, request, render_template
import pandas as pd
import pickle


with open("/Users/ivyadiele/Desktop/FraudDetection/model/fraud_model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction_result = None

    if request.method == "POST":
        file = request.files["/Users/ivyadiele/Desktop/FraudDetection/data/creditcard.csv"]

        if file:
            data = pd.read_csv(file)
            prediction = model.predict(data)
            frauds = sum(prediction == -1)
            total = len(prediction)

            prediction_result = {
                "frauds": frauds,
                "total": total,
                "message": f"Detected {frauds} fraudulent out of {total} transactions."
            }

    return render_template("index.html", result=prediction_result)

if __name__ == "__main__":
    app.run(debug=True)