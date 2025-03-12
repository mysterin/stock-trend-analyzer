from typing import Optional

from sqlalchemy import BigInteger, DECIMAL, Date, Index, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from app.models.base import Base
import datetime
import decimal

class StockIndividualInfoEm(Base):
    __tablename__ = 'stock_individual_info_em'
    __table_args__ = (
        Index('idx_stock_code', 'stock_code'),
        {'comment': '存储个股信息的表'}
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, comment='唯一标识符')
    total_market_value: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(20, 4), comment='总市值')
    circulating_market_value: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(20, 4), comment='流通市值')
    industry: Mapped[Optional[str]] = mapped_column(String(50), comment='行业')
    listing_date: Mapped[Optional[datetime.date]] = mapped_column(Date, comment='上市时间')
    stock_code: Mapped[Optional[str]] = mapped_column(String(10), comment='股票代码')
    stock_name: Mapped[Optional[str]] = mapped_column(String(50), comment='股票简称')
    total_shares: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(20, 4), comment='总股本')
    circulating_shares: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(20, 4), comment='流通股')
