# api/fastapi_ml.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
from pathlib import Path

app = FastAPI(title="Identity Fraud Detection ML API")

# Load processed dataset
DATA_PATH = Path("data/processed/users_transformed.csv")
MODEL_PATH = Path("models/fraud_model.pkl")

if not DATA_PATH.exists():
    raise FileNotFoundError(f"Processed dataset not found: {DATA_PATH}")
if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Trained model not found: {MODEL_PATH}")

df = pd.read_csv(DATA_PATH)
model = joblib.load(MODEL_PATH)

FEATURES = ["name_email_match", "device_risk_score", "phone_prefix"]

# Pydantic model for request
class UserRequest(BaseModel):
    user_id: int

@app.get("/")
def root():
    return {"message": "Identity Fraud Detection ML API is running"}

@app.post("/score")
def score_user(user: UserRequest):
    user_row = df[df["user_id"] == user.user_id]
    if user_row.empty:
        raise HTTPException(status_code=404, detail="User not found")

    X = user_row[FEATURES]
    score = model.predict_proba(X)[0, 1]  # probability of fraud
    is_high_risk = score >= 0.5

    return {
        "user_id": user.user_id,
        "fraud_score": round(score, 4),
        "is_high_risk": is_high_risk
    }
