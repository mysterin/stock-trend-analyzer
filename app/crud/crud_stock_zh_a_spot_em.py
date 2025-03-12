from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from app.models.stock_zh_a_spot_em import StockZhASpotEm
from app.schemas.stock_zh_a_spot_schemas import StockZhASpotEmList, StockZhASpotEm as StockZhASpotEmSchema

def get_stock_individual_info_by_code(db: Session, stock_code: str):
    return db.query(StockZhASpotEm).filter(StockZhASpotEm.stock_code == stock_code).first()

def delete_all(db: Session):
    db.query(StockZhASpotEm).delete()
    db.commit()

def insert(db: Session, stock: StockZhASpotEm):
    db.add(stock)
    db.commit()

def update(db: Session, stock: StockZhASpotEm):
    update_values = stock.__dict__.copy()
    update_values.pop('id', None)
    update_values.pop('stock_code', None)
    update_values.pop('_sa_instance_state', None)
    db.query(StockZhASpotEm).filter(StockZhASpotEm.stock_code == stock.stock_code).update(update_values, synchronize_session=False)
    db.commit()

# 分页查询股票实时行情数据
def get_stock_spot_list(db: Session, params: dict):
    page_num = params.get('page_num', 1)
    page_size = params.get('page_size', 10)
    order_by = params.get('order_by', 'stock_code')  # 默认按 stock_code 排序
    order_type = params.get('order_type', 'asc')  # 默认升序排序

    offset = (page_num - 1) * page_size

    # 根据 order_type 设置排序方式
    if order_type == 'desc':
        order = desc(getattr(StockZhASpotEm, order_by))
    else:
        order = asc(getattr(StockZhASpotEm, order_by))

    query = db.query(StockZhASpotEm)

    # 动态添加查询条件
    if 'stock_code' in params and params['stock_code'] is not None:
        query = query.filter(StockZhASpotEm.stock_code == params['stock_code'])
    if 'min_volume_ratio' in params and params['min_volume_ratio'] is not None:
        query = query.filter(StockZhASpotEm.volume_ratio >= params['min_volume_ratio'])
    if 'max_volume_ratio' in params and params['max_volume_ratio'] is not None:
        query = query.filter(StockZhASpotEm.volume_ratio <= params['max_volume_ratio'])
    if 'min_latest_price' in params and params['min_latest_price'] is not None:
        query = query.filter(StockZhASpotEm.latest_price >= params['min_latest_price'])
    if 'max_latest_price' in params and params['max_latest_price'] is not None:
        query = query.filter(StockZhASpotEm.latest_price <= params['max_latest_price'])
    if 'min_change_percentage' in params and params['min_change_percentage'] is not None:
        query = query.filter(StockZhASpotEm.change_percentage >= params['min_change_percentage'])
    if 'max_change_percentage' in params and params['max_change_percentage'] is not None:
        query = query.filter(StockZhASpotEm.change_percentage <= params['max_change_percentage'])
    if 'min_change_amount' in params and params['min_change_amount'] is not None:
        query = query.filter(StockZhASpotEm.change_amount >= params['min_change_amount'])
    if 'max_change_amount' in params and params['max_change_amount'] is not None:
        query = query.filter(StockZhASpotEm.change_amount <= params['max_change_amount'])
    if 'min_volume' in params and params['min_volume'] is not None:
        query = query.filter(StockZhASpotEm.volume >= params['min_volume'])
    if 'max_volume' in params and params['max_volume'] is not None:
        query = query.filter(StockZhASpotEm.volume <= params['max_volume'])
    if 'min_amplitude' in params and params['min_amplitude'] is not None:
        query = query.filter(StockZhASpotEm.amplitude >= params['min_amplitude'])
    if 'max_amplitude' in params and params['max_amplitude'] is not None:
        query = query.filter(StockZhASpotEm.amplitude <= params['max_amplitude'])
    if 'min_highest_price' in params and params['min_highest_price'] is not None:
        query = query.filter(StockZhASpotEm.highest_price >= params['min_highest_price'])
    if 'max_highest_price' in params and params['max_highest_price'] is not None:
        query = query.filter(StockZhASpotEm.highest_price <= params['max_highest_price'])
    if 'min_lowest_price' in params and params['min_lowest_price'] is not None:
        query = query.filter(StockZhASpotEm.lowest_price >= params['min_lowest_price'])
    if 'max_lowest_price' in params and params['max_lowest_price'] is not None:
        query = query.filter(StockZhASpotEm.lowest_price <= params['max_lowest_price'])
    if 'min_turnover_rate' in params and params['min_turnover_rate'] is not None:
        query = query.filter(StockZhASpotEm.turnover_rate >= params['min_turnover_rate'])
    if 'max_turnover_rate' in params and params['max_turnover_rate'] is not None:
        query = query.filter(StockZhASpotEm.turnover_rate <= params['max_turnover_rate'])
    if 'min_change_5min' in params and params['min_change_5min'] is not None:
        query = query.filter(StockZhASpotEm.change_5min >= params['min_change_5min'])
    if 'max_change_5min' in params and params['max_change_5min'] is not None:
        query = query.filter(StockZhASpotEm.change_5min <= params['max_change_5min'])
    if 'date_time_range' in params and params['date_time_range'] and len(params['date_time_range']) == 2:
        start_date, end_date = params['date_time_range']
        query = query.filter(StockZhASpotEm.date_time >= start_date, StockZhASpotEm.date_time <= end_date)
    # 可以根据需要添加更多的查询条件

    stock_list = query.order_by(order).offset(offset).limit(page_size).all()
    total = query.count()

    # 将 SQLAlchemy 模型对象转换为 Pydantic 模型
    stock_list_pydantic = [StockZhASpotEmSchema.from_orm(stock) for stock in stock_list]

    return StockZhASpotEmList(
        list=stock_list_pydantic,
        total=total,
        page_num=page_num,
        page_size=page_size
    )