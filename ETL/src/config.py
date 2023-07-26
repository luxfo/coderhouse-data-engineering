import os
import json
from dotenv import load_dotenv

load_dotenv()

_settings = None
with open('ETL/settings.json') as f:
    _settings = json.load(f)

API_URL         = _settings['api']['base_url']
API_RETRY_AFTER = _settings['api']['retry_after']
LOG_LEVEL       = _settings['logging']['level']
DB_DRIVER       = os.getenv('DB_DRIVER')
DB_HOST         = os.getenv('DB_HOST')
DB_PORT         = os.getenv('DB_PORT')
DB_DATABASE     = os.getenv('DB_DATABASE')
DB_SCHEMA       = os.getenv('DB_SCHEMA')
DB_USER         = os.getenv('DB_USER')
DB_PASS         = os.getenv('DB_PASS')


