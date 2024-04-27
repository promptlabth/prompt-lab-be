"""
middleware authentication
"""
import os
import json
import requests
import dotenv

from typing import Annotated

from fastapi import Response, Request, HTTPException
from firebase_admin import auth

from fastapi import Depends

from fastapi.security import OAuth2PasswordBearer

from app.services.firebase_service import FirebaseService

dotenv.load_dotenv()

# create a oauth2 schema
oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

# v1 authentication pattern
async def get_current_user(token : Annotated[str, Depends(oauth2_schema)]):
    # call a service 
    firebase_service =  FirebaseService()
    
    decode_token = firebase_service.validate(token)
    if decode_token is None:
        raise HTTPException(status_code=401, detail="Access token is expired")
    
    return decode_token

