import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

const SectorChart = () => {
  const [sectorData, setSectorData] = useState([]);

  useEffect(() => {
    const fetchSectorData = async () => {
      try {
        const response = await axios.get("http://localhost:8000/sectors");
        setSectorData(response.data);
      } catch (error) {
        console.error("Error fetching sector data:", error);
      }
    };

    fetchSectorData();
  }, []);

  return (
    <div style={{ width: "100%", height: 400, marginTop: "30px" }}>
      <ResponsiveContainer width="100%" height="100%">
        <div style={{ padding: "20px" }}>
          <h3>📊 Sector Performance</h3>
          <ResponsiveContainer width="100%" height={400}>
            <BarChart
              data={sectorData}
              layout="vertical"
              margin={{ top: 20, right: 30, left: 100, bottom: 20 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis
                type="number"
                domain={[-5, 5]}
                tickFormatter={(val) => `${val}%`}
              />
              <YAxis type="category" dataKey="sector" />
              <Tooltip formatter={(value) => `${value}%`} />
              <Bar dataKey="change" fill="#8884d8" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </ResponsiveContainer>
    </div>
  );
};

export default SectorChart;
