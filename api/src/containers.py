from typing import Callable

import dependency_injector.containers as containers
import dependency_injector.providers as providers
from sqlalchemy import create_engine

import src.entities.user.handlers as user_handlers
import src.entities.user.service as user_service
from src.services.auth import AuthProvider
from src.config.environment import from_environment
from src.db.database import (build_dsn, create_scoped_session,
                             create_session_factory, select_connection)
from src.services.validator import Validator
from src.http import aws


class Kernel(containers.DeclarativeContainer):
    config = providers.Configuration('core', from_environment())

    connection = providers.Callable(select_connection, config.database)
    dsn = providers.Callable(build_dsn, connection)
    engine = providers.Callable(create_engine, dsn)
    session_factory = providers.Callable(create_session_factory, engine)
    session = providers.Singleton(create_scoped_session, session_factory)

    auth = providers.Singleton(
        AuthProvider,
        config=config
    )


class Services(containers.DeclarativeContainer):
    user_service = providers.Factory(
        user_service.UserService,
        auth=Kernel.auth,
        session=Kernel.session
    )
    validator = providers.Singleton(
        Validator,
        session=Kernel.session
    )


class Handlers(containers.DeclarativeContainer):
    user = providers.Callable(
        user_handlers.UserHandler,
        user_service=Services.user_service,
        auth=Kernel.auth,
        validator=Services.validator
    )
    user_create = providers.Callable(
        user_handlers.UserCreateHandler,
        user_service=Services.user_service,
        auth=Kernel.auth,
        validator=Services.validator
    )
    user_authentication = providers.Callable(
        user_handlers.UserAuthenticationHandler,
        user_service=Services.user_service,
        auth=Kernel.auth,
        validator=Services.validator
    )


class AWS(containers.DeclarativeContainer):
    Event = providers.Factory(
        aws.Event
    )
    LambdaProxy = providers.Factory(
        aws.LambdaProxy,
        auth=Kernel.auth,
        config=Kernel.config
    )
    FlaskApiGatewayEvent = providers.Factory(
        aws.FlaskApiGatewayEvent
    )
