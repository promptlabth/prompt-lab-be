from fastapi import Response, Request, HTTPException
from firebase import init_firebase
from firebase_admin import auth

import requests
import os
import dotenv
dotenv.load_dotenv()

import json


# fix auth to new dependency
async def auth_depen_new(
        req: Request,
        res: Response
) -> str:
    token_with_bearer = req.headers.get('Authorization')
    if(not token_with_bearer):
            raise HTTPException(status_code=401, detail="DON'T HAVE ACCESS TOKEN")

    try:
        token = token_with_bearer.split(" ")[1]
    except:
        raise HTTPException(404, "Not have Bearer in Access Token")
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
        firebase_app = init_firebase.firebase_app_module()
        # if refresh token is have ??
        refresh_token_with_bearer = req.headers.get("RefreshToken")
        if(not refresh_token_with_bearer):
            raise HTTPException(status_code=401, detail="DON'T HAVE REFRESH TOKEN")
        
        # get a refresh token
        try:
            refresh_token = refresh_token_with_bearer.split(" ")[1]
        except:
            raise HTTPException(404, "Refresh Token is not have Bearer")
        object = {
            'refresh_token':refresh_token,
            'grant_type':"refresh_token"
        }
        API_KEY = os.environ.get("FIREBASE_API_KEY")
        firebase_response = requests.post(f"https://securetoken.googleapis.com/v1/token?key={API_KEY}", object)
        firebase_response_json = json.loads(firebase_response.text)

        # if have some error will return refresh token is invalid
        if("error" in firebase_response_json):
            raise HTTPException(status_code=401, detail="REFRESH TOKEN IS INVALID")
        
        # but if token is good 
        res.headers["access-token"] = firebase_response_json['access_token']
        res.headers["refresh-token"] = firebase_response_json['refresh_token']
        # check access token is pass not error
        extract = auth.verify_id_token(
        id_token=token,
        app=firebase_app
        )
        # print("test")

        # extract a uid(firebaseID) from main structure
        uid = extract["uid"]
    return uid

def authentication_middleware():
    async def auth_dependency(request: Request, response: Response) -> None:
        
        token_with_bearer = request.headers.get('Authorization')
        
        if(not token_with_bearer):
            raise HTTPException(status_code=401, detail="DON'T HAVE ACCESS TOKEN")

        token = token_with_bearer.split(" ")[1]

        # check access token is pass
        try:
            # if access token is authorized
            firebase_app = init_firebase.firebase_app_module()
            # check access token is pass not error
            auth.verify_id_token(
            id_token=token,
            app=firebase_app
            )
            # print("test")
        except:
            # if refresh token is have ??
            refresh_token_with_bearer = request.headers.get("RefreshToken")
            if(not refresh_token_with_bearer):
                raise HTTPException(status_code=401, detail="DON'T HAVE REFRESH TOKEN")
            
            # get a refresh token
            refresh_token = refresh_token_with_bearer.split(" ")[1]
            object = {
                'refresh_token':refresh_token,
                'grant_type':"refresh_token"
            }
            API_KEY = os.environ.get("FIREBASE_API_KEY")
            firebase_response = requests.post(f"https://securetoken.googleapis.com/v1/token?key={API_KEY}", object)
            firebase_response_json = json.loads(firebase_response.text)

            # if have some error will return refresh token is invalid
            if("error" in firebase_response_json):
                raise HTTPException(status_code=401, detail="REFRESH TOKEN IS INVALID")
            
            # but if token is good 
            response.headers["access-token"] = firebase_response_json['access_token']
            response.headers["refresh-token"] = firebase_response_json['refresh_token']
            # print(firebase_response_json)

    return auth_dependency





def options(request: Request, response: Response) -> None:
    request_origin = request.headers.get('origin')
    
    
