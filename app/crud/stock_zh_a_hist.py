from sqlalchemy.orm import Session
from app.models import stock_zh_a_hist

def get_stock_by_code_and_trade_date(db: Session, stock_code: str, trade_date: str):
    return db.query(stock_zh_a_hist.StockZhAHist).filter(stock_zh_a_hist.StockZhAHist.stock_code == stock_code, stock_zh_a_hist.StockZhAHist.trade_date == trade_date).first()

def insert(db: Session, stock: stock_zh_a_hist.StockZhAHist):
    db.add(stock)
    db.commit()

def update(db: Session, stock: stock_zh_a_hist.StockZhAHist):
    db.query(stock_zh_a_hist.StockZhAHist).filter(stock_zh_a_hist.StockZhAHist.stock_code == stock.stock_code, stock_zh_a_hist.StockZhAHist.trade_date == stock.trade_date).update(stock)
    db.commit()
