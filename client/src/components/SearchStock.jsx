import React, { useState } from "react";
import axios from "axios";

const SearchStock = () => {
  const [symbol, setSymbol] = useState("");
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  const handleSearch = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/stock/${symbol}`);
      setData(response.data);
      setError("");
    } catch (err) {
      console.error(err);
      setError("Stock not found or API error.");
      setData(null);
    }
  };

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
          <h3>{data.symbol}</h3>
          <p>
            <strong>Price:</strong> ${data.price}
          </p>
          <p>
            <strong>Volume:</strong> {data.volume}
          </p>
          <p>
            <strong>Timestamp:</strong> {data.timestamp}
          </p>
        </div>
      )}
    </div>
  );
};

export default SearchStock;
