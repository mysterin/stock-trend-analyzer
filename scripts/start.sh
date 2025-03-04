#!/bin/bash

# 确保脚本在项目根目录下运行
cd "$(dirname "$0")/.."

# 设置环境变量
export DATABASE_URL='mysql+pymysql://root:77777777@localhost:3306/stock'
export LOGGING_CONFIG='config/logging_config.yaml'

# 启动 FastAPI 应用
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload