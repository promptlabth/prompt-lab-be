
"""
Router for openAI Service
"""

import os
from typing import List, Optional

from fastapi import APIRouter
import openai
from pydantic import BaseModel


class TextGenerationResponse(BaseModel):
    generated_text: str

class Prompt(BaseModel):
    text: str


openai.api_key = os.environ.get("OPANAI_KEY")


router = APIRouter(
    tags=["OpenAI Service"],
    responses={404: {"description": "Not found in /create"}},
)


@router.post("/gennerate", status_code=200, response_model=str)
def proxy_open_ai(prompt: Prompt) -> str:
    """
    this function to create proxy to openai
    
    """

    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt.text},
        ],
    )

    assistant_reply = result['choices'][0]['message']['content']
    return assistant_reply
