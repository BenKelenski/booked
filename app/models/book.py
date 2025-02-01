from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel

from app.utils.utils import get_timestamp_utc

if TYPE_CHECKING:
    from app.models.collection import Collection, CollectionPublic


class BookBase(SQLModel):
    title: str
    author: str
    created_ts: str = get_timestamp_utc()

    collection_id: int = Field(foreign_key="collection.id")


class Book(BookBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    collection: "Collection" = Relationship(back_populates="books")


class BookPublic(BookBase):
    id: int


class BookCreate(BookBase):
    title: str
    author: str
    collection_id: int


class BookPublicWithCollection(BookPublic):
    collection: Optional["CollectionPublic"] = None


# Fixes pydantic import error
from app.models.collection import CollectionPublic  # noqa
