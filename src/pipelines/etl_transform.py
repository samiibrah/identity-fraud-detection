# src/etl/transform.py

import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning: strip strings, standardize casing, handle nulls.
    """
    logger.info("Cleaning data...")

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip().str.lower()

    df = df.drop_duplicates()
    df = df.fillna({"email": "unknown", "phone": "unknown"})

    return df


def create_baseline_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create simple fraud-related engineered features.
    """
    logger.info("Engineering features...")

    df["email_domain"] = df["email"].str.split("@").str[-1]
    df["phone_prefix"] = df["phone"].str[:3]

    df["name_email_match"] = df.apply(
        lambda r: int(r["first_name"] in r["email"] or r["last_name"] in r["email"]),
        axis=1,
    )

    df["device_risk_score"] = df["device_id"].map(df["device_id"].value_counts())

    return df


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Full ETL transformation pipeline.
    """
    df = clean_data(df)
    df = create_baseline_features(df)
    logger.info("Transformation complete.")
    return df
