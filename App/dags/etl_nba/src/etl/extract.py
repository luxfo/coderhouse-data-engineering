from ..utils import logger
from ..datasets import get_teams, get_games, get_players

def extract_data() -> dict:
    try:
        # Extract all teams
        data_teams = _extract_teams()
        # Extract all players
        data_players = _extract_players()
        # Extract all games
        data_games = _extract_games()

        #return {'teams': data_teams}
        return {'teams': data_teams, 
                'players': data_players,
                'games': data_games}
    except Exception as err:
        raise

def _extract_teams() -> []:
    try:
        logger.info('Extract all teams')
        data_teams = []
        p = 1

        while True:
            # Get teams from api
            api_response = get_teams({'page': p, 'per_page': 100})
            # Check if key exists and has data
            if 'data' in api_response and len(api_response['data']) > 0:
                data_teams.append(api_response)
                p += 1
            else:
                break
        
        #logger.debug(data_teams)
        return data_teams
    except Exception as err:
        raise

def _extract_players() -> []:
    try:
        logger.info('Extract all players')
        data_players = []
        p = 1

        while True:
            # Get players from api
            api_response = get_players({'page': p, 'per_page': 100})
            # Check if key exists and has data
            if 'data' in api_response and len(api_response['data']) > 0:
                data_players.append(api_response)
                p += 1
            else:
                break

        #logger.debug(data_players)
        return data_players
    except Exception as err:
        raise

def _extract_games() -> []:
    try:
        logger.info('Extract all games')
        data_games = []
        p = 1

        while True:
            # Get games from api
            api_response = get_games({'page': p, 'per_page': 100})
            # Check if key exists and has data
            if 'data' in api_response and len(api_response['data']) > 0:
                data_games.append(api_response)
                p += 1
            else:
                break

        #logger.debug(data_games)
        return data_games
    except Exception as err:
        raise

