from fastapi import APIRouter
from pydantic import BaseModel
import openai
import os

class OpenAiResDTO(BaseModel):
    reply:str
    error:str

class OpenAiRequest(BaseModel):
    """
    this class is model for Request on BaseModel
    """
    prompt: str
    model: str
    

router = APIRouter(
    tags=["OpenAI Service"],
    responses={404: {"description": "Not found in"}},
)


@router.post("/gennerate", status_code=200) # No login require
def proxy_open_ai(prompt: OpenAiRequest):
    """
    this function to create proxy to openai
    
    """

    openai.api_key = os.environ.get("OPENAI_KEY")

    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt.prompt},
        ],
    )

    assistant_reply = result['choices'][0]['message']['content']
    return OpenAiResDTO(
            reply=assistant_reply,
            error=""
        )


    # return assistant_reply
