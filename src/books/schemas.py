from datetime import date
from pydantic import BaseModel, field_validator
from typing import Optional

# Author schemas 

#common attributes should be in baseClass and the childs should inhert them (data redundancy)

#BaseModel for Author
class Author(BaseModel):
    id: Optional[int] = None 
    name: str
    biography: Optional[str] = None
    birth_date: date

    #custom validator for name
    # @field_validator("name")
    # def valid_name(name):
    #      if(name.isalpha()):
    #          return True
       
    # old method = find new one  
    class Config:
        from_attributes = True # Enables SQLAlchemy compatibility

class CreateAuthor(BaseModel):
    # id: Optional[int] = None 
    name: str
    biography: Optional[str] = None
    birth_date: date

#baseModel to update a book
class AuthorUpdateModel(BaseModel):
    # id: Optional[int] = None
    name: Optional[str] = None
    biography: Optional[str] = None
    birth_date: Optional[date] = None    


#BaseModel for book
class Book(BaseModel):
    id: Optional[int] = None 
    title: str
    author: Author
    publisher: str
    published_date: date
    page_count: int
    language: str

    class Config:
        from_attributes = True # Enables SQLAlchemy compatibility
        
#todo : create time author complete detail not needed
class CreateBook(BaseModel):
    # id: Optional[int] = None 
    title: str
    author_id : int #this is the major change we did 
    publisher: str
    published_date: date
    page_count: int
    language: str
    
#baseModel to update a book
class BookUpdateModel(BaseModel):
    title: Optional[str] = None
    # author: Optional[int] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None
    language: Optional[str] = None
    


    
