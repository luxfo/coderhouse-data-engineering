import requests

def getRequest(pRoute, pParams=None):
    data = requests.get(pRoute, pParams).json()
    return data
