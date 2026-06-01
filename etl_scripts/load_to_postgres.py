import pandas as pd
from sqlalchemy import create_engine
from extract import extract_data
from transform import transform_data


# -----------------------------
# DATABASE CONFIG
# -----------------------------

DB_CONFIG = {
    "user": "postgres",
    "password": "your_password",
    "host": "localhost",
    "port": "5432",
    "database": "airline_db"
}


# -----------------------------
# CREATE DATABASE CONNECTION
# -----------------------------

def get_engine():

    engine = create_engine(
        f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )

    return engine


# -----------------------------
# LOAD DATA
# -----------------------------

def load_data(df, table_name="fact_airline_flights", mode="append"):

    engine = get_engine()

    print("\n==============================")
    print("LOADING DATA TO POSTGRESQL")
    print("==============================")

    try:

        # safety check
        if df is None or df.empty:
            raise ValueError("DataFrame is empty. Nothing to load.")

        if mode not in ["append", "replace"]:
            raise ValueError("mode must be 'append' or 'replace'")

        print("\nColumns being loaded:")
        print(df.columns.tolist())

        df.to_sql(
            name=table_name,
            con=engine,
            if_exists=mode,
            index=False
        )

        print(f"\nSUCCESS: Data loaded into table '{table_name}'")
        print(f"Mode: {mode}")
        print(f"Rows inserted: {len(df)}")

    except Exception as e:
        print("\nERROR WHILE LOADING DATA:")
        print(str(e))


# -----------------------------
# MAIN ETL PIPELINE
# -----------------------------

if __name__ == "__main__":

    print("\n==============================")
    print("AIRLINE ETL PIPELINE STARTED")
    print("==============================")

    # 1. EXTRACT
    print("\n[1/3] Extracting data...")
    df = extract_data()

    print(f"Extracted shape: {df.shape}")

    # 2. TRANSFORM
    print("\n[2/3] Transforming data...")
    df = transform_data(df)
    df.columns = df.columns.str.lower()
    
    print(f"Transformed shape: {df.shape}")

    # 3. LOAD
    print("\n[3/3] Loading data into PostgreSQL...")
    load_data(df, mode="append")

    print("\n==============================")
    print("ETL PIPELINE COMPLETED SUCCESSFULLY 🚀")
    print("==============================")