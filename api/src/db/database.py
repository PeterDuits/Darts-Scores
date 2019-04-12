import functools
from typing import Optional

from sqlalchemy.orm import scoped_session, sessionmaker


def create_session_factory(engine):
    return sessionmaker(bind=engine)


def create_scoped_session(factory):
    return scoped_session(factory)


def build_dsn(connection) -> str:
    return '{}://{}:{}@{}:{}/{}'.format(
        connection.get('driver', 'mysql+mysqlconnector'),
        connection.get('username'),
        connection.get('password'),
        connection.get('host'),
        connection.get('port'),
        connection.get('database')
    )


def select_connection(db_config) -> Optional[dict]:
    connection_key = db_config.get('connection')
    connection = db_config.get('connections', {}).get(connection_key)

    if connection is None:
        raise ConnectionError("Connection not found: '{}'".format(connection))

    return connection


class ScopedSession(object):
    def __call__(self, fn):
        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            from src.containers import Kernel
            try:
                return fn(*args, **kwargs)
            finally:
                Kernel.session().remove()
        return decorated
