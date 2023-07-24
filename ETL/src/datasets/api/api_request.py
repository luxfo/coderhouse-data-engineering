import utils.logger as logger
import requests

def _get_request(p_route, p_params=None):
    try:
        logger.info('Request HTTP GET: ' + p_route + ' - params: ' + str(p_params))
        data = requests.get(p_route, p_params).json()
        return data
    except Exception as err:
        raise
