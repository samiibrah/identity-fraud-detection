# Train model placeholder
# src/modeling/train_model.py

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report

# Load processed dataset
df = pd.read_csv("data/processed/users_transformed.csv")

# Features and target
FEATURES = ["name_email_match", "device_risk_score", "phone_prefix"]  # example features
TARGET = "is_fraud"  # add this column in your synthetic data

X = df[FEATURES]
y = df[TARGET]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = GradientBoostingClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "models/fraud_model.pkl")
print("Model saved to models/fraud_model.pkl")
