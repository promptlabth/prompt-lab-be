from sqlmodel import Field, SQLModel, create_engine, Session
import os


# should be remove before push to production
from dotenv import load_dotenv 
load_dotenv() 


DATABASE_USER = os.environ.get("DB_USER")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
DATABASE_HOST = os.environ.get("DB_HOST")
DATABASE_PORT = os.environ.get("DB_PORT")
DATABASE_NAME = os.environ.get("DB_NAME")


postgres_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

engine = create_engine(postgres_URL, echo=True, future=True, pool_size=10, max_overflow=20)

def create_database():
    SQLModel.metadata.create_all(engine)

def session_engine(): 
    return Session(engine)

def get_session():
    with Session(engine) as session:
        yield session
        
