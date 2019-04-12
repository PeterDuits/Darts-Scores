from functools import wraps

from src.containers import Kernel
from src.http.errors import Unauthorized
from src.messages import errors


def auth_self(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = Kernel.auth()
        account_id = auth.get_account_id()

        if account_id is None:
            raise Unauthorized(errors.UNAUTHORIZED)

        return f(*args, **kwargs)

    return decorated_function
