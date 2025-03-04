import yaml
from logging.config import dictConfig
from app.core.config import settings

def setup_logging():
    with open(settings.LOGGING_CONFIG, 'r') as f:
        config = yaml.safe_load(f.read())
        dictConfig(config)