from app.core.logging_config import setup_logging
# 配置日志
setup_logging()

from app.database import create_all
from fastapi import FastAPI
from app.routers import stocks
from app.scheduler.a_task import scheduler
from contextlib import asynccontextmanager
import logging
from app.middleware import LoggingMiddleware

logger = logging.getLogger(__name__)

# 创建所有表
create_all()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 在应用启动时启动调度器
    scheduler.start()
    yield
    # 在应用关闭时关闭调度器
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

# 添加中间件
app.add_middleware(LoggingMiddleware)
# 包含路由模块
app.include_router(stocks.router)