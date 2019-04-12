import enum
from typing import Type
from uuid import uuid4
from sqlalchemy import CHAR, Column, DateTime, Integer, String, TypeDecorator
import datetime


def uuid():
    return Column(CHAR(36), index=True, default=lambda: str(uuid4()))


def timestamps() -> tuple:
    return (
        Column(DateTime, default=datetime.datetime.utcnow, index=True),
        Column(DateTime, index=True, onupdate=datetime.datetime.utcnow)
    )


class SoftEnum(TypeDecorator):
    impl = String(length=255)

    def __init__(self, base: Type[enum.Enum] = None, *args, **kwargs):
        self.base = base
        super().__init__(*args, **kwargs)

    def process_bind_param(self, value, dialect):
        if value is None:
            return value

        if not hasattr(self.base, getattr(value, 'name', value)):
            raise Exception("Value not part of enum")

        return getattr(value, 'name', value)

    def process_result_value(self, value, dialect):
        if value is None:
            return value

        try:
            return self.base[value]
        except KeyError:
            raise Exception("Value not part of enum")

    def copy(self, **kw):
        return SoftEnum(self.base, **kw)

    def __repr__(self):
        return self.impl.__repr__()
