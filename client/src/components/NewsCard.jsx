// NewsCard.jsx
import React from "react";

const NewsCard = ({ news }) => {
  return (
    <div
      style={{
        border: "1px solid #ddd",
        borderRadius: "8px",
        padding: "10px",
        marginBottom: "12px",
        maxWidth: "600px",
      }}
    >
      <h4>{news.headline}</h4>
      <p>{news.summary}</p>
      {news.image && (
        <img
          src={news.image}
          alt="news"
          style={{ maxWidth: "100%", borderRadius: "5px" }}
        />
      )}
      <p>
        <a href={news.url} target="_blank" rel="noreferrer">
          Read more
        </a>
      </p>
      <small>
        Published: {new Date(news.datetime * 1000).toLocaleString()}
      </small>
    </div>
  );
};

export default NewsCard;
