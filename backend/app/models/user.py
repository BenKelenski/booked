from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

from app.utils.utils import get_timestamp_utc

if TYPE_CHECKING:
    from app.models.collection import Collection


class UserBase(SQLModel):
    name: str = Field(default=None, min_length=1, max_length=40)
    is_active: bool = True
    is_admin: bool = False
    created_ts: datetime = Field(default_factory=datetime.now, nullable=False)


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


class UserUpdate(UserBase):
    name: str | None = Field(default=None, min_length=1, max_length=255)
    password: str | None = Field(default=None, min_length=8, max_length=40)


class User(UserBase, table=True):
    __tablename__ = "users"
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: bytes = Field()

    collections: list["Collection"] = Relationship(back_populates="user")


class UserPublic(UserBase):
    id: int


class UserPublicWithCollections(UserPublic):
    collections: list["CollectionPublic"] = []


from app.models.collection import CollectionPublic  # noqa
