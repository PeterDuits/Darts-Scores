from typing import Optional

from src.db import entities
from src.entities.user import commands, service
from src.http.errors import Error, InvalidCredentials
from src.messages import errors
from src.services.auth import AuthProvider
from src.services.utils import hash_password
from src.services.validator import Validator


class UserCreateHandler:
    def __init__(
        self,
        user_service: service.UserService,
        auth: AuthProvider,
        validator: Validator
    ):
        self.user_service = user_service
        self.auth = auth
        self.validator = validator

    def handle(
        self,
        command: commands.UserCreateCommand
    ) -> (Optional[entities.User], Optional[Error]):
        errors = self._validate_command_input(command)
        if len(errors) > 0:
            return None, errors

        user = entities.User(
            first_name=command.first_name,
            last_name=command.last_name,
            email=command.email,
            password=hash_password(command.password)
        )

        user, err = self.user_service.persist(user)
        if err is not None:
            return None, [err]

        return user, None

    def _validate_command_input(
        self,
        command: commands.UserCreateCommand
    ) -> Optional[Error]:
        rules = {
            'first_name':   'required',
            'last_name':    'required',
            'email':        'required|email|unique:user,email',
            'password':     'required|min:8'
        }

        return self.validator.validate(command, rules)


class UserAuthenticationHandler:
    def __init__(
        self,
        user_service: service.UserService,
        auth: AuthProvider,
        validator: Validator
    ):
        self.user_service = user_service
        self.auth = auth
        self.validator = validator

    def handle(
        self,
        command: commands.UserAuthenticationCommand
    ) -> (Optional[str], Optional[Error]):
        user = self.user_service.find_by_email(command.email)
        if user is None:
            return None, [InvalidCredentials(errors.AUTH_ERROR)]

        if self._invalid_password(user.password, command.password):
            return None, [InvalidCredentials(errors.AUTH_ERROR)]

        token = self.auth.generate_token(user.id)

        return token, None

    def _invalid_password(self, user_pass, command_pass):
        return user_pass != hash_password(command_pass, user_pass).decode()


class UserHandler:
    def __init__(
        self,
        user_service: service.UserService,
        auth: AuthProvider,
        validator: Validator
    ):
        self.user_service = user_service
        self.auth = auth
        self.validator = validator

    def handle(
        self,
        command: commands.UserCommand
    ) -> (Optional[entities.User], Optional[Error]):
        if command.id is None:
            return None, [InvalidCredentials(errors.AUTH_ERROR)]

        user = self.user_service.find_by_id(command.id)

        return user, None
