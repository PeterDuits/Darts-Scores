import enum
import json

from src.http import errors
from src.http.utils import map_error


class EnumEncoder(json.JSONEncoder):
    def default(self, o):
        if type(o) is enum.Enum:
            try:
                return str(o)
            except ValueError:
                pass
        return super(EnumEncoder, self).default(o)


error_status_codes = {
    errors.Error: 400,
    errors.BadRequest: 400,
    errors.Unauthorized: 401,
    errors.Forbidden: 403,
    errors.NotFound: 404,
    errors.MethodNotAllowed: 405
}


class Response:

    DEFAULT_ERROR_STATUS_CODE = 400
    DEFAULT_OK_STATUS_CODE = 200

    def __init__(
            self,
            data: any = None,
            errors_: list = None,
            status_code: int = None,
            headers: dict = None
    ):
        self._data = data
        self._errors = errors_ or []
        self._status_code = status_code
        self._headers = headers or self._default_headers()

    def _default_status_code(self) -> int:
        """
        Returns the highest status_code found in mapping, starting at 400 if
        any error is found at all
        """
        status_codes = []
        for error in self._errors:
            error_status_code = error_status_codes.get(
                error.__class__,
                Response.DEFAULT_ERROR_STATUS_CODE
            )
            status_codes.append(error_status_code)

        if len(status_codes) > 0:
            return max(status_codes)

        return Response.DEFAULT_OK_STATUS_CODE

    def body(self):
        if self.ok():
            return self._serialized_data()

        return self._serialized_errors()

    def _serialized_data(self):
        if type(self._data) is str:
            # Skip re-serialization
            return self._data

        if self._data is None:
            return ''

        return json.dumps(self._data, cls=EnumEncoder)

    def _serialized_errors(self) -> str:
        """
        Return serialized error response compatible with jsonapi spec
        Example: {"errors": [{"message": "error"}, {"message": "error"}]}
        """
        response_errors = []
        for err in self._errors:
            error = map_error(err)
            response_errors.append(error)

        return json.dumps(dict(errors=response_errors))

    def status_code(self):
        return self._status_code or self._default_status_code()

    def headers(self):
        return self._headers or self._default_headers()

    @staticmethod
    def _default_headers() -> dict:
        return {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, PUT, PATCH, GET, OPTIONS",
            "Content-Type": "application/json",
        }

    def ok(self):
        return self._errors is None or len(self._errors) == 0
