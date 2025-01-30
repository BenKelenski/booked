from sqlmodel import Field, SQLModel

from app.utils.utils import get_timestamp_utc


class UserBase(SQLModel):
    name: str
    created_ts: str = get_timestamp_utc()


class User(UserBase, table=True):
    # id: uuid = Field(default_factory=uuid.uuid4, primary_key=True)
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: bytes = Field()


class UserPublic(UserBase):
    id: int


class UserCreate(UserBase):
    password: str
