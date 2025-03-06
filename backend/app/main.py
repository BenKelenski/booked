from contextlib import asynccontextmanager
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.dependencies import create_db_and_tables

from .routers import books, users, collections


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    os.remove("database.db")


app = FastAPI(title="booked", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(users.router)
app.include_router(books.router)
app.include_router(collections.router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
