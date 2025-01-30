from sqlmodel import Field, SQLModel

from app.utils.utils import get_timestamp_utc


class BookBase(SQLModel):
    title: str
    author: str
    created_ts: str = get_timestamp_utc()


class Book(BookBase, table=True):
    # id: uuid = Field(default_factory=uuid.uuid4, primary_key=True)
    id: int | None = Field(default=None, primary_key=True)


class BookPublic(BookBase):
    id: int


class BookCreate(BookBase):
    title: str
    author: str
