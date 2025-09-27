# 📈 Real-Time Stock & News Dashboard

A sleek and responsive dashboard that allows users to:
- 🔍 Search for stock prices
- 📈 View real-time intraday charts
- 📰 Read latest news for a stock
- 🧠 Monitor sector performance (local only)

Live Demo 👉 [https://stock-news-dashboard.vercel.app](https://stock-news-dashboard.vercel.app)

---

## 🚀 Features

- **🔍 Stock Search** – Fetches current stock prices & volume via Finnhub API
- **📈 Intraday Charts** – Visualizes last 100 mins of price movement using Twelve Data API
- **📰 Company News** – Pulls recent company news via Finnhub API
- **📊 Sector Performance** – Displays sector performance chart *(requires local environment)*
- **🌐 WebSocket Updates** – Live price updates every 5 seconds
- **⚡ Fast & Modern UI** – Built with React + Recharts

---

## 🛠️ Tech Stack

- **Frontend:** React, Axios, Recharts, WebSocket API
- **Backend:** FastAPI, Python, Uvicorn
- **APIs Used:**
  - [Finnhub](https://finnhub.io/) – Real-time price & news
  - [Twelve Data](https://twelvedata.com/) – Intraday chart + sectors
- **Deployment:**
  - Frontend → Vercel
  - Backend → Render

---

## 📸 Screenshots

### 🔍 Search & Live Stock Updates
![Search and Live Price](./screenshot1.png)

### 📈 Intraday Price Chart
![Intraday Chart](./screenshot2.png)

### 📰 Latest News Section
![News Section](./screenshot3.png)

### 📊 Sector Performance (Local Only)
> Note: This chart uses a premium API and may not work in the live deployment.
![Sector Chart](./screenshot4.png)

---

## 🧪 Run Locally (for Full Features)

### 1. Clone the repo
```bash
git clone https://github.com/MaheshVenkatReesu/stock-news-dashboard.git
cd stock-news-dashboard

2. Set up Backend

cd server
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Create a .env file:

FINNHUB_API_KEY=your_finnhub_key
TWELVE_DATA_API_KEY=your_twelve_data_key

Run the server:

uvicorn main:app --reload --port 10000

3. Set up Frontend

cd client
npm install
npm start

Make sure API URLs in the frontend point to http://localhost:10000

⸻

🌍 Deployment
	•	Frontend: Push to GitHub → Auto deployed to Vercel
	•	Backend: Connect GitHub repo to Render and deploy with Python 3.13 and FastAPI

⸻

❗ Known Limitations
	•	Sector performance chart does not work on deployed site (Twelve Data restriction)
	•	Free API plans have rate limits

⸻

🙌 Acknowledgements
	•	Finnhub.io
	•	TwelveData.com
	•	Render
	•	Vercel

⸻

📬 Contact

Mahesh Venkat Reesu
