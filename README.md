# 📈 Real-Time Stock & News Dashboard

A sleek, full-stack dashboard to track real-time stock prices, intraday charts, live news updates, and sector performance — all in one place.

🌐 **Live Demo**: [Frontend on Vercel](https://stock-news-dashboard-htfuo0y63-maheshvenkatreesus-projects.vercel.app)  
🔧 **Backend API**: [Render API](https://stock-news-backend-hc0n.onrender.com)

---

## 🚀 Features

- 🔍 Search any stock (e.g., AAPL, TSLA, MSFT)
- 📉 Real-time stock prices (via WebSocket)
- 🕒 Intraday chart (5-minute intervals)
- 📰 Latest financial news
- 📊 Sector performance (via Twelve Data API)
- ⚠️ Graceful error handling & fallback UI
- 🔐 Free-tier API compatible

---

## 🛠️ Tech Stack

### Frontend
- React.js + Vite
- Recharts for charting
- Axios for API calls
- Deployed on **Vercel**

### Backend
- FastAPI (Python)
- WebSocket (live prices)
- Finnhub API (quotes, news)
- Twelve Data API (intraday + sector)
- Deployed on **Render**

---

## 📸 Screenshots

> _(You can add your own screenshots or GIFs here later)_

---

## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/MaheshVenkatReesu/stock-news-dashboard.git
cd stock-news-dashboard



2. Environment Variables


FINNHUB_API_KEY=your_finnhub_api_key
TWELVE_DATA_API_KEY=your_twelve_data_api_key

3. Start Backend

cd server
uvicorn main:app --reload --port 10000

4. Start Frontend

cd client
npm install
npm run dev



🌍 Deployment Notes
	•	Backend is hosted on Render
	•	Frontend is auto-deployed via Vercel
	•	Make sure CORS is enabled in FastAPI for frontend origin

⸻

🙌 Credits
	•	Finnhub.io
	•	Twelve Data

⸻

🧠 Future Improvements
	•	Add dark mode toggle
	•	Pagination for news
	•	Sector performance with historical charts
	•	User portfolios / watchlist

⸻

📄 License

MIT License



https://github.com/user-attachments/assets/8a7850ec-3f1d-43b8-99a5-8348420fff71

https://github.com/user-attachments/assets/9353b11e-a4f4-415a-b353-9b5fb015e147
