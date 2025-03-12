from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import crud_stock_individual_info_em as crud_individual, crud_stock_zh_a_spot_em as crud_spot
from app.scheduler.a_task import sync_stock_zh_a_hist_job, sync_stock_zh_a_spot_em_job
from app.routers.response import ResponseModel, ResponseCode

router = APIRouter()

# 同步所有股票实时数据
@router.get("/stocks/sync")
def sync_all_stocks(db: Session = Depends(get_db)):
    sync_stock_zh_a_spot_em_job()
    return {"message": "Sync all stocks successfully"}

# 查询指定股票信息
@router.get("/stocks/code/{stock_code}")
def get_stock_info_by_code(stock_code: str, db: Session = Depends(get_db)):
    stock_info = crud_individual.get_stock_individual_info_by_code(db, stock_code)
    if stock_info is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock_info

# 同步指定股票历史行情数据
@router.get("/stocks/hist/sync")
def sync_stock_hist_data(stock_code: str, start_date: str):
    sync_stock_zh_a_hist_job(stock_code, start_date)
    return {"message": "同步指定股票历史行情数据成功"}

# 分页查询股票实时行情数据
@router.post("/stocks/spot/list")
def get_stock_spot_list(params: dict, db: Session = Depends(get_db)):
    query_result = crud_spot.get_stock_spot_list(db, params)
    return ResponseModel.from_code(ResponseCode.SUCCESS, data=query_result)
