from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine

from .config import settings


engine = create_engine(str(settings.SQLMODEL_DATABASE_URI))


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
