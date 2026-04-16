import pandas as pd


COL = ["Date", "Open", "High", "Low", "Close", "Volume"]

def load_stock_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)

    missing_columns = [col for col in COL if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date").reset_index(drop=True)

    return df