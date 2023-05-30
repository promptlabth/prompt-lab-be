
"""
Router for openAI Service
"""

import os

from fastapi import APIRouter
import openai
from pydantic import BaseModel


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


openai.api_key = os.environ.get("OPENAI_KEY")


router = APIRouter(
    tags=["OpenAI Service"],
    responses={404: {"description": "Not found in"}},
)


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
