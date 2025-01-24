from pydantic import BaseModel

from app.utils.utils import getTimestampUTC


class Book(BaseModel):
    id: int | None = None
    title: str
    author: str
    created_ts: str = getTimestampUTC()
