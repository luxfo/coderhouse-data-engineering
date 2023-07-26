from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from .config import DB_DRIVER, DB_HOST, DB_PORT, DB_DATABASE, DB_USER, DB_PASS

__url = URL.create(
    drivername = DB_DRIVER,
    host = DB_HOST,
    port = DB_PORT,
    database = DB_DATABASE,
    username = DB_USER,
    password = DB_PASS
)

engine = create_engine(__url)

