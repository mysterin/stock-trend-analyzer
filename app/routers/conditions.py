from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.query_condition_schemas import QueryCondition, QueryConditionList
from app.crud.crud_query_condition import (
    create_query_condition,
    get_query_condition,
    get_query_conditions,
    update_query_condition,
    delete_query_condition
)
from app.routers.response import ResponseModel, ResponseCode

router = APIRouter()

# 新增或更新查询条件
@router.post("/condition/save", response_model=QueryCondition)
def create_query_condition_endpoint(query_condition: QueryCondition, db: Session = Depends(get_db)):
    # id 是否存在，存在则更新，不存在则新增
    if query_condition.id:
        result = update_query_condition(db=db, query_condition_id=query_condition.id, query_condition=query_condition)
    else:
        result = create_query_condition(db=db, query_condition=query_condition)
    return ResponseModel.from_code(ResponseCode.SUCCESS, data=result)

# 分页查询查询条件
@router.post("/condition/list", response_model=QueryConditionList)
def get_query_condition_list(params: dict, db: Session = Depends(get_db)):
    result = get_query_conditions(db, params)
    return ResponseModel.from_code(ResponseCode.SUCCESS, data=result)

# 删除查询条件
@router.post("/query_conditions/delete", response_model=QueryCondition)
def delete_query_condition_endpoint(query_condition_id: int, db: Session = Depends(get_db)):
    delete_query_condition(db, query_condition_id)
    return ResponseModel.from_code(ResponseCode.SUCCESS)