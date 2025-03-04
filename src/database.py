from sqlalchemy.ext.asyncio import create_async_engine , AsyncSession
from sqlalchemy.orm import sessionmaker
from src.books.models import Base

DATABASE_URL = "sqlite+aiosqlite:///books.db"  # Directly hardcoded

# function that establishes connection to the database 
async_engine = create_async_engine(DATABASE_URL, connect_args = {"check_same_thread" : False})

# function that creates database session
# transaction will not commit automatically, must commit using .commit()
# by default SQLAlchemy will auto push changes to database, autoflush = false will disable them.
# bind to engine will connect the session to database 
AsyncSessionLocal = sessionmaker(expire_on_commit=False ,class_=AsyncSession, autoflush = False,bind=async_engine)

# This function creates all the tables in the database if they don’t already exist.
#metadata contains collection of all the database models
async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)