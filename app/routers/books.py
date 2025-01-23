from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/books",
    tags=["books"],
)


class Book(BaseModel):
    id: int | None = None
    title: str
    author: str


DB = [
    Book(title="The Great Gatsby", author="F. Scott Fitzgerald"),
]


@router.get("/")
async def get_all_books() -> list[Book]:
    return DB


@router.post("/")
async def create_book(book: Book) -> Book:
    DB.append(book)
    return book
