from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class BookInput(BaseModel):
    title: str
    author: str


class Book(BookInput):
    id: int


books: dict[int, Book] = {
    1: Book(id=1, title="The Little Prince", author="Antoine de Saint-Exupery"),
    2: Book(id=2, title="Frankenstein", author="Mary Shelley"),
}
next_book_id = 3
