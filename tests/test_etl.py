# tests/test_etl.py

import pandas as pd
import pytest
from src.etl.extract import validate_schema
from src.etl.transform import clean_data, create_baseline_features, transform

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "user_id": [1, 2],
        "first_name": ["Alice", "Bob"],
        "last_name": ["Smith", "Jones"],
        "email": ["alice@example.com", "bob@example.com"],
        "phone": ["1234567890", "9876543210"],
        "device_id": ["dev1", "dev2"]
    })

def test_validate_schema_pass(sample_df):
    schema = {
        "user_id": "i",
        "first_name": "O",
        "last_name": "O",
        "email": "O",
        "phone": "O",
        "device_id": "O"
    }
    assert validate_schema(sample_df, schema) == True

def test_clean_data_removes_whitespace(sample_df):
    sample_df["first_name"] = [" Alice ", " Bob "]
    df_clean = clean_data(sample_df)
    assert all(df_clean["first_name"] == ["alice", "bob"])

def test_baseline_features(sample_df):
    df_feat = create_baseline_features(sample_df)
    assert "email_domain" in df_feat.columns
    assert "phone_prefix" in df_feat.columns
    assert "name_email_match" in df_feat.columns
    assert "device_risk_score" in df_feat.columns

def test_full_transform(sample_df):
    df_transformed = transform(sample_df)
    assert "email_domain" in df_transformed.columns
    assert "phone_prefix" in df_transformed.columns
