from .api_request import _get_request
from config import api_url

def get_teams(p_params = None)-> dict:
    try:
        route = api_url + "/teams"
        data = _get_request(route, p_params)
        return data
    except Exception as err:
        raise

def get_players(p_params = None)-> dict:
    try:
        route = api_url + "/players"
        data = _get_request(route, p_params)
        return data
    except Exception as err:
        raise

def get_games(p_params = None)-> dict:
    try:
        route = api_url + "/games"
        data = _get_request(route, p_params)
        return data
    except Exception as err:
        raise

