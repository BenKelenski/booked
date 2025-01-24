from fastapi import APIRouter

from app.models.book import Book

router = APIRouter(
    prefix="/books",
    tags=["books"],
)


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
