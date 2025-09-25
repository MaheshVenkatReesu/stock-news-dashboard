from fastapi import APIRouter, HTTPException
from services.stock_service import get_stock_data

router = APIRouter()

@router.get("/stock/{symbol}")
def stock_endpoint(symbol: str):
    try:
        data = get_stock_data(symbol)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))