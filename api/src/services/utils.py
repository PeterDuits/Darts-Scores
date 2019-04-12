import bcrypt


def hash_password(password: str, hashed: str = None) -> str or None:
    try:
        return bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt() if hashed is None else hashed.encode()
        )
    except ValueError:
        return None
