from fastapi import FastAPI
from app.routers import stocks

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "home page"}

# 包含路由模块
app.include_router(stocks.router)