from sqlalchemy import BigInteger, JSON, String, DateTime, text
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base
import datetime

class QueryCondition(Base):
    __tablename__ = 'query_condition'
    __table_args__ = (
        {'comment': '前端查询条件表'}
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment='唯一标识符')
    page_name: Mapped[str] = mapped_column(String(50), comment='页面名称')
    title: Mapped[Optional[str]] = mapped_column(String(100), comment='标题')
    remark: Mapped[Optional[str]] = mapped_column(String(255), comment='说明')
    condition: Mapped[dict] = mapped_column(JSON, comment='查询条件')
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'), comment='创建时间')