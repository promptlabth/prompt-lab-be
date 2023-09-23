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

from module.promptapi.prompt_utils.repository import getFeaturById, getLanguageById, getToneById
from module.promptapi.prompt_utils.open_ai import openAiGenerate
from module.promptapi.prompt_utils.vertex_parameter import vertexGenerator

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


@router.post("/generate-free-test")
def generateTextReasult(
    userReq: OpenAiRequest
):
    """
    In this function is will be return a old message of user by userid
    """
    
    model_language_choices = ["GPT", "VERTEX"]
    weights = [0.7, 0.3]

    modelLanguage = random.choices(model_language_choices, weights, k=1)[0]
    tone = getToneById(userReq.tone_id)
    language = getLanguageById(tone.language_id)
    feature = getFeaturById(userReq.feature_id)
    
    result = ""
    if(modelLanguage == "GPT"):
        result = openAiGenerate(language.language_name, feature.name, tone.tone_name, userReq.input_message)
    elif(modelLanguage == "VERTEX"):
        result = vertexGenerator(language.language_name, feature.name, tone.tone_name, userReq.input_message)


    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data" : result,
            "model" : modelLanguage,
            "lang": language.language_name,
            "tone" : tone.tone_name,
            "feature" : feature.name
        }
    )
