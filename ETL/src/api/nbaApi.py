from .apiRequest import getRequest
from config import api_config

BASE_URL = api_config['base_url'] 

def extractTeams()-> dict:
    route = BASE_URL + "/teams"
    data = getRequest(route)
    return data

def extractPlayers()-> dict:
    route = BASE_URL + "/players"
    data = getRequest(route)
    return data

def extractGames()-> dict:
    route = BASE_URL + "/games"
    data = getRequest(route)
    return data
