from .utils import logger
from .etl import extract_data, transform_data, load_data

def pipeline():
    try:
        logger.info('Started')

        # Extract data - return a new dict with all data
        data = extract_data()
        # Transform data - Return a dict with dataframes
        dfs = transform_data(data)
        # Load data
        load_data(dfs)

        logger.info('Finished')
    except Exception as err:
        logger.exception(err)
        raise