from fastapi import Depends
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import akshare as ak
from datetime import datetime
from app.database import SessionLocal
from sqlalchemy.orm import Session
import app.crud.stock_zh_a_spot_em as stock_zh_a_spot_em_crud
from app.models.stock_zh_a_spot_em import StockZhASpotEm
import logging

logger = logging.getLogger(__name__)
db = SessionLocal()

# 每五分钟同步股票实时行情数据
def sync_stock_zh_a_spot_em():
    logging.info("sync_stock_zh_a_spot_em")
    stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
    logging.info(stock_zh_a_spot_em_df)
    stock_zh_a_spot_em_crud.delete_all(db)
    for index, row in stock_zh_a_spot_em_df.iterrows():
        stockXhASpotEm = StockZhASpotEm(
            stock_code=row['代码'],
            stock_name=row['名称'],
            latest_price=row['最新价'],
            change_percent=row['涨跌幅'],
            change_amount=row['涨跌额'],
            volume=row['成交量'],
            turnover=row['成交额'],
            amplitude=row['振幅'],
            high=row['最高'],
            low=row['最低'],
            open=row['今开'],
            close=row['昨收'],
            turnover_rate=row['换手率'],
            pe_ratio=row['市盈率(动态)'],
            pb_ratio=row['市净率'],
            total_market_value=row['总市值'],
            circulating_market_value=row['流通市值'],
            date_time=datetime.now()
        )
        stock_zh_a_spot_em_crud.insert(db, stockXhASpotEm)

scheduler = BackgroundScheduler()
scheduler.add_job(sync_stock_zh_a_spot_em, CronTrigger.from_crontab("* * * * *"))