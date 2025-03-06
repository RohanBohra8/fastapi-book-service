from fastapi import FastAPI
from src.books.routes import book_router
from src.books.author_routes import author_router

# from src.database import init_db
from contextlib import contextmanager

#app version defined
version = "v1"

# NEED EXPLAINATION
# Using lifespan instead of @app.on_event
# @contextmanager
# def lifespan(app: FastAPI):
#     # init_db()  # Initialize the database
#     print("Server is starting...")
#     yield
#     # Continue running the application
#     print("server is stopping")

#creating fastapi instance having these properties
app = FastAPI(
    title = "Bookify",
    description = "Restful API for book serivice",
    version = version,
    # lifespan = lifespan
)

# include the router we created in the rotues.py file so that the app can use it
# book related endpoints can be access by goin to : http://localhost:8000/api/v1/books
app.include_router(book_router, prefix = f"/api/{version}/books", tags = ["books"])
app.include_router(author_router, prefix = f"/api/{version}/authors", tags = ["authors"])
