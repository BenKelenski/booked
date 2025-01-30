from sqlmodel import Field, SQLModel

from app.utils.utils import get_timestamp_utc


class CollectionBase(SQLModel):
    name: str
    user_id: int
    description: str
    is_private: bool
    created_ts: str = get_timestamp_utc()


class Collection(CollectionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class CollectionPublic(CollectionBase):
    id: int
    name: str
    description: str
    is_private: bool
    created_ts: str = get_timestamp_utc()


class CollectionCreate(CollectionBase):
    name: str
    description: str
    is_private: bool
