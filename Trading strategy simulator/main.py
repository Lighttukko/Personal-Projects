from fastapi import FastAPI
from data_loader import load_stock_data


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Trading Strategy Simulator API is running. This message is used for testing."}

@app.get("/stock-preview")
def stock_preview():
    df = load_stock_data("data/aapl.csv")
    preview_data = df.head(5).to_dict(orient="records")

    return {
        "rows_loaded": len(df),
        "preview": preview_data
    }

