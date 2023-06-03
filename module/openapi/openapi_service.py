
"""
Router for openAI Service
"""

import os

from fastapi import APIRouter, Depends
import openai
from pydantic import BaseModel
import dotenv
from middlewares import authentication

dotenv.load_dotenv()

class TextGenerationResponse(BaseModel):
    """
    this class is model for text genneration on BaseModel
    """
    generated_text: str

class OpenAiRequest(BaseModel):
    """
    this class is model for Request on BaseModel
    """
    prompt: str
    model: str
    product: str
    tone: str
    feature: str



openai.api_key = os.environ.get("OPENAI_KEY")


router = APIRouter(
    tags=["OpenAI Service-Free"],
    responses={404: {"description": "Not found in"}},
)

router_with_dependency = APIRouter(
    tags=["OpenAI Service-Free"],
    responses={404: {"description": "Not found in"}},
    dependencies=[
        Depends(authentication.authentication_middleware())
    ]
)

@router.post("/test")
def getdata():
    return openai.api_key

# general generate
# can be use all prompt in this url
# TODO: 1. create a api for all feature in this app

@router.post("/gennerate", status_code=200, response_model=str)
def proxy_open_ai(prompt: OpenAiRequest) -> str:
    """
    this function to create proxy to openai
    
    """
    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt.prompt},
        ],
    )

    assistant_reply = result['choices'][0]['message']['content']
    return assistant_reply

# TODO: 2. create a api with middleware in this app
router_with_dependency.post("/gennerate", status_code=200, response_model=str)
def proxy_open_ai_and_collect_data(prompt: OpenAiRequest) -> str:
    pass
