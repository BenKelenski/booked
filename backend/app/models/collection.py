from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel


if TYPE_CHECKING:
    from app.models.book import Book, BookPublic
    from app.models.user import User


class CollectionBase(SQLModel):
    name: str
    description: str | None = Field(default=None)
    is_private: bool
    created_ts: datetime = Field(default_factory=datetime.now, nullable=False)
    user_id: int = Field(foreign_key="users.id")


class Collection(CollectionBase, table=True):
    __tablename__ = "collections"
    id: int | None = Field(default=None, primary_key=True)

    user: "User" = Relationship(back_populates="collections")
    books: list["Book"] = Relationship(back_populates="collection", cascade_delete=True)


class CollectionPublic(CollectionBase):
    id: int


class CollectionCreate(CollectionBase):
    user_id: int
    name: str
    description: str | None = None
    is_private: bool = False


class CollectionPublicWithBooks(CollectionPublic):
    books: list["BookPublic"] = []


# Fixes pydantic import error
from app.models.book import BookPublic  # noqa
