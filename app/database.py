import logging
import os
import importlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base
from app.core.config import settings

logger = logging.getLogger(__name__)

# 创建数据库引擎
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

def import_all_models():
    models_dir = os.path.join(os.path.dirname(__file__), 'models')
    for filename in os.listdir(models_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f"app.models.{filename[:-3]}"
            importlib.import_module(module_name)

# 根据 models 类创建数据库表
def create_all():
    logger.info("Importing all models")
    import_all_models()
    logger.info("Creating all tables")
    Base.metadata.create_all(bind=engine)
    logger.info("All tables created")