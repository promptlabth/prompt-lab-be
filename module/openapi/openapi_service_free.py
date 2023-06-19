from fastapi import APIRouter
from pydantic import BaseModel
import openai

class OpenAiResDTO(BaseModel):
    reply:str
    error:str

class OpenAiRequest(BaseModel):
    """
    this class is model for Request on BaseModel
    """
    prompt: str
    model: str
    input_message: str
    tone_id: int
    feature_id: int

router = APIRouter(
    tags=["OpenAI Service"],
    responses={404: {"description": "Not found in"}},
)

@router.post("/gennerate-with-user", status_code=200, response_model=str) # No login require
def proxy_open_ai(prompt: OpenAiRequest) -> str:
    """
    this function to create proxy to openai
    
    """
    # result = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "user", "content": prompt.prompt},
    #     ],
    # )

    # assistant_reply = result['choices'][0]['message']['content']
    # return OpenAiResDTO(
    #     reply=assistant_reply,
    #     error=""
    # )

    return "good"