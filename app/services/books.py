from fastapi import HTTPException
from sqlmodel import select
from app.dependencies import SessionDep
from app.models.book import Book, BookCreate, BookPublic, BookPublicWithCollection


class BookService:
    def __init__(self, session: SessionDep):
        self.session = session

    def get_all_books(self) -> list[BookPublic]:
        return self.session.exec(select(Book)).all()

    def get_book(self, book_id: int) -> BookPublicWithCollection | None:
        book = self.session.exec(select(Book).where(Book.id == book_id)).first()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return book

    def create_book(self, book_request: BookCreate) -> BookPublic:
        book = Book.model_validate(book_request)
        self.session.add(book)
        self.session.commit()
        self.session.refresh(book)
        return book

    def delete_book(self, book_id: int) -> dict[str, str]:
        book = self.session.exec(select(Book).where(Book.id == book_id)).first()
        if book is None:
            return {"message": "Book not found"}
        self.session.delete(book)
        self.session.commit()
        return {"message": "Book deleted successfully"}
