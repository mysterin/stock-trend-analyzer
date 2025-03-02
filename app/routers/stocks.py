from fastapi import APIRouter

router = APIRouter()

# 创建物品
@router.get("/stocks")
def stocks():
    return {"message": "stocks page"}
