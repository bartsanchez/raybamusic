import uuid
import pydantic


class Song(pydantic.BaseModel):
    id: uuid.UUID
    name: str
