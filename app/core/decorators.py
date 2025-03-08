import time
import logging

logger = logging.getLogger(__name__)

'''
各种装饰器
'''

# 记录函数执行时间
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper