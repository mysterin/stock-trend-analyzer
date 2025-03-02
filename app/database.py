from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, 
                       echo=settings.DATABASE_ECHO, 
                       pool_size=settings.DATABASE_POOL_SIZE,
                       max_overflow=settings.DATABASE_MAX_OVERFLOW, 
                       pool_recycle=settings.DATABASE_POOL_RECYCLE,
                       pool_timeout=settings.DATABASE_POOL_TIMEOUT)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()