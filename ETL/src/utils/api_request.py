import time
import requests
from .logger import logger
from ..config import API_RETRY_AFTER

__req_session = requests.Session()

def get_request(p_route, p_params=None):
    try:
        logger.info('Request HTTP GET: ' + p_route + ' - params: ' + str(p_params))
        response = __req_session.get(url=p_route, params=p_params)
        
        if response.status_code != 200:
            # Code 429 represent request limit exceeded
            if response.status_code == 429:
                # Get the time for retry again
                retry_after = response.headers.get("Retry-After") or API_RETRY_AFTER
                # Wait the rate limit for retry request again
                time.sleep(int(retry_after))
                return get_request(p_route=p_route, p_params=p_params)
            else:
                raise response.raise_for_status()
        
        return response.json()
    except Exception as err:
        raise
