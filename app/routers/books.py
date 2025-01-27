from fastapi import APIRouter, HTTPException
from sqlmodel import select

from app.models.book import Book, BookCreate, BookPublic
from app.dependencies import SessionDep

router = APIRouter(
    prefix="/books",
    tags=["books"],
)


@router.get("/")
async def get_all_books(session: SessionDep) -> list[BookPublic]:
    return session.exec(select(Book)).all()


@router.get("/{book_id}")
async def get_book(book_id: int, session: SessionDep) -> BookPublic:
    book = session.exec(select(Book).where(Book.id == book_id)).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@router.post("/")
async def create_book(book_request: BookCreate, session: SessionDep) -> BookPublic:
    book = Book.model_validate(book_request)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book
