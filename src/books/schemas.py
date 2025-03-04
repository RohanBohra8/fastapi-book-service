from datetime import date
from pydantic import BaseModel
from typing import Optional

#BaseModel for book
class Book(BaseModel):
    id: Optional[int] = None 
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str

    class Config:
        from_attributes = True # Enables SQLAlchemy compatibility
    
#baseModel to update a book
class BookUpdateModel(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None
    language: Optional[str] = None
