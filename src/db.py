import mysql.connector
from mysql.connector import pooling
from config import db_config
import log

logger = log.get_logger()

def init_connection_pool():
    return mysql.connector.pooling.MySQLConnectionPool(pool_name = db_config['pool_name'],
                                                        pool_size = db_config['pool_size'],
                                                        host = db_config['host'],
                                                        user = db_config['user'],
                                                        password = db_config['password'],
                                                        database = db_config['database'])

# 初始化连接池
connection_pool = init_connection_pool()

# 执行插入、更新、删除 sql，在 finally 关闭连接
def execute_sql(sql, args=None):
    logger.info(f"Execute sql: {sql}, args: {args}")
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(sql, args)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

# 执行查询 sql
def query_sql(sql, args=None):
    logger.info(f"Query sql: {sql}, args: {args}")
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(sql, args)
        logger.info(f"Total {cursor.rowcount} records")
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()