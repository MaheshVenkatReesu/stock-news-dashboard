import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

def get_stock_data(symbol: str):
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "5min",
        "apikey": API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception("Alpha Vantage API failed")

    data = response.json()

    # Check if response contains valid data
    if "Time Series (5min)" not in data:
        raise Exception("Invalid symbol or no data")

    latest_time = sorted(data["Time Series (5min)"].keys())[-1]
    latest_data = data["Time Series (5min)"][latest_time]

    return {
        "symbol": symbol.upper(),
        "timestamp": latest_time,
        "price": float(latest_data["1. open"]),
        "volume": int(latest_data["5. volume"])
    }