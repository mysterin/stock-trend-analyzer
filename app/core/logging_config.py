import yaml
from logging.config import dictConfig
from app.core.config import settings

# 配置日志
def setup_logging():
    with open(settings.LOGGING_CONFIG, 'r') as f:
        config = yaml.safe_load(f.read())
        print(f'Load logging config: {config}')
        dictConfig(config)