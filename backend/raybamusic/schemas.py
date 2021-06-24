import pydantic

from datetime import date


class SongBase(pydantic.BaseModel):
    name: str
    release: date


class Song(SongBase):
    id: int

    class Config:
        orm_mode = True


class SongCreate(SongBase):
    pass
