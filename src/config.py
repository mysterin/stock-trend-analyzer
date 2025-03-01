import yaml

# file_path = 'config/config.yaml'
def load_config(file_path = 'config/config.yaml'):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

config = load_config()

# 连接池配置
db_config = config['db']
# 日志配置
logging_config = config['logging']