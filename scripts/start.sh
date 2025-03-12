#!/bin/bash

# 确保脚本在项目根目录下运行
cd "$(dirname "$0")/.."

# 设置环境变量
export DATABASE_URL='mysql+pymysql://root:77777777@localhost:3306/stock'
export LOGGING_CONFIG='config/logging_config.yaml'

# 函数：启动 FastAPI 应用
start_app() {
    echo "启动 FastAPI 应用..."
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
}

# 函数：启动前端应用
start_frontend() {
    echo "启动前端应用..."
    cd stock-frontend
    npm install
    npm run serve
}

# 函数：显示帮助信息
show_help() {
    echo "使用方法: $0 [选项]"
    echo "选项:"
    echo "  --app        启动 FastAPI 应用"
    echo "  --frontend   启动前端应用"
    echo "  --all        同时启动 FastAPI 应用和前端应用"
}

# 如果没有传递参数，显示帮助信息
if [ "$#" -eq 0 ]; then
    show_help
    exit 1
fi

# 解析传递的参数
while [ "$#" -gt 0 ]; do
    case $1 in
        --app) start_app ;;
        --frontend) start_frontend ;;
        --all) start_app & start_frontend & ;;
        *) echo "未知参数: $1"; show_help; exit 1 ;;
    esac
    shift
done