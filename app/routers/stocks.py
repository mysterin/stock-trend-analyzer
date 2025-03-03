from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.stock_individual_info_em import get_stock_individual_info_by_code

router = APIRouter()

@router.get("/stocks/code/{stock_code}")
def get_stock_info_by_code(stock_code: str, db: Session = Depends(get_db)):
    stock_info = get_stock_individual_info_by_code(db, stock_code)
    if stock_info is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock_info
