import logging
import secrets
from datetime import datetime
from typing import Optional, Union

import jwt

from src.http.aws import Event


class AuthProvider:
    def __init__(self, config):
        self._token = None
        self._claims = None
        self._config = config

    def reset(self):
        self._token = None
        self._claims = None

    def set_token(self, token: str):
        self._token = token

    def get_token(self):
        return self._token

    def set_claims(self, claims: dict):
        self._claims = claims

    def get_claims(self) -> dict:
        if self._claims is None and self._token:
            self._claims = self.decode_claims(self._token)

        return self._claims or {}

    def get_claim(self, key, default_value=None) -> any:
        return self.get_claims().get(key, default_value)

    def get_account_id(self) -> Optional[str]:
        return self.get_claim('aid')

    def decode_claims(
        self,
        raw_token: Union[str, bytes, None]
    ) -> Optional[dict]:
        try:
            if type(raw_token) is bytes:
                token_bytes = raw_token
            else:
                token_bytes = raw_token.encode()

            return jwt.decode(
                token_bytes,
                self.token_secret(),
                algorithms=self.jwt_encryption_algorithm(),
                options={'verify_exp': False}
            )
        except jwt.InvalidTokenError as e:
            logging.exception(e)

        return None

    def token_secret(self):
        return self._config.get('secret')

    def jwt_encryption_algorithm(self):
        return self._config.get('jwt_encryption_algorithm')

    def authorize_event(self, event: Event):
        headers = event.get('headers', {})
        auth_header = headers.get('Authorization')
        token = self.token_from_header(auth_header)
        self.reset()
        self.set_token(token)

    def generate_token(self, account_id, expiry=None) -> str:
        claims = {}
        claims.update({
            "aid": account_id,
            "iat": int(datetime.utcnow().timestamp()),
            "jti": secrets.token_urlsafe(16)
        })
        if expiry:
            self.update_claims_exp(claims, expiry)

        return jwt.encode(
            claims,
            self.token_secret(),
            algorithm=self.jwt_encryption_algorithm()
        ).decode()

    @staticmethod
    def token_from_header(header: Optional[str]) -> str:
        if header is None:
            return ''

        segments = header.split(' ')

        if len(segments) < 2:
            return ''

        return segments[1]

    @staticmethod
    def update_claims_exp(claim, seconds_from_now):
        claim.update({
            'exp': int(datetime.utcnow().timestamp() + float(seconds_from_now))
        })
