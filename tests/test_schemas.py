import uuid
from raybamusic import schemas
from pydantic import ValidationError
import pytest


def test_song_creation():
    song = schemas.Song(id=1, name='fake song')
    assert song.name == 'fake song'


def test_song_creation__wrong_id():
    with pytest.raises(ValidationError) as excinfo:
        schemas.Song(id='should fail', name='fake song')

    assert 'value is not a valid integer' in str(excinfo.value)
