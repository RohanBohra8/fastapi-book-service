from fastapi import APIRouter, status
from typing import  List,Optional
from src.books.schemas import Book, BookUpdateModel
from fastapi.exceptions import HTTPException

from src.books.book_data import books


###
# i have used APIRouter() imported from fast api instead of FastApi()
# to create and use routers
# is is how the old one looked : book_router = FastAPI()
###

book_router = APIRouter()


# get all the books 
@book_router.get('/books', response_model = List[Book])
async def get_all_books():
    return books

# get a book by a specific book id 
@book_router.get("/book/{book_id}")
async def get_book(book_id:int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Book not found by given id : {book_id}")
   
# to create a book
@book_router.post("/books", status_code = status.HTTP_201_CREATED)
async def create_a_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

# update data in the specific book based on book_id
@book_router.patch("/book/{book_id}")
async def update_book(book_id: int, book_update_data : BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            updated_data = book_update_data.model_dump(exclude_unset=True)  # Exclude fields that were not provided
            book.update(updated_data)  # Merge the new values into the existing book
            
            return book
    
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "No Book found to update")


#need to ask for this error
# to delete a book from books
@book_router.delete("/book/{book_id}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return 
    
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "book not found")
