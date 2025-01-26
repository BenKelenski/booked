from contextlib import asynccontextmanager
import os
from fastapi import FastAPI

from app.dependencies import create_db_and_tables

from .routers import books, users


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    os.remove("database.db")


app = FastAPI(lifespan=lifespan)


app.include_router(users.router)
app.include_router(books.router)


@app.get("/health")
async def health_check() -> list[str, str]:
    return {"status": "ok"}
