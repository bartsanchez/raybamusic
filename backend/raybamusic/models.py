from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Date

from .database import Base


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    release = Column(Date)
