from typing import Annotated
from fastapi import APIRouter, Depends

from app.models.book import BookCreate, BookPublic
from app.dependencies import SessionDep
from app.services.books import BookService

router = APIRouter(
    prefix="/books",
    tags=["books"],
)


def get_book_service(session: SessionDep):
    return BookService(session)


@router.get("/")
async def get_all_books(
    bookService: Annotated[BookService, Depends(get_book_service)],
) -> list[BookPublic]:
    return bookService.get_all_books()


@router.get("/{book_id}")
async def get_book(
    book_id: int, bookService: Annotated[BookService, Depends(get_book_service)]
) -> BookPublic:
    return bookService.get_book(book_id)


@router.post("/")
async def create_book(
    book_request: BookCreate,
    bookService: Annotated[BookService, Depends(get_book_service)],
) -> BookPublic:
    return bookService.create_book(book_request)


@router.delete(
    "/{book_id}",
)
async def delete_book(
    book_id: int, bookService: Annotated[BookService, Depends(get_book_service)]
) -> dict[str, str]:
    return bookService.delete_book(book_id)
