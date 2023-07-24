import utils.logger as logger
import pandas as pd

def transform_data(p_data):
    try:
        #Transform data teams
        df_teams = _transform_data_teams(p_data['teams'])
        #Transform data teams
        df_players = _transform_data_players(p_data['players'])
        #Transform data games
        df_games = _transform_data_games(p_data['games'])

        #return {'teams': df_teams}
        return {'teams': df_teams,
                'players': df_players,
                'games': df_games}
    except Exception as err:
        raise

def _transform_data_teams(p_data_teams):
    try:
        logger.debug('Transform teams data')
        new_data = []
        #New array with only info from teams
        for teams in p_data_teams:
            for team in teams['data']:
                new_data.append(team)

        #DataFrame from team data
        df_teams = pd.DataFrame(new_data)
        df_teams.drop_duplicates()
        return df_teams
    except Exception as err:
        raise

def _transform_data_players(p_data_players):
    try:
        logger.debug('Transform players data')
        new_data = []
        #New array with only info from players
        for players in p_data_players:
            for player in players['data']:
                player['team_id'] = player['team']['id']
                player.pop('team', None)
                new_data.append(player)
    
        df_players = pd.DataFrame(new_data)
        df_players.drop_duplicates()
        return df_players
    except Exception as err:
        raise

def _transform_data_games(p_data_games):
    try:
        logger.debug('Transform games data')
        new_data = []
        #New array with only info from games
        for games in p_data_games:
            for game in games['data']:
                game['home_team_id'] = game['home_team']['id']
                game['visitor_team_id'] = game['visitor_team']['id']
                game.pop('home_team', None)
                game.pop('visitor_team', None)
                new_data.append(game)
    
        df_games = pd.DataFrame(new_data)
        df_games.drop_duplicates()
        return df_games
    except Exception as err:
        raise

