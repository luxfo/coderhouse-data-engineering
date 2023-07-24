from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from config import db_driver, db_host, db_port, db_database, db_schema, db_user, db_pass

def get_engine():
    url = URL.create(
            drivername = db_driver,
            host = db_host,
            port = db_port,
            database = db_database,
            username = db_user,
            password = db_pass
        )

    return create_engine(url)

def get_schema():
    return db_schema
