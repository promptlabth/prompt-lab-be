from sqlmodel import Field, SQLModel, create_engine, Session
import os
import users,sponsors,sponsortypes,users_sponser_select,features,featureusings
import languages
import tones
import promptMessages, promptRows

# should be remove before push to production
from dotenv import load_dotenv 
load_dotenv() 


DATABASE_USER = os.environ.get("DB_USER")
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD")
DATABASE_HOST = os.environ.get("DB_HOST")
DATABASE_PORT = os.environ.get("DB_PORT")
DATABASE_NAME = os.environ.get("DB_NAME")


postgres_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

engine = create_engine(postgres_URL, echo=True, future=True)

def create_database():
    SQLModel.metadata.create_all(engine)

def session_engine(): 
    return Session(engine)

create_database()