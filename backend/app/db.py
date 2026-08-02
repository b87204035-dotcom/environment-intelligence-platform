from contextlib import contextmanager
from psycopg_pool import ConnectionPool
from .config import settings
conninfo = settings.database_url.replace("postgresql+psycopg://", "postgresql://", 1)
pool = ConnectionPool(conninfo, min_size=1, max_size=10, open=False)
@contextmanager
def connection():
    with pool.connection() as conn:
        yield conn
