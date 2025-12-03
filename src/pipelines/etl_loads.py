# src/etl/load.py

import pandas as pd
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def save_dataframe(df: pd.DataFrame, output_path: str) -> None:
    """
    Write transformed dataframe to a clean output directory.
    """
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)
    logger.info(f"Saved transformed dataset to {output_path} ({len(df)} rows).")
