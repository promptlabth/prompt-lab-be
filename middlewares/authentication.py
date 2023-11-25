"""
middleware authentication
"""
import os
import json
import requests
import dotenv

from fastapi import Response, Request, HTTPException
from firebase_admin import auth
from firebase import init_firebase
dotenv.load_dotenv()



# fix auth to new dependency
async def auth_depen_new(
        req: Request,
        res: Response
) -> str:
    """
    a new dependency for authtication in function
    """
    token_with_bearer = req.headers.get('Authorization')
    if not token_with_bearer:
        raise HTTPException(status_code=401, detail="DON'T HAVE ACCESS TOKEN")

    try:
        token = token_with_bearer.split(" ")[1]
    except Exception as exc:
        raise HTTPException(404, "Not have Bearer in Access Token") from exc
    uid = ""
    # check access token is pass
    try:
        firebase_app = init_firebase.firebase_app_module()
        # check access token is pass not error
        extract = auth.verify_id_token(
        id_token=token,
        app=firebase_app
        )
        # print("test")

        # extract a uid(firebaseID) from main structure
        uid = extract["uid"]
    except:
        raise HTTPException(status_code=401, detail="Access token is expired")
    return uid