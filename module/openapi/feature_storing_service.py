import os
import time
from fastapi import APIRouter, Depends,Header,Request,Response,status, HTTPException
import openai
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from sqlmodel import select
from middlewares import authentication
from model import database
from model.users import users_model
from model.featureusings import feature_usings_model
from model.features import features_model
from datetime import datetime

# for input data when set start time
class FeatureWithUserStart(BaseModel):
    user_id: str
    feature_id: str

# for input data when set stop time
class FeatureWithUserStop(BaseModel):
    id: str
    user_id: str
    feature_id: str

# for response data
class FeatureUsingResponse(BaseModel):
    id : str
    user_id: str
    feature_id: str
    error:str

openai.api_key = os.environ.get("OPENAI_KEY")

router = APIRouter(
    tags=["Feature Services"],
    responses={404: {"description": "Not found in"}},
)

router_with_dependency = APIRouter(
    tags=["User-Feature Service-Free"],
    responses={404: {"description": "Not found in"}},
    dependencies=[
        Depends(authentication.authentication_middleware())
    ]
)


# TODO: 1. create a api for time start 
@router_with_dependency.post("/feature-using/start", status_code=200, response_model=FeatureUsingResponse)
def feature_storing_start(
    featureStart: FeatureWithUserStart, 
    request: Request,
    response: Response,
    Authorization:str= Header(default=None),
    RefreshToken:str = Header(default=None),
    ) -> FeatureUsingResponse:
    """
    this function to create feature-using and set start time
    
    """

    # TODO: add a database zone for collect featureUsing
    with database.session_engine() as session:

        # * find user by firebase id if it can found then will collect to user val 
        # ! but if it not will return that no need for store data
        try:
            statement_user = select(users_model.Users).where(users_model.Users.firebase_id == featureStart.user_id)
            user = session.exec(statement=statement_user).one()
        except:
            return HTTPException(
                status_code=404, 
                detail="Not Found User, No need to store data"
            )
        
        # * find feature by feature id
        # ! no need to return exception
        try:
            statement_feature = select(features_model.Features).where(features_model.Features.id==featureStart.feature_id)
            feature = session.exec(statement=statement_feature).one()
            print("Find feature id")
        except:
            print("cannot Find feature id")
            return HTTPException(
                status_code=404,
                detail = "Not Found Features"
            )
        
        # * save data to database
        # ! but if not work will return exception
        try:
            # set time format
            currentDateAndTime = datetime.now()
            currentTime = currentDateAndTime.strftime("%H:%M:%S")
            print(time.localtime())
            feature_message_db = feature_usings_model.Featureusings(
                user_id= user.id,
                feature_id=feature.id,
                dates=datetime.now(),
                timestart=currentTime,
                timestop=currentTime

            )
            session.add(feature_message_db)
            session.commit()
            session.refresh(feature_message_db)
            print("create feature using")
        except:
            return HTTPException(
                status_code=404,
                detail = "cannot create and save feature using to database"
            )
        
    try:
        response_data = JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=FeatureUsingResponse(
        id = feature_message_db.id,
        user_id= user.id,
        feature_id= feature.id, 
        error="").dict(),
        headers={
                "AccessToken":response.headers["access-token"],
                "RefreshToken":response.headers["refresh-token"]
            }
        )
    except:
            response_data = JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=FeatureUsingResponse(
                id = feature_message_db.id,
                user_id= user.id,
                feature_id= feature.id, 
                error="cannot get accessToken or refreshToken").dict(),
            )


    return response_data

# TODO: 2. create a api for time stop
@router_with_dependency.post("/feature-using/stop", status_code=200, response_model=FeatureUsingResponse) # login require
def feature_storing_start(
    featureStop: FeatureWithUserStop, 
    request: Request,
    response: Response,
    Authorization:str= Header(default=None),
    RefreshToken:str = Header(default=None),
    ) -> FeatureUsingResponse:
    """
    this function to set stop time
    
    """

    # TODO: add a database zone for collect promptMessages
    with database.session_engine() as session:

        # * find user by firebase id if found will collect to user val 
        # ! but if not will do not thing
        try:
            statement_user = select(users_model.Users).where(users_model.Users.firebase_id == featureStop.user_id)
            user = session.exec(statement=statement_user).one()
        except:
            return HTTPException(status_code=404, detail="Not Found User, No need to store data")
        
        # * find feature by feature id
        # ! no need to return anything 
        try:
            statement_feature = select(features_model.Features).where(features_model.Features.id==featureStop.feature_id)
            feature = session.exec(statement=statement_feature).one()
        except:
            return HTTPException(
                status_code=404,
                detail = "Not Found Features"
            )
        
        # * find featureusing by featureusing id
        # ! no need to return anything 
        try:
            statement_feature = select(feature_usings_model.Featureusings).where(feature_usings_model.Featureusings.id==featureStop.id)
            featureusings = session.exec(statement=statement_feature).one()

        except:
            return HTTPException(
                status_code=404,
                detail = "Not Found Featureusings"
            )
        
        # * check if it has the same feature_id(upComing data and database)
        # ! return error if not true
        try:
            statement_feature = select(feature_usings_model.Featureusings).where(feature_usings_model.Featureusings.id==featureStop.id).where(feature_usings_model.Featureusings.feature_id==featureStop.feature_id)
            featureusings = session.exec(statement=statement_feature).one()
        except:
            return HTTPException(
                status_code=404,
                detail = "Not Match featureusing id"
            )
        
        # * update data to database
        # ! but if not work will do nothing
        try:
            currentDateAndTime = datetime.now()
            currentTime = currentDateAndTime.strftime("%H:%M:%S")
            featureusings.timestop = currentTime
            session.add(featureusings)
            session.commit()
            session.refresh(featureusings)
        except:
            return HTTPException(
                status_code=404,
                detail = "cannot update and save featureusing to database"
            )
        
    try:
        response_data = JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=FeatureUsingResponse(
        id = featureStop.id,
        user_id= user.id,
        feature_id= feature.id, 
        error="").dict(),
        headers={
                "AccessToken":response.headers["access-token"],
                "RefreshToken":response.headers["refresh-token"]
            }
        )
    except:
        response_data = JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=FeatureUsingResponse(
        id = featureStop.id,
        user_id= user.id,
        feature_id= feature.id, 
        error="cannot get accessToken or refreshToken").dict(),
        )


    return response_data
    
