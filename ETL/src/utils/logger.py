import os
import logging
import logging.handlers as handlers
from config import log_level

_log_path = 'ETL/log/'

if not os.path.exists(_log_path):
    os.makedirs(_log_path)

logger = logging.getLogger(__name__)
logger.setLevel(log_level)
_file_handler = handlers.TimedRotatingFileHandler(_log_path + '/log.log', when='H', backupCount=30)
_formatter    = logging.Formatter('%(asctime)s - %(levelname)s - (%(module)s): %(message)s')
_file_handler.setFormatter(_formatter)
_file_handler.suffix = '%Y%m%d%h'
logger.addHandler(_file_handler)
