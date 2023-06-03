from datetime import datetime
from sqlmodel import Session, select
from fastapi import APIRouter, Header, HTTPException, Depends, Request, Response
from pydantic import BaseModel
from typing import List, Any, Annotated, Optional
from middlewares import authentication
# 
from firebase import init_firebase
from firebase_admin import auth

# import a model session for read, create, update, delete a data in table
from model import database

# Import model of user model for dto, execute user table  
from model.users import users_model

# users_model.Users()
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
    },
    dependencies=[
        Depends(authentication.authentication_middleware())
    ]
    
)

@router.get("/testPath")
def testMiddleware(request: Request, response: Response):
    return response.headers