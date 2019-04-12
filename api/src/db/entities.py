from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from src.db import utils


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_id = utils.uuid()
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at, updated_at = utils.timestamps()
