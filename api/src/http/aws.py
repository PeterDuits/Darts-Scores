import functools
import json
from typing import Optional, Union

from src import debug
from src.http import responses


class Event:
    """
    Event class that mimics an API gateway request
    https://docs.aws.amazon.com/lambda/latest/dg/eventsources.html#eventsources-api-gateway-request
    """
    def __init__(self, **kwargs):
        self._properties = kwargs
        self._media = None
        self._query_params = None
        self._path_params = None

    def __getitem__(self, item):
        return self.get(item)

    @classmethod
    def from_dict(cls, props: dict):
        return cls(**props)

    @classmethod
    def from_str(cls, input_: str) -> 'Event':
        return cls(**json.loads(input_))

    def get(self, key, default=None) -> Union[str, dict, None]:
        """ Fetch param from event root """
        return self._properties.get(key, default) or default

    def set(self, key: str, value):
        self._properties[key] = value

    def is_json(self) -> bool:
        headers = self.get('headers', dict())
        content_type = headers.get(
            'content-type', headers.get('Content-Type', '')
        )

        return 'application/json' in content_type

    @property
    def path_params(self):
        """Memoized path parameters"""
        if self._path_params is None:
            self._path_params = self.get('pathParameters', {})

        return self._path_params

    @property
    def query_params(self):
        """Memoized query parameters"""
        if self._query_params is None:
            self._query_params = self.get('queryStringParameters', {})

        return self._query_params

    def path(self) -> str:
        """Request path taken from gateway"""
        return self.get('path', '')

    def query_param(self, key: str, default=None) -> Optional[str]:
        """Request query string param taken from gateway"""
        return self.query_params.get(key, default)

    def path_param(self, key: str, default=None) -> Optional[str]:
        """Request path param taken from gateway"""
        return self.path_params.get(key, default)

    def json(self, key: Optional[str] = None, default=None):
        """Memoized JSON decoded body"""
        if self._media is None:
            self._media = self._decode_body()

        if key is None:
            return self._media

        return self._media.get(key, default)

    def _decode_body(self):
        return json.loads(self.get('body', '{}'))


def proxy_response(response: responses.Response):
    return {
        "statusCode": response.status_code(),
        "body": response.body(),
        "headers": response.headers()
    }


def flask_response(response: responses.Response):
    """ Create a flask response """
    from flask import make_response
    response_ = make_response(response.body(), response.status_code())

    for h, v in response.headers().items():
        response_.headers[h] = v

    return response_


def dev_context(request) -> dict:
    return dict()


def dev_response(response):
    from flask import has_app_context
    if has_app_context():
        return flask_response(response)

    return response


def build_event(request) -> dict:
    return dict(
        path=request.path,
        httpMethod=request.method,
        headers=request.headers,
        queryStringParameters=request.args,
        pathParameters=request.view_args,
        body=request.data,
    )


class LambdaProxy:
    """
    Decorator to automatically transform a response to an aws lambda proxy
    response
    """
    def __init__(self, auth, config, debug=False):
        self.auth = auth
        self.environment = config.get('env')
        self.debug = debug

    def __call__(self, fn):
        """ Transforms a response """
        @functools.wraps(fn)
        def decorated(event, context, *args, **kwargs):
            event_ = self._map_event(event)

            if self.debug:
                self._start_trace()

            response = fn(event_, context, *args, **kwargs)

            return self._map_response(response)

        return decorated

    def _map_response(self, response):
        if self.environment == 'dev':
            return dev_response(response)

        return proxy_response(response)

    def _map_event(self, event: Union[dict, Event]):
        if isinstance(event, Event):
            aws_event = event
        else:
            aws_event = Event.from_dict(event)

        self.auth.authorize_event(aws_event)

        return aws_event

    @staticmethod
    def _start_trace():
        debug.trace()


class FlaskApiGatewayEvent:
    def __init__(self, request):
        self.request = request

    def __call__(self, fn):
        """ Converts flask request params to event + context objects """

        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            event = build_event(self.request)
            context = dev_context(self.request)
            return fn(event, context, *args, **kwargs)

        return decorated
