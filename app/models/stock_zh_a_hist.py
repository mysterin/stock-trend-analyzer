from typing import Optional

from sqlalchemy import BigInteger, DECIMAL, Date, Index, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime
import decimal

class Base(DeclarativeBase):
    pass


class StockZhAHist(Base):
    __tablename__ = 'stock_zh_a_hist'
    __table_args__ = (
        Index('idx_date_code', 'trade_date', 'stock_code'),
        {'comment': '股票历史交易数据表'}
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, comment='唯一标识')
    trade_date: Mapped[datetime.date] = mapped_column(Date, comment='交易日期')
    stock_code: Mapped[str] = mapped_column(String(20), comment='股票代码（不带市场标识）')
    open_price: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='开盘价')
    close_price: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='收盘价')
    highest_price: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='最高价')
    lowest_price: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='最低价')
    volume: Mapped[Optional[int]] = mapped_column(BigInteger, comment='成交量（单位：手）')
    turnover: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(20, 2), comment='成交额（单位：元）')
    amplitude: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='振幅（单位：%）')
    change_percentage: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='涨跌幅（单位：%）')
    change_amount: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='涨跌额（单位：元）')
    turnover_rate: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), comment='换手率（单位：%）')
