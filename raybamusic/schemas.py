import pydantic


class SongBase(pydantic.BaseModel):
    name: str


class Song(SongBase):
    id: int

    class Config:
        orm_mode = True


class SongCreate(SongBase):
    pass
