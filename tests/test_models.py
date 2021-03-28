import uuid
from raybamusic import models
from pydantic import ValidationError
import pytest


def test_song_creation():
    song = models.Song(id=uuid.uuid4(), name='fake song')
    assert song.name == 'fake song'


def test_song_creation__wrong_uuid():
    with pytest.raises(ValidationError) as excinfo:
        models.Song(id='should fail', name='fake song')

    assert 'value is not a valid uuid' in str(excinfo.value)
