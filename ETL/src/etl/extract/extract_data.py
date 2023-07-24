import utils.logger as logger
import datasets.api as api

def extract_data() -> dict:
    try:
        #Extract all teams
        data_teams = _extract_all_teams()
        #Extract all players
        data_players = _extract_all_players()
        #Extract all games
        data_games = _extract_all_games()

        #return {'teams': data_teams}
        return {'teams': data_teams, 
                'players': data_players,
                'games': data_games}
    except Exception as err:
        raise

def _extract_all_teams() -> []:
    try:
        logger.debug('Extract all teams')
        data_teams = []
        p = 1

        while True:
            #Get teams from api
            api_response = api.get_teams({'page': p, 'per_page': 100})
            #Check if key exists and has data
            if 'data' in api_response and len(api_response['data']) > 0:
                data_teams.append(api_response)
                p += 1
            else:
                break
        
        #logger.debug(data_teams)
        return data_teams
    except Exception as err:
        raise

def _extract_all_players() -> []:
    try:
        logger.debug('Extract all players')
        data_players = []
        p = 1

        while True:
            #Get players from api
            api_response = api.get_players({'page': p, 'per_page': 100})
            #Check if key exists and has data
            if 'data' in api_response and len(api_response['data']) > 0:
                data_players.append(api_response)
                p += 1
            else:
                break

        #logger.debug(data_players)
        return data_players
    except Exception as err:
        raise

def _extract_all_games() -> []:
    try:
        logger.debug('Extract all games')
        data_games = []
        p = 1

        while True:
            #Get games from api
            api_response = api.get_games({'page': p, 'per_page': 100})
            #Check if key exists and has data
            if 'data' in api_response and len(api_response['data']) > 0:
                data_games.append(api_response)
                p += 1
            else:
                break

        #logger.debug(data_games)
        return data_games
    except Exception as err:
        raise

