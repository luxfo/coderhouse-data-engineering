import os
import json
from dotenv import load_dotenv

load_dotenv()

_settings = None
with open('ETL/src/settings.json') as f:
    _settings = json.load(f)

api_url         = _settings['api']['base_url']
api_retry_after = _settings['api']['retry_after']
log_level       = _settings['logging']['level']
db_driver       = os.getenv('DB_DRIVER')
db_host         = os.getenv('DB_HOST')
db_port         = os.getenv('DB_PORT')
db_database     = os.getenv('DB_DATABASE')
db_schema       = os.getenv('DB_SCHEMA')
db_user         = os.getenv('DB_USER')
db_pass         = os.getenv('DB_PASS')

