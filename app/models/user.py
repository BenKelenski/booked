from sqlmodel import Field, SQLModel

from app.utils.utils import getTimestampUTC


class UserBase(SQLModel):
    name: str
    created_ts: str = getTimestampUTC()


class User(UserBase, table=True):
    # id: uuid = Field(default_factory=uuid.uuid4, primary_key=True)
    id: int | None = Field(default=None, primary_key=True)
    password: str


class UserPublic(UserBase):
    id: int


class UserCreate(UserBase):
    password: str
