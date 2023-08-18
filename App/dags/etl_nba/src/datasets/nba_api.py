from ..utils import api_request as api_req
from ..config import API_URL

def get_teams(p_params = None)-> dict:
    try:
        route = API_URL + "/teams"
        data = api_req.get_request(route, p_params)
        return data
    except Exception as err:
        raise

def get_players(p_params = None)-> dict:
    try:
        route = API_URL + "/players"
        data = api_req.get_request(route, p_params)
        return data
    except Exception as err:
        raise

def get_games(p_params = None)-> dict:
    try:
        route = API_URL + "/games"
        data = api_req.get_request(route, p_params)
        return data
    except Exception as err:
        raise

