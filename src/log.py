import logging
import logging.config
from config import logging_config

# 读取日志配置
logging.config.dictConfig(logging_config)

def get_logger(name=__name__):
    return logging.getLogger(name)

