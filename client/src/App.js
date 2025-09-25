import React from "react";
import "./App.css";

function App() {
  return (
    <div className="App">
      <h1>📈 Real-Time Stock & News Dashboard</h1>

      <input type="text" placeholder="Enter stock ticker (e.g., AAPL)" />

      <div className="stock-info">
        <h2>Stock Info</h2>
        <p>Price: --</p>
        <p>Volume: --</p>
        <p>% Change: --</p>
      </div>

      <div className="chart-placeholder">
        <h2>1-Day Price Chart</h2>
        <p>[Chart will go here]</p>
      </div>

      <div className="news-section">
        <h2>Latest News</h2>
        <ul>
          <li>News item 1</li>
          <li>News item 2</li>
        </ul>
      </div>
    </div>
  );
}

export default App;
