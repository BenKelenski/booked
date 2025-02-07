from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

from app.utils.utils import get_timestamp_utc

if  TYPE_CHECKING:
    from app.models.collection import Collection


class UserBase(SQLModel):
    name: str
    created_ts: str = get_timestamp_utc()


class User(UserBase, table=True):
    # id: uuid = Field(default_factory=uuid.uuid4, primary_key=True)
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: bytes = Field()

    collections: list["Collection"] = Relationship(back_populates="user")


class UserPublic(UserBase):
    id: int


class UserCreate(UserBase):
    password: str


class UserPublicWithCollections(UserPublic):
    collections: list["CollectionPublic"] = []


from app.models.collection import CollectionPublic #noqa
