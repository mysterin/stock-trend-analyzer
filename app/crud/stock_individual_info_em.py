from sqlalchemy.orm import Session
from app.models.stock_individual_info_em import StockIndividualInfoEm

def get_stock_individual_info_by_code(db: Session, stock_code: str):
    return db.query(StockIndividualInfoEm).filter(StockIndividualInfoEm.stock_code == stock_code).first()

def get_stock_individual_info_by_name(db: Session, stock_name: str):
    return db.query(StockIndividualInfoEm).filter(StockIndividualInfoEm.stock_name == stock_name).first()

def insert(db: Session, stock: StockIndividualInfoEm):
    db.add(stock)
    db.commit()

def update(db: Session, stock: StockIndividualInfoEm):
    db.query(StockIndividualInfoEm).filter(StockIndividualInfoEm.stock_code == stock.stock_code).update(stock)
    db.commit()