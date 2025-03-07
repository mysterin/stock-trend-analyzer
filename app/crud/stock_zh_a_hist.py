from sqlalchemy.orm import Session
from app.models.stock_zh_a_hist import StockZhAHist

def get_stock_by_code_and_trade_date(db: Session, stock_code: str, trade_date: str):
    return db.query(StockZhAHist).filter(StockZhAHist.stock_code == stock_code, StockZhAHist.trade_date == trade_date).first()

def insert(db: Session, stock: StockZhAHist):
    db.add(stock)
    db.commit()

def update(db: Session, stock: StockZhAHist):
    update_value = stock.__dict__.copy()
    update_value.pop('id', None)
    update_value.pop('stock_code', None)
    update_value.pop('trade_date', None)
    update_value.pop('_sa_instance_state', None)
    db.query(StockZhAHist).filter(StockZhAHist.stock_code == stock.stock_code, StockZhAHist.trade_date == stock.trade_date).update(update_value, synchronize_session=False)
    db.commit()
