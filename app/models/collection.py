from pydantic import BaseModel

from app.utils.utils import getTimestampUTC


class Collection(BaseModel):
    id: int | None = None
    name: str
    description: str
    created_ts: str = getTimestampUTC()
