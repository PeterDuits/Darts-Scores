from typing import List, Optional

from src.graphql.types import Error as GraphQLError
from src.http.errors import Error


def collect_errors(*errs: List[Optional[Error]]) -> List[Error]:
    """
    Collects errors supplied and returns a list of errors where all falsey
    errors are filtered out.
    Example: (None, Error(), '', Error()) -> [Error(), Error()]
    """
    errors = []
    for e in errs:
        if type(e) is list:
            for err in e:
                if is_error(err):
                    errors.append(err)
        else:
            if is_error(e):
                errors.append(e)

    return errors


def is_error(error):
    return isinstance(error, Error)


def errors_to_graphql_errors(errors: List[Error]) -> List[GraphQLError]:
    _errors = []
    if errors is not None:
        for err in errors:
            converted_error = map_error(err)
            _errors.append(
                GraphQLError(
                    title=converted_error.get('title'),
                    detail=converted_error.get('detail')
                )
            )

    return _errors


def map_error(err):
    if isinstance(err, Error):
        error_title = err.__class__.__name__
    else:
        error_title = str(err)

    if hasattr(err, 'message'):
        error_message = err.message
    else:
        error_message = str(err)

    if hasattr(err, 'meta'):
        error_meta = err.meta
    else:
        error_meta = {}

    return dict(
        title=error_title,
        detail=error_message,
        meta=error_meta
    )
