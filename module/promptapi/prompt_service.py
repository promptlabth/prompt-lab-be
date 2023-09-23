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
router.counter = 0


@router.post("/generate/free")
def generateTextReasult(
    userReq: OpenAiRequest
):
    """
    In this function is will be return a old message of user by userid
    """
    openai.api_key = os.environ.get("OPENAI_KEY")
    
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

    listPrompt = {
        "th" : {
            "เขียนแคปชั่นขายของ" : """Write a social media announcement about [{topic}] with hashtags and emojis The feeling of the message should be [{filling}]. [เป็นภาษาไทยเท่านั้น]""",
            "ช่วยคิดคอนเทนต์" : """ """,
            "เขียนบทความ": """ """,
            "เขียนสคริปวิดีโอสั้น" : """ """,
            "เขียนประโยคเปิดคลิป" : """ """
        },
        "en" : {
            "เขียนแคปชั่นขายของ" : "",
            "ช่วยคิดคอนเทนต์" : "",
            "เขียนบทความ": "",
            "เขียนสคริปวิดีโอสั้น" : "",
            "เขียนประโยคเปิดคลิป" : ""
        },
        "in" : {
            "เขียนแคปชั่นขายของ" : "",
            "ช่วยคิดคอนเทนต์" : "",
            "เขียนบทความ": "",
            "เขียนสคริปวิดีโอสั้น" : "",
            "เขียนประโยคเปิดคลิป" : ""
        }
    }
    prompt = ""
    
    tone = getToneById(userReq.tone_id)
    language = getLanguageById(tone.language_id)
    feature = getFeaturById(userReq.feature_id)
    
    result = openAiGenerate(language.language_name, feature.name, tone.tone_name, userReq.input_message)



    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data" : result,
            "model" : modelLanguage
        }
    )