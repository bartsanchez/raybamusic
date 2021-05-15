from graphene.test import Client
from raybamusic import crud, schemas
from raybamusic.database import SessionLocal
from raybamusic.main import schema


def test_all_songs__empty():
    client = Client(schema)
    executed = client.execute('''{ allSongs {edges {node {name} }}}''')
    assert executed == {
        "data": {"allSongs": {"edges": []}}
    }


def test_all_songs__one_song():
    db_session = SessionLocal

    fake_song = schemas.SongCreate(name="Let me go")
    song_instance = crud.create_song(db=db_session, song=fake_song)

    client = Client(schema)

    executed = client.execute('''{ allSongs {edges {node {name} }}}''')
    assert executed == {
        "data": {"allSongs": {"edges": [{"node": {"name": "Let me go"}}]}}
    }

    crud.delete_song(db_session, song_instance)


def test_all_songs__more_than_one_song():
    db_session = SessionLocal

    for name in ("Alameda's blues", "Lobo López"):
        fake_song = schemas.SongCreate(name=name)
        crud.create_song(db=db_session, song=fake_song)

    client = Client(schema)

    executed = client.execute('''{ allSongs {edges {node {name} }}}''')
    assert executed == {
        "data": {"allSongs": {"edges": [
            {"node": {"name": "Alameda's blues"}},
            {"node": {"name": "Lobo López"}}
        ]}}
    }

    crud.delete_all_songs(db_session)
