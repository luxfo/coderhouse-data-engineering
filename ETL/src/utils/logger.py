import os
import logging
import logging.handlers as handlers
from ..config import LOG_LEVEL

_log_path = 'ETL/log/'

if not os.path.exists(_log_path):
    os.makedirs(_log_path)

logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
_file_handler = handlers.TimedRotatingFileHandler(_log_path + '/log.log', when='H', backupCount=30)
_formatter    = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
_file_handler.setFormatter(_formatter)
_file_handler.suffix = '%Y%m%d%H'
logger.addHandler(_file_handler)
