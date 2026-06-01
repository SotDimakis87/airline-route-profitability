
import pandas as pd
from pathlib import Path

def extract_data():
    file_path = Path.cwd().parent / "data" / "raw" / "airline_route_profitability.csv"
    return pd.read_csv(file_path)

if __name__ == "__main__":
    df = extract_data()

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(df.head())
