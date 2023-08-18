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
        df_teams = pd.json_normalize(new_data)   
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
                new_data.append(player)
    
        # DataFrame from players data
        df_players = pd.json_normalize(new_data)
        # Get only columns to insert
        df_players = df_players[['id', 'first_name', 'last_name', 'position', 'team.id']]
        df_players = df_players.rename(columns={"team.id": "team_id"})
        # Drop duplicates
        df_players = df_players.drop_duplicates()
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
                new_data.append(game)
    
        # DataFrame from games data
        df_games = pd.json_normalize(new_data)
        # Get only columns to insert
        df_games = df_games[['id', 'date', 'home_team_score', 'period', 'postseason', 'season',
                            'status', 'visitor_team_score', 'home_team.id', 'visitor_team.id']]
        df_games = df_games.rename(columns={"home_team.id": "home_team_id", "visitor_team.id": "visitor_team_id"})
        # Drop duplicates
        df_games = df_games.drop_duplicates()
        # Add column with date of processing
        df_games['etl_date'] = pd.Timestamp.today().strftime('%Y-%m-%d')
        return df_games
    except Exception as err:
        raise

