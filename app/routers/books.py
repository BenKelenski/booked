from typing import Annotated
from fastapi import APIRouter, Depends

from app.models.book import BookCreate, BookPublic, BookPublicWithCollection
from app.dependencies import SessionDep
from app.repositories.books_repo import BookRepository
from app.services.books import BookService

router = APIRouter(
    prefix="/books",
    tags=["books"],
)


def get_book_service(session: SessionDep):
    return BookService(BookRepository(session))


@router.get("/", response_model=list[BookPublic])
async def get_all_books(
    bookService: Annotated[BookService, Depends(get_book_service)],
) -> list[BookPublic]:
    return bookService.get_all_books()


@router.get("/{book_id}", response_model=BookPublicWithCollection)
async def get_book(
    book_id: int, bookService: Annotated[BookService, Depends(get_book_service)]
) -> BookPublic:
    return bookService.get_book(book_id)


@router.post("/", response_model=BookPublic)
async def create_book(
    book_request: BookCreate,
    bookService: Annotated[BookService, Depends(get_book_service)],
) -> BookPublic:
    return bookService.create_book(book_request)


@router.delete(
    "/{book_id}",
    response_model=dict[str, str],
)
async def delete_book(
    book_id: int, bookService: Annotated[BookService, Depends(get_book_service)]
) -> dict[str, str]:
    return bookService.delete_book(book_id)
