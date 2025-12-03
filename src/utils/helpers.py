# Helper functions
#etl 
#etl_runner.py

from src.etl.extract import load_csv_files
from src.etl.transform import transform
from src.etl.load import save_dataframe

RAW_FILES = ["data/raw/users_part1.csv", "data/raw/users_part2.csv"]

SCHEMA = {
    "user_id": "i",
    "first_name": "O",
    "last_name": "O",
    "email": "O",
    "phone": "O",
    "device_id": "O",
}

if __name__ == "__main__":
    df_raw = load_csv_files(RAW_FILES, SCHEMA)
    df_tx = transform(df_raw)
    save_dataframe(df_tx, "data/processed/users_transformed.csv")
