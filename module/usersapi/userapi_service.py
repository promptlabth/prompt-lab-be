from datetime import datetime
from sqlmodel import Session, select
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any

# import a model session for read, create, update, delete a data in table
from model import database




# Import model of user model for dto, execute user table  
from model.users import users_model

users_model.Users()
# dto for CRUD data (response user data)
class User(BaseModel):
    name: str
    email : str
    profilepic : str
    id : str


router = APIRouter(
    tags=["User Services"],
    responses={
        404:{"discription": "NOT FOUND!!"}
    }
)

# list all user (we should run a middleware for authentications)
@router.get("/", status_code=200, response_model=list[users_model.Users])
def list_users():
    data = []
    with database.session_engine() as session:
        users_exec = select(users_model.Users)
        users = session.exec(statement=users_exec)
        for user in users:
            data.append(user)
    return data

# get user by id ??
# ?id should be use userid of datatbase or userid of firebase???
@router.get("/:id", status_code=200, response_model=users_model.Users)
def get_user():
    pass


