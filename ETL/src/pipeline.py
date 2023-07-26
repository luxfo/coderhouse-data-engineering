from .utils import logger
from .etl import extract_data, transform_data, load_data

def pipeline():
    try:
        logger.info('Started')

        # Extract data: Return a new dict with all data
        data = extract_data()
        # Transform data: Return a new dict with dataframes
        dfs = transform_data(data)
        # Load data: Load dataframes to the database
        load_data(dfs)

        logger.info('Finished')
    except Exception as err:
        logger.exception(err)
        raise