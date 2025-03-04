from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # 数据库配置
    DATABASE_URL: str  # 数据库 URL
    DATABASE_ECHO: bool = False  # 是否打印 SQL 语句
    DATABASE_POOL_SIZE: int = 5  # 连接池大小
    DATABASE_MAX_OVERFLOW: int = 10  # 超过连接池大小外最多创建的连接
    DATABASE_POOL_RECYCLE: int = 1800  # 连接的最长使用时间（秒）
    DATABASE_POOL_TIMEOUT: int = 30  # 池中没有连接时等待的时间（秒）

    # API 配置
    API_V1_STR: str = "/api/v1"

    # 其他配置
    PROJECT_NAME: str = "stock-trend-analyzer"
    LOGGING_CONFIG: str = "config/logging_config.yaml"  # 日志配置文件
    
    # 从环境变量加载配置
    class Config:
        env_file = "config/.env"  # 指定环境变量文件
        env_file_encoding = "utf-8"  # 指定文件编码

# 创建配置实例
settings = Settings()
print(settings)