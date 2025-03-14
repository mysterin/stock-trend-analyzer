from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from app.models.query_condition import QueryCondition
from app.schemas.query_condition_schemas import QueryConditionList, QueryCondition as QueryConditionSchema

def create_query_condition(db: Session, query_condition: QueryCondition) -> QueryConditionSchema:
    db_query_condition = QueryCondition(**query_condition.dict())
    db.add(db_query_condition)
    db.commit()
    db.refresh(db_query_condition)
    return QueryConditionSchema.from_orm(db_query_condition)

def get_query_condition(db: Session, query_condition_id: int) -> QueryConditionSchema:
    db_query_condition = db.query(QueryCondition).filter(QueryCondition.id == query_condition_id).first()
    if db_query_condition is None:
        return None
    return QueryConditionSchema.from_orm(db_query_condition)

def get_query_conditions(db: Session, params: dict) -> QueryConditionList:
    page_num = params.get('page_num', 1)
    page_size = params.get('page_size', 10)
    order_by = params.get('order_by', 'id')  # 默认按 id 排序
    order_type = params.get('order_type', 'asc')  # 默认升序排序

    offset = (page_num - 1) * page_size

    # 根据 order_type 设置排序方式
    if order_type == 'desc':
        order = desc(getattr(QueryCondition, order_by))
    else:
        order = asc(getattr(QueryCondition, order_by))

    total = db.query(QueryCondition).count()
    query_conditions = db.query(QueryCondition).order_by(order).offset(offset).limit(page_size).all()
    query_conditions_list = [QueryConditionSchema.from_orm(query_condition) for query_condition in query_conditions]
    return QueryConditionList(
        list=query_conditions_list,
        total=total,
        page_num=page_num,
        page_size=page_size
    )

def update_query_condition(db: Session, query_condition: QueryCondition) -> QueryConditionSchema:
    db_query_condition = db.query(QueryCondition).filter(QueryCondition.id == query_condition.id).first()
    if db_query_condition:
        for key, value in query_condition.dict(exclude_unset=True).items():
            setattr(db_query_condition, key, value)
        db.commit()
        db.refresh(db_query_condition)
    return QueryConditionSchema.from_orm(db_query_condition)

def delete_query_condition(db: Session, query_condition_id: int) -> QueryConditionSchema:
    db_query_condition = db.query(QueryCondition).filter(QueryCondition.id == query_condition_id).first()
    if db_query_condition:
        db.delete(db_query_condition)
        db.commit()
    return QueryConditionSchema.from_orm(db_query_condition)