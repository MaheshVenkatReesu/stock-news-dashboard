# main.py
import os
import asyncio
import requests
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from datetime import datetime
from fastapi import HTTPException
import time
from datetime import timedelta
from fastapi.responses import JSONResponse

load_dotenv()
app = FastAPI()

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
print("API KEY FROM ENV:", FINNHUB_API_KEY)

@app.get("/stock/{symbol}")
def get_stock(symbol: str):
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_API_KEY}"
    res = requests.get(url)
    data = res.json()

    if "c" not in data:
        return {"error": "Stock not found or API issue"}

    return {
        "symbol": symbol.upper(),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "price": data["c"],
        "volume": data.get("v", 0),
    }


@app.get("/stock/{symbol}/intraday")
def get_intraday(symbol: str):
    url = "https://api.twelvedata.com/time_series"
    params = {
        "symbol": symbol,
        "interval": "5min",
        "outputsize": 20,
        "apikey": os.getenv("TWELVE_DATA_API_KEY")
    }

    response = requests.get(url, params=params)
    data = response.json()
    print("Intraday response:", data)

    if "values" not in data:
        return {"error": "Data not found or API limit exceeded"}

    formatted_data = [
        {"time": entry["datetime"][11:16], "price": float(entry["open"])}
        for entry in reversed(data["values"])
    ]

    return formatted_data

@app.websocket("/ws/stock")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        symbol = await websocket.receive_text()
        print("WebSocket received symbol:", symbol)

        while True:
            res = requests.get(
                f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_API_KEY}"
            )
            data = res.json()

            await websocket.send_json({
                "price": data.get("c"),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            await asyncio.sleep(5)

    except WebSocketDisconnect:
        print("WebSocket closed")


@app.get("/stock/{symbol}/news")
def get_stock_news(symbol: str):
    try:
        to_date = datetime.utcnow().date()
        from_date = to_date - timedelta(days=3)

        url = "https://finnhub.io/api/v1/company-news"
        params = {
            "symbol": symbol,
            "from": from_date.isoformat(),
            "to": to_date.isoformat(),
            "token": FINNHUB_API_KEY
        }

        print("Fetching news with params:", params)
        response = requests.get(url, params=params)
        data = response.json()
        
        if not isinstance(data, list):
            print("News API error:", data)
            raise HTTPException(status_code=404, detail="News data not found")

        return data[:10]  # return latest 10 news items
    except Exception as e:
        print("Error fetching news:", e)
        return {"error": "News fetch failed"}


@app.get("/sectors")
def get_sector_performance():
    # url = f"https://finnhub.io/api/v1/stock/sector-performance?token={FINNHUB_API_KEY}"
    # response = requests.get(url)

    # try:
    #     data = response.json()
    #     print("✅ Sector data fetched:", data)
    #     return data
    # except Exception as e:
    #     print("❌ Error parsing sector data:", e)
    #     return {"error": "Unable to fetch sector data"}

    mock_data = [
        {"sector": "Technology", "change": 1.75},
        {"sector": "Healthcare", "change": -0.42},
        {"sector": "Financials", "change": 0.91},
        {"sector": "Consumer Discretionary", "change": 1.2},
        {"sector": "Energy", "change": -1.35},
        {"sector": "Industrials", "change": 0.56},
        {"sector": "Real Estate", "change": -0.85}
    ]
    return mock_data

from fastapi.responses import JSONResponse

@app.get("/sectors")
async def get_sector_data():
    TWELVE_DATA_API_KEY = os.getenv("TWELVE_DATA_API_KEY")
    url = f"https://api.twelvedata.com/sectors?apikey={TWELVE_DATA_API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        raw_data = response.json()

        if "data" in raw_data:
            # Format: [{'sector': 'Technology', 'change': '1.25'}, ...]
            sectors = [
                {
                    "sector": item["name"],
                    "change": float(item["change"]) if "change" in item else 0
                }
                for item in raw_data["data"]
            ]
            return sectors
        else:
            return {"error": "No sector data found."}
    except Exception as e:
        print("Sector fetch error:", e)
        return {"error": "Unable to fetch sector data"}

# @app.get("/market/sectors")
# async def get_sector_performance():
#     # Mock sector data to simulate real API
#     mock_data = [
#         {"sector": "Technology", "change": 1.75},
#         {"sector": "Healthcare", "change": -0.42},
#         {"sector": "Financials", "change": 0.91},
#         {"sector": "Consumer Discretionary", "change": 1.2},
#         {"sector": "Energy", "change": -1.35},
#         {"sector": "Industrials", "change": 0.56},
#         {"sector": "Real Estate", "change": -0.85},
#     ]
#     return JSONResponse(content=mock_data)

# Example using Twelve Data
@app.get("/market/gainers-losers")
def get_gainers_losers():
    try:
        API_KEY = os.getenv("TWELVE_DATA_API_KEY")
        url = f"https://api.twelvedata.com/stocks?sort=percent_change&apikey={API_KEY}"

        res = requests.get(url)
        raw_data = res.json()

        # Extract top 5 gainers and losers
        sorted_data = raw_data["data"][:20]  # adjust as needed
        gainers = sorted(sorted_data, key=lambda x: float(x["percent_change"]), reverse=True)[:5]
        losers = sorted(sorted_data, key=lambda x: float(x["percent_change"]))[:5]

        # Format
        formatted = lambda x: {
            "symbol": x["symbol"],
            "price": x["close"],
            "change": round(float(x["percent_change"]), 2)
        }

        return {
            "gainers": [formatted(g) for g in gainers],
            "losers": [formatted(l) for l in losers]
        }
    except Exception as e:
        print("Error fetching gainers/losers:", e)
        return {"error": "Unable to fetch data"}