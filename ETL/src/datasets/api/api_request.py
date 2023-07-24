import requests

def _get_request(p_route, p_params=None):
    try:
        data = requests.get(p_route, p_params).json()
        return data
    except Exception as err:
        raise
