from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# customize yours
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:dbuserdbuser@localhost:3306/user_schema"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()