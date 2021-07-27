import uuid
from raybamusic import schemas
from pydantic import ValidationError
import pytest

from datetime import date


def test_song_creation():
    song = schemas.Song(id=1, name="fake song", release=date.today())
    assert song.name == "fake song"
    assert song.release == date.today()


def test_song_creation__wrong_id():
    with pytest.raises(ValidationError) as excinfo:
        schemas.Song(id="should fail", name="fake song", release=date.today())

    assert "value is not a valid integer" in str(excinfo.value)
