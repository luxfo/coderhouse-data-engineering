import utils.logger as logger
from .extract import extract_data
from .transform import transform_data
from .load import load_data

def etl():
    try:
        #Extract data
        data = extract_data()
        #Transform data
        dfs = transform_data(data)
        #Load data
        load_data(dfs)
    except Exception as err:
        raise