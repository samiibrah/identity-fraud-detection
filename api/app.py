print('API placeholder')
# api/fastapi_app.py

from fastapi import FastAPI, HTTPException
import pandas as pd
from pydantic import BaseModel
from pathlib import Path

app = FastAPI(title="Identity Fraud Detection API")

# Load processed dataset once at startup
DATA_PATH = Path("data/processed/users_transformed.csv")
if not DATA_PATH.exists():
    raise FileNotFoundError(f"Processed dataset not found: {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

# Pydantic model for API request
class UserRequest(BaseModel):
    user_id: int
    email: str
    phone: str
    device_id: str

@app.get("/")
def root():
    return {"message": "Identity Fraud Detection API is running"}

@app.post("/score")
def score_user(user: UserRequest):
    """
    Return a dummy fraud score based on simple rules from processed dataset.
    """
    user_row = df[df["user_id"] == user.user_id]
    if user_row.empty:
        raise HTTPException(status_code=404, detail="User not found")

    # Example scoring logic: higher score if device reused or name-email mismatch
    score = 0
    if user_row["device_risk_score"].values[0] > 1:
        score += 0.5
    if user_row["name_email_match"].values[0] == 0:
        score += 0.5

    return {
        "user_id": user.user_id,
        "fraud_score": round(score, 2),
        "is_high_risk": score >= 0.5
    }
