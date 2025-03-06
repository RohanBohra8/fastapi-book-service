from datetime import date
from pydantic import BaseModel, field_validator
from typing import Optional

#common attributes should be in baseClass and the childs should inhert them (data redundancy)

#BaseModel for Author
class Author(BaseModel):
    id: Optional[int] = None 
    name: str
    biography: Optional[str] = None
    birth_date: date

    class Config:
        from_attributes = True # Enables SQLAlchemy compatibility

class CreateAuthor(BaseModel):
    name: str
    biography: Optional[str] = None
    birth_date: date

#baseModel to update a book
class AuthorUpdateModel(BaseModel):
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
        from_attributes = True 
        
#todo : create time author complete detail not needed
class CreateBook(BaseModel):
    title: str
    author_id : int 
    publisher: str
    published_date: date
    page_count: int
    language: str
    
#baseModel to update a book
class BookUpdateModel(BaseModel):
    title: Optional[str] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None
    language: Optional[str] = None
    

#TOODOO
#custom validator for name
    # @field_validator("name")
    # def valid_name(name):
    #      if(name.isalpha()):
    #          return True
       
    # old method = find new one  
    
