import React, { useState, useRef, useEffect } from "react";
import axios from "axios";
import StockChart from "./StockChart";
import NewsCard from "./NewsCard";
import SectorChart from "./SectorChart";

const SearchStock = () => {
  const [symbol, setSymbol] = useState("");
  const [data, setData] = useState(null);
  const [chartData, setChartData] = useState([]);
  const [error, setError] = useState("");
  const ws = useRef(null); // ⬅️ Persistent WebSocket across renders
  const [news, setNews] = useState([]);

  const handleSearch = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/stock/${symbol}`);
      const chartRes = await axios.get(
        `http://localhost:8000/stock/${symbol}/intraday`
      );

      console.log("STATIC STOCK DATA:", response.data);
      console.log("CHART DATA:", chartRes.data);

      const newsRes = await axios.get(
        `http://localhost:8000/stock/${symbol}/news`
      );
      setNews(newsRes.data || []);

      if (Array.isArray(chartRes.data)) {
        setChartData(chartRes.data);
      } else {
        setChartData([]);
      }

      setData(response.data); // ✅ inside try block
      setError(""); // ✅ inside try block

      // Close existing socket
      if (ws.current) {
        ws.current.close();
      }

      const socket = new WebSocket("ws://localhost:8000/ws/stock");
      ws.current = socket;

      socket.onopen = () => {
        console.log("WebSocket connected");
        socket.send(symbol);
      };

      socket.onmessage = (event) => {
        const priceData = JSON.parse(event.data);
        console.log("Live data:", priceData);

        setData((prevData) => {
          if (!prevData) return null;
          return {
            ...prevData,
            price: priceData.price,
            timestamp: priceData.timestamp,
          };
        });
      };

      socket.onerror = (err) => {
        console.error("WebSocket error:", err);
        setError("WebSocket error");
      };
    } catch (err) {
      console.error("❌ API error:", err);
      setError("Stock not found or API error.");
      setData(null);
      setChartData([]);
    }
  };

  // Cleanup on unmount or re-search
  useEffect(() => {
    return () => {
      if (ws.current) {
        ws.current.close();
        console.log("🧹 WebSocket closed (cleanup)");
      }
    };
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Search Stock</h2>
      <input
        type="text"
        value={symbol}
        onChange={(e) => setSymbol(e.target.value)}
        placeholder="Enter stock symbol (e.g. AAPL)"
      />
      <button onClick={handleSearch}>Search</button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {data && (
        <div>
          <p>Price: ${data.price}</p>
          {data.volume && <p>Volume: {data.volume}</p>}
          <p>Time: {data.timestamp}</p>

          {chartData.length > 0 ? (
            <StockChart chartData={chartData} />
          ) : (
            <p>No chart data available.</p>
          )}

          {news.length > 0 && (
            <div>
              <h3>📰 Latest News</h3>
              {news.map((item, idx) => (
                <NewsCard key={idx} news={item} />
              ))}
            </div>
          )}
        </div>
      )}

      {data && (
        <div>
          <p>Price: ${data.price}</p>
          <p>Volume: {data.volume}</p>
          <p>Time: {data.timestamp}</p>

          <StockChart chartData={chartData} />

          {/* ✅ Render sector performance chart */}
          <SectorChart />
        </div>
      )}
    </div>
  );
};

export default SearchStock;
