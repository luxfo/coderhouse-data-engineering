import os
import logging
import logging.handlers as handlers
from config import log_level

logger = logging.getLogger(__name__)
logger.setLevel(log_level)
_file_handler = handlers.TimedRotatingFileHandler('ETL/log/log.log', when='H', backupCount=30)
_formatter    = logging.Formatter('%(asctime)s - %(levelname)s - (%(module)s): %(message)s')
_file_handler.setFormatter(_formatter)
_file_handler.suffix = '%Y%m%d%h'
logger.addHandler(_file_handler)
