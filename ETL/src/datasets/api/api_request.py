import utils.logger as logger
import config as cfg
import time
import requests

def _get_request(p_route, p_params=None):
    try:
        logger.info('Request HTTP GET: ' + p_route + ' - params: ' + str(p_params))
        response = requests.get(url=p_route, params=p_params)

        return response.json()
    except Exception as err:
        logger.error(err, exc_info=True)
