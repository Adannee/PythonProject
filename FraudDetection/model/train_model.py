from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle

df = pd.read_csv("/Users/ivyadiele/Desktop/PythonProject/FraudDetection/data/creditcard.csv")

X = df.drop(['Class'], axis = 1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = IsolationForest(n_estimators=100, contamination=0.001, random_state=42)
model.fit(X_scaled)

with open('/Users/ivyadiele/Desktop/PythonProject/FraudDetection/model/fraud_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('/Users/ivyadiele/Desktop/PythonProject/FraudDetection/model/fraud_model.pkl', 'rb') as f:
    model = pickle.load(f)
preds = model.predict(X_scaled)
df['Anomaly'] = [1 if x== -1 else 0 for x in preds]