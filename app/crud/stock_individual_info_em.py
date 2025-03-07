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
    # stock 转成字典
    update_values = stock.__dict__.copy()
    update_values.pop('id', None)  # 删除字典中的 id 键值对
    update_values.pop('stock_code', None)  # 删除字典中的 stock_code 键值对
    # 删除字典中的 _sa_instance_state 键值对
    update_values.pop('_sa_instance_state', None)
    db.query(StockIndividualInfoEm).filter(StockIndividualInfoEm.stock_code == stock.stock_code).update(update_values, synchronize_session=False)
    db.commit()