from sqlalchemy.orm import Session

from . import models, schemas


def get_song(db: Session, song_id: int):
    return db.query(models.Song).filter(models.Song.id == song_id).first()


def get_all_songs(db: Session):
    return db.query(models.Song).all()


def create_song(db: Session, song: schemas.SongCreate):
    db_song = models.Song(**song.dict())
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song


def delete_song(db: Session, song: models.Song):
    db.delete(song)
    db.commit()


def delete_all_songs(db: Session):
    for song in get_all_songs(db):
        delete_song(db, song)
