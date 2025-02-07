from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel


from app.utils.utils import get_timestamp_utc

if TYPE_CHECKING:
    from app.models.book import Book, BookPublic
    from app.models.user import User


class CollectionBase(SQLModel):
    name: str
    description: str
    is_private: bool
    created_ts: str = get_timestamp_utc()
    user_id: int = Field(foreign_key="user.id")


class Collection(CollectionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    user: "User" = Relationship(back_populates="collections")
    books: list["Book"] = Relationship(back_populates="collection")


class CollectionPublic(CollectionBase):
    id: int


class CollectionCreate(CollectionBase):
    user_id: int
    name: str
    description: str
    is_private: bool


class CollectionPublicWithBooks(CollectionPublic):
    books: list["BookPublic"] = []


# Fixes pydantic import error
from app.models.book import BookPublic  # noqa
