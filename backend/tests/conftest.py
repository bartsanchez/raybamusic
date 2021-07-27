import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from raybamusic.models import Base

test_db_url = "sqlite://"


@pytest.fixture(scope="function")
def session_factory():
    engine = create_engine(test_db_url)
    Base.metadata.create_all(engine)
    Base.query = None

    yield sessionmaker(bind=engine)

    engine.dispose()


@pytest.fixture(scope="function")
def db_session(session_factory):
    return session_factory()
