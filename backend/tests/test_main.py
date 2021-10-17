from graphene.test import Client
from raybamusic import crud, schemas
from raybamusic.main import schema


def test_all_songs__empty(db_session):
    client = Client(schema)
    query = """{ songs {name, release} }"""
    executed = client.execute(query, context_value={"session": db_session})
    assert executed == {"data": {"songs": []}}


def test_all_songs__one_song(db_session):
    fake_song = schemas.SongCreate(name="Let me go", release="2021-01-01")
    song_instance = crud.create_song(db=db_session, song=fake_song)

    client = Client(schema)

    query = """{ songs {name, release} }"""
    executed = client.execute(query, context_value={"session": db_session})
    assert executed == {
        "data": {"songs": [{"name": "Let me go", "release": "2021-01-01"}]}
    }


def test_all_songs__more_than_one_song(db_session):
    for name in ("Alameda's blues", "Lobo López"):
        fake_song = schemas.SongCreate(name=name, release="2021-01-01")
        crud.create_song(db=db_session, song=fake_song)

    client = Client(schema)

    query = """{ songs {name, release} }"""
    executed = client.execute(query, context_value={"session": db_session})
    assert executed == {
        "data": {
            "songs": [
                {"name": "Alameda's blues", "release": "2021-01-01"},
                {"name": "Lobo López", "release": "2021-01-01"},
            ]
        }
    }
