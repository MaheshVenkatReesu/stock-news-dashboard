import React from "react";
import SearchStock from "./components/SearchStock";
import SectorChart from "./components/SectorChart";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>📊 Real-Time Stock & News Dashboard</h1>

      <SearchStock />

      <hr style={{ margin: "40px 0" }} />

      <h2>📈 Market Sector Performance</h2>
      <SectorChart />
    </div>
  );
}

export default App;
