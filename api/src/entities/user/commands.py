class UserCommand:
    def __init__(
        self,
        id: int
    ):
        self.id = id


class UserCreateCommand:
    def __init__(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class UserAuthenticationCommand:
    def __init__(
        self,
        email: str,
        password: str
    ):
        self.email = email
        self.password = password
