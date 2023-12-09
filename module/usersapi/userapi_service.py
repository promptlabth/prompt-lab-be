import logging
from datetime import datetime
from sqlmodel import Session, select
from fastapi import APIRouter, Header, HTTPException, Request, Response, Depends, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Any, Annotated, Optional
from module.promptapi.prompt_utils.repository import (
    getUserByFirebaseId,
    getCoinBalanceByUserId,
    getPlanByUserId,
)
from middlewares import authentication

# import firebase 
from firebase import init_firebase
from firebase_admin import auth

# import a model session for read, create, update, delete a data in table
from model import database

# Import model of user model for dto, execute user table  
from model.users import users_model
from model.subscriptions_payments import subscriptions_payments_model
from model.plans import plans_model

logger = logging.getLogger(__name__)

# users_model.Users()
# dto for CRUD data (response user data)
class User(BaseModel):
    name: str
    email : str
    profilepic : str
    id : str
    
# request model for get access token
class RequestAccessToken(BaseModel):
    platform : str
    access_token : str


router = APIRouter(
    tags=["User Services"],
    responses={
        404:{"discription": "NOT FOUND!!"}
    },
    
)

# list all user (we should run a middleware for authentications)
# @router.get("/", status_code=200, response_model=list[users_model.Users])
# def list_users():
#     """
#     list all user in the table
#     """
#     data = []
#     with database.session_engine() as session:
#         users_exec = select(users_model.Users)
#         users = session.exec(statement=users_exec)
#         for user in users:
#             data.append(user)
#     return data

# def login_user(user_agent: str = Header(default=None)):

# POST login/register to collect data of user to database 
@router.post("/login", status_code=200)
def login_user(request: RequestAccessToken, Authorization:str = Header(default=None)):

    """
    For Login to use a pro service
    """


    # Check Have Authorization Token ?
    if(Authorization == None):
        print("no Access Token")
        raise HTTPException(status_code=401, detail="DON'T HAVE ACCESS TOKEN")

    # Check it have "Bearer" ?
    bearer = Authorization.split(" ")
    if(len(bearer) != 2 and bearer[1] != "Bearer"):
        raise HTTPException(status_code=401, detail="INCORRECT TOKEN")
    
    # Extract a token from bearer
    token = bearer[1]

    # validate and extract a token from firebase
    # (should check a refresh token and send to frontend if token is expirat)
    # TODO set a system to use refresh token and send access token to frontend if token is expirate
    try:
        # Use access token to authtication
        firebase_app = init_firebase.firebase_app_module()
        extract = auth.verify_id_token(
        id_token=token,
        app=firebase_app
        )
    except:
        # Use Refresh Token ??
        raise HTTPException(status_code=401, detail="DON'T AUTH")
    
    # extract a uid(firebaseID) from main structure
    uid = extract["uid"]
    # GET A USER FOR CHECK IT HAVE USER??
    
    with database.session_engine() as session:
        # Find a user in database is have user ? (by uid is mean firebase id)
        # Add upldate a access token
        
        statement = select(users_model.Users).where(users_model.Users.firebase_id == uid)
        results = session.exec(statement=statement)
        try:
            old_user = results.one()
            old_user.access_token = request.access_token
            old_user.platform = request.platform
            session.add(old_user)
            session.commit()
            session.refresh(old_user)
        except:
            old_user = {}

    
    # CHECK if have userid in database ?
    # if haven't in database
    if(not old_user):
        print("test")
        try:
            email = extract["email"]
        except:
            email = None

        try:
            # print(extract)
            user = users_model.Users(
                email=email, 
                name=extract["name"],
                profilepic=extract["picture"],
                firebase_id=extract["uid"],
                platform=request.platform,
                access_token=request.access_token,
                )
        except:
            raise HTTPException(status_code=403, detail={
                "err" : "CREATE User model failed",
                "extract" : extract
            })

        try:
            with database.session_engine() as session:
                session.add(user)
                session.commit()
                session.refresh(user)
            old_user = user
        except:
            raise HTTPException(status_code=403, detail="CREATE IN DATABASE FAILED")
    
    else:
        # if user have some change profile on facebook
        change_pic = extract["picture"] != old_user.profilepic
        change_name = extract["name"] != old_user.name
        try:
            email = extract["email"]
        except:
            email = None

        change_email = email != old_user.email
        # if not change (will return the user on database)
        if(not (change_pic or change_name or change_email)):
            print("\n\n\n")
            old_user = old_user
        
        if(change_pic):
            old_user.profilepic = extract["picture"]
        if(change_name):
            old_user.name = extract["name"]
        if(change_email):
            old_user.email = email
       
        # Update database if something is changed
        with database.session_engine() as session:
            session.add(old_user)
            session.commit()
            session.refresh(old_user)
     
    plan = getPlanByUserId(old_user.id)
    result = { "user": old_user, "plan": plan }

    return result

@router.get("/coin-balance")
def generateTextReasult(
    response: Response,
    firebaseId: Annotated[str, Depends(authentication.auth_depen_new)],
    Authorization: str = Header(default=None),
    RefreshToken: str = Header(default=None),
):
    """
    In this function is will be return a balance coin of user search by userid
    """
    # get user id
    user = getUserByFirebaseId(firebaseId)

    # default coin value
    coin = False
    # get coin data
    if user.id:
        coin = getCoinBalanceByUserId(user.id)

    # check if user have balance coin
    if coin == False:
        response_data = JSONResponse(
            status_code=status.HTTP_200_OK,
            content=0,
        )
    else:
        response_data = JSONResponse(
            status_code=status.HTTP_200_OK,
            content=coin.total,
        )

    return response_data


