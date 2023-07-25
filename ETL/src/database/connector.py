from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import config as cfg

_url = URL.create(
            drivername = cfg.db_driver,
            host = cfg.db_host,
            port = cfg.db_port,
            database = cfg.db_database,
            username = cfg.db_user,
            password = cfg.db_pass
        )

engine = create_engine(_url)

