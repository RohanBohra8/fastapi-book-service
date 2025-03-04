from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.books.models import Base

DATABASE_URL = "sqlite:///books.db"  # Directly hardcoded

# function that establishes connection to the database 
engine = create_engine(DATABASE_URL, connect_args = {"check_same-thread" : False})

# function that creates database session
# transaction will not commit automatically, must commit using .commit()
# by default SQLAlchemy will auto push changes to database, autoflush = false will disable them.
# bind to engine will connect the session to database 
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# This function creates all the tables in the database if they don’t already exist.
#metadata contains collection of all the database models
def init_db():
    Base.metadata.create_all(bind = engine)