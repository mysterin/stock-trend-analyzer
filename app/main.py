from fastapi import FastAPI
from app.routers import stocks
from app.scheduler.task import scheduler
from contextlib import asynccontextmanager

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "home page"}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 在应用启动时启动调度器
    scheduler.start()
    yield
    # 在应用关闭时关闭调度器
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

# 包含路由模块
app.include_router(stocks.router)