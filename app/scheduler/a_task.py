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
import pandas as pd

logger = logging.getLogger(__name__)
db = SessionLocal()

# 每小时同步股票实时行情数据
def sync_stock_zh_a_spot_em():
    stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
    stock_zh_a_spot_em_crud.delete_all(db)
    for index, row in stock_zh_a_spot_em_df.iterrows():
        # logger.info(f'index: {index}, row: {row}')
        stockXhASpotEm = StockZhASpotEm(
            id=row['序号'],
            stock_code=row['代码'],
            stock_name=row['名称'],
            latest_price=row['最新价'] if pd.notna(row['最新价']) else None,
            change_percentage=row['涨跌幅'] if pd.notna(row['涨跌幅']) else None,
            change_amount=row['涨跌额'] if pd.notna(row['涨跌额']) else None,
            volume=row['成交量'] if pd.notna(row['成交量']) else None,
            turnover=row['成交额'] if pd.notna(row['成交额']) else None,
            amplitude=row['振幅'] if pd.notna(row['振幅']) else None,
            highest_price=row['最高'] if pd.notna(row['最高']) else None,
            lowest_price=row['最低'] if pd.notna(row['最低']) else None,
            open_price=row['今开'] if pd.notna(row['今开']) else None,
            previous_close=row['昨收'] if pd.notna(row['昨收']) else None,
            volume_ratio=row['量比'] if pd.notna(row['量比']) else None,
            turnover_rate=row['换手率'] if pd.notna(row['换手率']) else None,
            pe_dynamic=row['市盈率-动态'] if pd.notna(row['市盈率-动态']) else None,
            pb=row['市净率'] if pd.notna(row['市净率']) else None,
            total_market_value=row['总市值'] if pd.notna(row['总市值']) else None,
            circulating_market_value=row['流通市值'] if pd.notna(row['流通市值']) else None,
            increase_speed=row['涨速'] if pd.notna(row['涨速']) else None,
            change_5min=row['5分钟涨跌'] if pd.notna(row['5分钟涨跌']) else None,
            change_60d=row['60日涨跌幅'] if pd.notna(row['60日涨跌幅']) else None,
            change_ytd=row['年初至今涨跌幅'] if pd.notna(row['年初至今涨跌幅']) else None,
            date_time=datetime.now()
        )
        stock_zh_a_spot_em_crud.insert(db, stockXhASpotEm)

scheduler = BackgroundScheduler()
scheduler.add_job(sync_stock_zh_a_spot_em, CronTrigger.from_crontab("0 * * * *"))