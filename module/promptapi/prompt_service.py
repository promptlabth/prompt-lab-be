"""
Router for language model service 
- OPENAI
- VERTEX AI
"""

import os 
import random

from fastapi import APIRouter, Depends, HTTPException, Header, status, Request, Response
import openai
from pydantic import BaseModel
import dotenv
from middlewares import authentication
from fastapi.responses import JSONResponse

from typing import Annotated, List


from sqlmodel import select

from model import database
from model.promptMessages import prompt_messages_model
from model.users import users_model
from model.tones import tone_model
from model.features import features_model
from datetime import datetime

from module.promptapi.prompt_utils.repository import getFeaturById, getLanguageById, getToneById, getUserByFirebaseId, getModelAIById
from module.promptapi.prompt_utils.open_ai import openAiGenerate
from module.promptapi.prompt_utils.vertex_parameter import vertexGenerator
from model.models import models_model



dotenv.load_dotenv()

class OpenAiRequest(BaseModel):
    """
    this calss is model for Request to api
    """
    input_message: str
    tone_id: int
    feature_id: int

class ResponseHttp(BaseModel):
    """
    this model for response case in endpoint
    """
    reply: str
    error: str


router = APIRouter(
    tags=["Language AI Service"],
    responses={404: {"description" : "Not Found"}}
)


openai.api_key = os.environ.get("OPENAI_KEY")


@router.post("/generate-random")
def generateTextReasult(
    response: Response,
    userReq: OpenAiRequest,
    firebaseId: Annotated[str, Depends(authentication.auth_depen_new)],
    Authorization:str = Header(default=None), 
    RefreshToken:str = Header(default=None),
):
    """
    In this function is will be return a old message of user by userid
    """
    
    listModelLanguage = [
        "GPT",
        "GPT",
        "GPT",
        "GPT",
        "GPT",
        "GPT",
        "GPT",
        "VERTEX",
        "VERTEX",
        "VERTEX"
    ]
    modelLanguage = random.choice(listModelLanguage)

    user = getUserByFirebaseId(firebaseId)
    tone = getToneById(userReq.tone_id)
    language = getLanguageById(tone.language_id)
    feature = getFeaturById(userReq.feature_id)
    
    result = "test"

    if(modelLanguage == "GPT"):
        result = openAiGenerate(language.language_name, feature.name, tone.tone_name, userReq.input_message)
        model = getModelAIById("GPT")
    elif(modelLanguage == "VERTEX"):
        result = vertexGenerator(language.language_name, feature.name, tone.tone_name, userReq.input_message)
        model = getModelAIById("VERTEX")

    try:
        prompt_message_db = prompt_messages_model.Promptmessages(
            input_message=userReq.input_message,
            result_message=result,
                    feature=feature,
                    tone=tone,
                    user=user,
                    model=model,
                    date_time=datetime.now()
        )
    except:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=ResponseHttp(
                reply=result,
                error="cannot create and save to db"
            ).dict()
        )
    with database.session_engine() as session:
        try:
            session.add(prompt_message_db)
            session.commit()
            session.refresh(prompt_message_db)
        except:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=ResponseHttp(
                    reply=result,
                    error="cannot save to db"
                ).dict()
            )
    try:
        response_data = JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=ResponseHttp(reply=result, error="").dict(),
            headers={
                "AccessToken":response.headers["access-token"],
                "RefreshToken":response.headers["refresh-token"]
            }
        )
    except:
        response_data=JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=ResponseHttp(reply=result, error="").dict(),
        )
        
    return response_data

@router.post("/generate-random-free")
def generateTextReasult(
    userReq: OpenAiRequest,
):
    """
    In this function is will be return a old message of user by userid
    """
    
    listModelLanguage = [
        "GPT",
        "GPT",
        "GPT",
        "GPT",
        "GPT",
        "GPT",
        "GPT",
        "VERTEX",
        "VERTEX",
        "VERTEX"
    ]
    modelLanguage = random.choice(listModelLanguage)

    tone = getToneById(userReq.tone_id)
    language = getLanguageById(tone.language_id)
    feature = getFeaturById(userReq.feature_id)
    
    result = "test"
    model = models_model.Models()
    if(modelLanguage == "GPT"):
        model = getModelAIById("GPT")
    else:
        model = getModelAIById("VERTEX")


    if(modelLanguage == "GPT"):
        result = openAiGenerate(language.language_name, feature.name, tone.tone_name, userReq.input_message)
        model = getModelAIById("GPT")
    elif(modelLanguage == "VERTEX"):
        result = vertexGenerator(language.language_name, feature.name, tone.tone_name, userReq.input_message)
        model = getModelAIById("VERTEX")

    try:
        prompt_message_db = prompt_messages_model.Promptmessages(
            input_message=userReq.input_message,
            result_message=result,
            feature=feature,
            tone=tone,
            user=None,
            model=model,
            date_time=datetime.now()
        )
    except:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=ResponseHttp(
                reply=result,
                error="cannot create and save to db"
            ).dict()
        )
    with database.session_engine() as session:
        try:
            session.add(prompt_message_db)
            session.commit()
            session.refresh(prompt_message_db)
        except:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=ResponseHttp(
                    reply=result,
                    error="cannot save to db"
                ).dict()
            )
    response_data=JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=ResponseHttp(reply=result, error="").dict(),
    )
        
    return response_data