import db
import log

logger = log.get_logger()

def test_query_sql():
    sql = 'select * from stock_individual_info_em'
    result = db.query_sql(sql)
    logger.debug(result)
    
def test_execute_sql():
    sql = '''
    INSERT INTO stock_individual_info_em (
    total_market_value,
    circulating_market_value,
    industry,
    listing_date,
    stock_code,
    stock_name,
    total_shares,
    circulating_shares
) VALUES (
    337468917463.220032,
    337466070320.25,
    '银行',
    '1991-04-03',
    '000001',
    '平安银行',
    19405918198.0,
    19405754475.0
);
    '''
    result = db.execute_sql(sql)
    logger.debug(f'Insert result: {result}')