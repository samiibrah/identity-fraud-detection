# src/etl/extract.py

import pandas as pd
import logging
from typing import Dict, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def validate_schema(df: pd.DataFrame, schema: Dict[str, str]) -> bool:
    """
    Validate that dataframe columns match the expected schema.
    """
    missing = [col for col in schema if col not in df.columns]
    if missing:
        logger.error(f"Missing columns: {missing}")
        return False

    for col, expected_type in schema.items():
        if df[col].dtype.kind not in expected_type:
            logger.warning(f"Column '{col}' expected type {expected_type}, but got {df[col].dtype}")

    return True


def load_csv_files(paths: List[str], schema: Dict[str, str]) -> pd.DataFrame:
    """
    Load multiple CSVs and return a single concatenated dataframe.
    """
    dfs = []
    for p in paths:
        logger.info(f"Loading {p}")
        df = pd.read_csv(p)

        if not validate_schema(df, schema):
            raise ValueError(f"Schema validation failed for {p}")

        dfs.append(df)

    combined = pd.concat(dfs, ignore_index=True)
    logger.info(f"Loaded {len(combined)} total rows from {len(paths)} files.")
    return combined
