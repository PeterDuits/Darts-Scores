from typing import Optional

from sqlalchemy import exc

from src.services.auth import AuthProvider
from src.db import entities
from src.http import errors


class Service(object):
    def __init__(self, auth: AuthProvider, session):
        self.auth = auth
        self.session = session

    def persist(self, entity) -> (
        entities.Base, Optional[errors.PersistenceError]
    ):
        try:
            self.session.add(entity)
            self.session.commit()

            return entity, None
        except exc.SQLAlchemyError as e:
            self.session.rollback()

            return entity, errors.PersistenceError(e)
