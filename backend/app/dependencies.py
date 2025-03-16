from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

db_connection_url = f"postgresql://postgres:password@localhost:5432/test_db"

connect_args = {"check_same_thread": False}
engine = create_engine(db_connection_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
