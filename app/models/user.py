from pydantic import BaseModel

from app.utils.utils import getTimestampUTC


class User(BaseModel):
    id: int | None = None
    name: str
    created_ts: str = getTimestampUTC()
