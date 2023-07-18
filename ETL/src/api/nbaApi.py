from .apiRequest import getRequest
from config import api_config

BASE_URL = api_config['base_url'] 

def extractTeams(pParams = None)-> dict:
    route = BASE_URL + "/teams"
    data = getRequest(route, pParams)
    return data

def extractPlayers(pParams = None)-> dict:
    route = BASE_URL + "/players"
    data = getRequest(route, pParams)
    return data

def extractGames(pParams = None)-> dict:
    route = BASE_URL + "/games"
    data = getRequest(route, pParams)
    return data
