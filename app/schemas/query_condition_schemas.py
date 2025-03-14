from pydantic import BaseModel
from typing import Optional, Dict, List
import datetime

class QueryConditionBase(BaseModel):
    page_name: Optional[str] = None
    condition: Optional[Dict] = None

class QueryCondition(QueryConditionBase):
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True

class QueryConditionList(BaseModel):
    list: List[QueryCondition]
    total: int
    page_num: int
    page_size: int