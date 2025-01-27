from sqlmodel import SQLModel

from app.utils.utils import getTimestampUTC


class CollectionBase(SQLModel):
    name: str
    user_id: int
    description: str
    is_private: bool
    created_ts: str = getTimestampUTC()


class Collection(CollectionBase, table=True):
    id: int


class CollectionPublic(CollectionBase): ...


class CollectionCreate(CollectionBase): ...
