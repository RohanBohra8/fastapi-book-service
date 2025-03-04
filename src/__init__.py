from fastapi import FastAPI
from src.books.routes import book_router

#app version defined
version = "v1"

#creating fastapi instance having these properties
app = FastAPI(
    title = "Bookify",
    description = "Restful API for book serivice",
    version = version
)

# include the router we created in the rotues.py file so that the app can use it
# book related endpoints can be access by goin to : http://localhost:8000/api/v1/books
app.include_router(book_router, prefix = f"/api/{version}/books", tags = ["books"])


