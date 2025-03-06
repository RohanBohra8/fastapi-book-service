from fastapi import FastAPI
from src.books.routes import book_router
from src.books.author_routes import author_router

version = "v1"

app = FastAPI(
    title = "Bookify",
    description = "Restful API for book service",
    version = version,
)

app.include_router(book_router, prefix = f"/api/{version}/books", tags = ["books"])
app.include_router(author_router, prefix = f"/api/{version}/authors", tags = ["authors"])
