from typing import Optional

from sqlalchemy import BigInteger, DECIMAL, DateTime, Index, String, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime
import decimal

class Base(DeclarativeBase):
    pass


class StockZhASpotEm(Base):
    __tablename__ = 'stock_zh_a_spot_em'
    __table_args__ = (
        Index('idx_date_time', 'date_time'),
        Index('idx_stock_code', 'stock_code'),
        {'comment': '股票实时行情数据表'}
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, comment='唯一标识符')
    stock_code: Mapped[str] = mapped_column(String(10), comment='股票代码')
    date_time: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'), comment='数据时间')
    stock_name: Mapped[Optional[str]] = mapped_column(String(50), comment='股票简称')
    latest_price: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='最新价')
    change_percentage: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='涨跌幅（单位：%）')
    change_amount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='涨跌额（单位：元）')
    volume: Mapped[Optional[int]] = mapped_column(BigInteger, comment='成交量（单位：手）')
    turnover: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(20, 2), comment='成交额（单位：元）')
    amplitude: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='振幅（单位：%）')
    highest_price: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='最高价')
    lowest_price: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='最低价')
    open_price: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='今开价')
    previous_close: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='昨收价')
    volume_ratio: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='量比')
    turnover_rate: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='换手率（单位：%）')
    pe_dynamic: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='市盈率-动态')
    pb: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='市净率')
    total_market_value: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(20, 4), comment='总市值（单位：元）')
    circulating_market_value: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(20, 4), comment='流通市值（单位：元）')
    increase_speed: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='涨速')
    change_5min: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='5分钟涨跌（单位：%）')
    change_60d: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='60日涨跌幅（单位：%）')
    change_ytd: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='年初至今涨跌幅（单位：%）')
