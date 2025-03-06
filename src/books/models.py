from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date
from sqlalchemy.orm import declarative_base 
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

# declarative_base() is a function that provides base class for our database models
Base = declarative_base()

class Author(Base):
    __tablename__ = "authors"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    biography = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    books = relationship("Book", back_populates="author", cascade="all, delete")
     
    '''
    books = relationship("Book",
    secondary=Table(
        "author_book",
        Base.metadata,
        Column("author_id", Integer, ForeignKey("authors.id"), primary_key = True),
        Column("id", Integer, ForeignKey("books.author_id"), primary_key = True)
        ),
    back_populates="author", cascade="all, delete")
    '''
    
    def __repr__(self):
        return f"<Author(name={self.name}, id={self.id})>"
    
class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    publisher = Column(String, nullable=False)
    published_date = Column(Date, nullable=False)
    page_count = Column(Integer, nullable=False)
    language = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    author = relationship("Author", back_populates="books")
    
    def __repr__(self):
        return f"<Book(title={self.title}, author_id={self.author_id})>"
    
    
   
# todo 
#     # Association table
# author_book_association = Table(
#     'author_book',
#     Base.metadata,
#     Column('author_id', Integer, ForeignKey('authors.id')),
#     Column('book_id', Integer, ForeignKey('books.id'))
# )
