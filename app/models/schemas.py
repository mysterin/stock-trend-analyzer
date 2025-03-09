from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from decimal import Decimal

class StockZhASpotEmBase(BaseModel):
    stock_code: str
    date_time: datetime
    stock_name: str
    latest_price: Optional[Decimal] = None
    change_percentage: Optional[Decimal] = None
    change_amount: Optional[Decimal] = None
    volume: Optional[int] = None
    turnover: Optional[Decimal] = None
    amplitude: Optional[Decimal] = None
    highest_price: Optional[Decimal] = None
    lowest_price: Optional[Decimal] = None
    open_price: Optional[Decimal] = None
    previous_close: Optional[Decimal] = None
    volume_ratio: Optional[Decimal] = None
    turnover_rate: Optional[Decimal] = None
    pe_dynamic: Optional[Decimal] = None
    pb: Optional[Decimal] = None
    total_market_value: Optional[Decimal] = None
    circulating_market_value: Optional[Decimal] = None
    increase_speed: Optional[Decimal] = None
    change_5min: Optional[Decimal] = None
    change_60d: Optional[Decimal] = None
    change_ytd: Optional[Decimal] = None

class StockZhASpotEm(StockZhASpotEmBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True

class StockZhASpotEmList(BaseModel):
    list: List[StockZhASpotEm]
    total: int
    page_num: int
    page_size: int