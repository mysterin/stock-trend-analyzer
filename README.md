# stock-trend-analyzer
这是一个用于分析股票走势的工具

# 项目架构
fastapi + sqlalchemy + mysql

# 模型生成
```shell
sqlacodegen mysql+pymysql://root:77777777@localhost:3306/stock --table stock_zh_a_spot_em --outfile app/models/stock_zh_a_spot_em.py
```

# 启动服务
```shell
uvicorn app.main:app --port 8080 --reload
```