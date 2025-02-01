from fastapi import HTTPException
from app.models.book import Book, BookCreate, BookPublic, BookPublicWithCollection
from app.repositories.books_repo import BookRepository


class BookService:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    def get_all_books(self) -> list[BookPublic]:
        return self.book_repo.get_all_books()

    def get_book(self, book_id: int) -> BookPublicWithCollection | None:
        book = self.book_repo.get_book(book_id)
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return book

    def create_book(self, book_request: BookCreate) -> BookPublic:
        book = Book.model_validate(book_request)
        self.book_repo.create_book(book)
        return book

    def delete_book(self, book_id: int) -> dict[str, str]:
        book = self.book_repo.get_book(book_id)
        if book is None:
            return {"message": "Book not found"}
        self.book_repo.delete_book(book)
        return {"message": "Book deleted successfully"}
