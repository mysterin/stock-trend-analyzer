from sqlalchemy.orm import Session
from app.models.stock_zh_a_spot_em import StockZhASpotEm

def get_stock_individual_info_by_code(db: Session, stock_code: str):
    return db.query(StockZhASpotEm).filter(StockZhASpotEm.stock_code == stock_code).first()

def delete_all(db: Session):
    db.query(StockZhASpotEm).delete()
    db.commit()

def insert(db: Session, stock: StockZhASpotEm):
    db.add(stock)
    db.commit()
