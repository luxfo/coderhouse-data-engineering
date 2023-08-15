import sys
import os
import json
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)

_settings = None
with open(ROOT_DIR + '/settings.json') as f:
    _settings = json.load(f)

API_URL         = _settings['api']['base_url']
API_RETRY_AFTER = _settings['api']['retry_after']
LOG_LEVEL       = _settings['logging']['level']
DB_DRIVER       = str(os.getenv('DB_DRIVER'))
DB_HOST         = str(os.getenv('DB_HOST'))
DB_PORT         = int(os.getenv('DB_PORT'))
DB_DATABASE     = str(os.getenv('DB_DATABASE'))
DB_SCHEMA       = str(os.getenv('DB_SCHEMA'))
DB_USER         = str(os.getenv('DB_USER'))
DB_PASS         = str(os.getenv('DB_PASS'))
