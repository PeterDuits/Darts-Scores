from typing import Callable, Iterator, Optional

from src.db.entities import User
from src.services.service import Service


class UserService(Service):
    def __init__(self, *args, **kwargs):
        Service.__init__(self, *args, **kwargs)

    def find_by_email(self, email) -> Optional[User]:
        return self.session.query(User) \
            .filter_by(email=email) \
            .first()

    def find_by_id(self, id) -> Optional[User]:
        return self.session.query(User) \
            .filter_by(id=id) \
            .first()
