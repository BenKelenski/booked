from sqlmodel import select
from app.dependencies import SessionDep
from app.models.book import Book, BookPublic, BookPublicWithCollection


class BookRepository:
    def __init__(self, session: SessionDep):
        self.session = session

    def get_all_books(self) -> list[BookPublic]:
        return self.session.exec(select(Book)).all()

    def get_book(self, book_id: int) -> BookPublicWithCollection:
        return self.session.exec(select(Book).where(Book.id == book_id)).first()

    def create_book(self, book: Book) -> BookPublic:
        self.session.add(book)
        self.session.commit()
        self.session.refresh(book)
        return book

    def delete_book(self, book: Book):
        self.session.delete(book)
        self.session.commit()
