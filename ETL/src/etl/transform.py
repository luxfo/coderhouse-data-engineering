import pandas as pd
from ..utils import logger

def transform_data(p_data):
    try:
        # Transform data teams
        df_teams = _transform_data_teams(p_data['teams'])
        # Transform data teams
        df_players = _transform_data_players(p_data['players'])
        # Transform data games
        df_games = _transform_data_games(p_data['games'])

        #return {'teams': df_teams}
        return {'teams': df_teams,
                'players': df_players,
                'games': df_games}
    except Exception as err:
        raise

def _transform_data_teams(p_data_teams):
    try:
        logger.info('Transform teams data')
        new_data = []
        # New array with only info from teams
        for teams in p_data_teams:
            for team in teams['data']:
                new_data.append(team)

        # DataFrame from team data
        df_teams = pd.DataFrame(new_data)
        # Drop Duplicates
        df_teams.drop_duplicates()
        # Add column with date of processing
        df_teams['etl_date'] = pd.Timestamp.today().strftime('%Y-%m-%d')
        return df_teams
    except Exception as err:
        raise

def _transform_data_players(p_data_players):
    try:
        logger.info('Transform players data')
        new_data = []
        # New array with only info from players
        for players in p_data_players:
            for player in players['data']:
                # Add new attribute with id of the team
                player['team_id'] = player['team']['id']
                # Delete 'team' attribute becouse contain all team's data
                player.pop('team', None)
                new_data.append(player)
    
        # DataFrame from players data
        df_players = pd.DataFrame(new_data)
        # Drop duplicates
        df_players.drop_duplicates()
        # Add column with date of processing
        df_players['etl_date'] = pd.Timestamp.today().strftime('%Y-%m-%d')
        return df_players
    except Exception as err:
        raise

def _transform_data_games(p_data_games):
    try:
        logger.info('Transform games data')
        new_data = []
        # New array with only info from games
        for games in p_data_games:
            for game in games['data']:
                # Add new attribute with id of the home team
                game['home_team_id'] = game['home_team']['id']
                # Add new attribute with id of the visitor team
                game['visitor_team_id'] = game['visitor_team']['id']
                # Delete 'home_team' attribute becouse contain all home team's data
                game.pop('home_team', None)
                # Delete 'visitor_team' attribute becouse contain all visitor team's data
                game.pop('visitor_team', None)
                new_data.append(game)
    
        # DataFrame from games data
        df_games = pd.DataFrame(new_data)
        # Drop duplicates
        df_games.drop_duplicates()
        # Add column with date of processing
        df_games['etl_date'] = pd.Timestamp.today().strftime('%Y-%m-%d')
        return df_games
    except Exception as err:
        raise

