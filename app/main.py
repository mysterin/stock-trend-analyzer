from app.core.logging_config import setup_logging
# 配置日志
setup_logging()

from fastapi import FastAPI
from app.routers import stocks
from app.scheduler.a_task import scheduler
from contextlib import asynccontextmanager
import logging

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 在应用启动时启动调度器
    scheduler.start()
    yield
    # 在应用关闭时关闭调度器
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def home():
    logger.info("home page")
    return {"message": "home page"}

# 包含路由模块
app.include_router(stocks.router)