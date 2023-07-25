import utils.logger as logger
import database as db
import config as cfg
import pandas as pd

def load_data(p_dfs):
    try:
        #Load teams
        _load_teams(p_dfs['teams'])
        #Load players
        _load_players(p_dfs['players'])
        #Load games
        _load_games(p_dfs['games'])
    except Exception as err:
        raise

def _load_teams(p_df):
    try:
        logger.info('Load teams data')
        table = 'teams'
        _to_sql(p_df, table)
    except Exception as err:
        raise

def _load_players(p_df):
    try:
        logger.info('Load players data')
        table = 'players'
        _to_sql(p_df, table)
    except Exception as err:
        raise

def _load_games(p_df):
    try:
        logger.info('Load games data')
        table = 'games'
        _to_sql(p_df, table)
    except Exception as err:
        raise

def _to_sql(p_df, p_table):
    try:
        logger.debug('db connection database')
        #Clean table
        with db.engine.connect() as conn:
            logger.debug('truncate table ' + p_table)
            conn.execute('TRUNCATE TABLE ' + cfg.db_schema + '.' + p_table)
        #Insert data to table
        logger.debug('insert table ' + p_table)
        p_df.to_sql(p_table, db.engine, schema=cfg.db_schema, if_exists='append', index=False, method='multi')
    except Exception as err:
        raise

