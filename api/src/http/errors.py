from src.messages import errors


class Error(Exception):
    def __str__(self):
        if Exception.__str__(self) == '':
            return self.__class__.__name__
        return Exception.__str__(self)


class BadRequest(Error):
    pass


class Unauthorized(Error):
    pass


class Forbidden(Error):
    pass


class NotFound(Error):
    pass


class MethodNotAllowed(Error):
    pass


class PersistenceError(Error):
    pass


class NotUniqueError(Error):
    pass


class EmailAlreadyExists(Error):
    def __init__(self, email, *args, **kwargs):
        Error.__init__(
            self,
            "Email '{}' already exists".format(email),
            *args,
            **kwargs
        )


class InvalidCredentials(Error):
    pass
