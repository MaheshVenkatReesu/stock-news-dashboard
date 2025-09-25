# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "FastAPI is running 🎉"}

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers import stock

app = FastAPI()

# CORS setup to allow frontend (React) to access backend (FastAPI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Optional: Replace * with ["http://localhost:3000"] for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stock.router)