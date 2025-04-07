#  Credit Card Fraud Detection

This project implements a machine learning model to detect fraudulent credit card transactions using anomaly detection techniques like **Isolation Forest**. The goal is to accurately identify suspicious behavior in an imbalanced dataset.

---

## Dataset

- **Name**: Credit Card Fraud Detection
- **Source**: [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Size**: 150 MB (compressed as `data/data.zip`)
- **Features**:
  - Numerical features (V1 to V28) from PCA transformation
  - `Amount` – transaction amount
  - `Class` – target variable (`0`: Normal, `1`: Fraud)

---

## Model Overview

- **Technique**: Unsupervised Learning / Anomaly Detection
- **Algorithm**: `IsolationForest` (from `sklearn.ensemble`)
- **Imbalance Handling**: Model trained on full data but flagged only rare anomalies

---
##  How to Run

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/PythonProject.git
cd PythonProject/FraudDetectionApp
```

2. **Install dependencies
```bash
pip install -r requirements.txt
```

3. **Extract dataset
```bash
unzip data/data.zip -d data/
```
4. **Run the Flask app
```bash
python app.py
```
5. **Visit your browser

Go to http://127.0.0.1:5000

---
