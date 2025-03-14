from fastapi import Depends
import logging
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import akshare as ak
from datetime import datetime
from app.database import SessionLocal
from sqlalchemy.orm import Session
from app.models.stock_zh_a_spot_em import StockZhASpotEm
from app.models.stock_zh_a_hist import StockZhAHist
from app.models.stock_individual_info_em import StockIndividualInfoEm
from app.crud import crud_stock_individual_info_em as individual_crud, crud_stock_zh_a_hist as hist_crud, crud_stock_zh_a_spot_em as spot_crud
from app.core.decorators import log_execution_time

logger = logging.getLogger(__name__)
db = SessionLocal()

'''
A 股相关定时任务
'''

# 每小时同步股票实时行情数据
@log_execution_time
def sync_stock_zh_a_spot_em_job():
    stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
    for index, row in stock_zh_a_spot_em_df.iterrows():
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
        # 数据存在则更新，不存在则插入
        if spot_crud.get_stock_individual_info_by_code(db, row['代码']):
            spot_crud.update(db, stockXhASpotEm)
        else:
            spot_crud.insert(db, stockXhASpotEm)

# 同步指定股票和开始时间到现在历史行情数据
@log_execution_time
def sync_stock_zh_a_hist_job(stock_code: str, start_date: str):
    '''
    :param stock_code: 股票代码
    :param start_date: 开始日期
    '''
    stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=stock_code, start_date=start_date)
    for index, row in stock_zh_a_hist_df.iterrows():
        stockXhAHist = StockZhAHist(
            stock_code=row['股票代码'],
            trade_date=row['日期'],
            open_price=row['开盘'],
            close_price=row['收盘'],
            highest_price=row['最高'],
            lowest_price=row['最低'],
            volume=row['成交量'],
            turnover=row['成交额'],
            amplitude=row['振幅'],
            change_percentage=row['涨跌幅'],
            change_amount=row['涨跌额'],
            turnover_rate=row['换手率'],
        )
        # 数据存在则更新，不存在则插入
        if hist_crud.get_stock_by_code_and_trade_date(db, stock_code, stockXhAHist.trade_date):
            hist_crud.update(db, stockXhAHist)
        else:
            hist_crud.insert(db, stockXhAHist)

# 同步个股信息
@log_execution_time
def sync_stock_individual_info_em_job(stock_code: str):
    # 接口可能有频率限制
    stock_individual_info_em_df = ak.stock_individual_info_em(symbol=stock_code)
    # 行列转换
    stock_individual_info_em_df = stock_individual_info_em_df.T
    # 取第二行数据
    row = stock_individual_info_em_df.iloc[1]
    logger.info(f'row: {row}')
    stockIndividualInfoEm = StockIndividualInfoEm(
        stock_code=row[0],
        stock_name=row[1],
        total_shares=row[2],
        circulating_shares=row[3],
        total_market_value=row[4],
        circulating_market_value=row[5],
        industry=row[6],
        listing_date=row[7]
    )
    logger.info(f'stockIndividualInfoEm: {stockIndividualInfoEm}')
    if individual_crud.get_stock_individual_info_by_code(db, stock_code=stock_code):
        individual_crud.update(db, stockIndividualInfoEm)
    else:
        individual_crud.insert(db, stockIndividualInfoEm)


scheduler = BackgroundScheduler()
scheduler.add_job(sync_stock_zh_a_spot_em_job, CronTrigger.from_crontab("* * * * *"))
# sync_stock_zh_a_spot_em_job()