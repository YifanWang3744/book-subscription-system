from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# change it to your username and password to your database
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:dbuserdbuser@localhost:3306/books_schema"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()