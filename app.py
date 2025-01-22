from typing import Dict, List
from uuid import uuid4 as uuid
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

DB = []


class Book(BaseModel):
    id: int | None = None
    title: str
    author: str

@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "ok"}

@app.get("/books/")
async def get_all_books() -> List[Book]:
    return DB

@app.post("/books/")
async def create_book(book: Book) -> Book:
    DB.append(book)
    return book