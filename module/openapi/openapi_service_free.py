from fastapi import APIRouter, status, Response
from pydantic import BaseModel
import openai
import os

import dotenv

from sqlmodel import select

from fastapi.responses import JSONResponse
from model import database
from model.promptMessages import prompt_messages_model
from model.tones import tone_model
from model.features import features_model
from datetime import datetime

dotenv.load_dotenv()
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


@router.post("/generate", status_code=200) # No login require
def proxy_open_ai(userReq: OpenAiRequest):
    """
    this function to create proxy to openai
    
    """

    openai.api_key = os.environ.get("OPENAI_KEY")

    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": userReq.prompt},
        ],
    )

    assistant_reply = result['choices'][0]['message']['content']
    
    with database.session_engine() as session:
         # * find tone by tone id
        # ! but if not will return prompt result
        try:
            statement_tone = select(tone_model.Tones).where(tone_model.Tones.id == userReq.tone_id)
            tone = session.exec(statement=statement_tone).one()
        except:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=OpenAiResDTO(
                    reply=assistant_reply,
                    error="Not Found Tones"
                ).dict()
            )
        
        # * find tone by feature id
        # ! but if not will return prompt result
        try:
            statement_feature = select(features_model.Features).where(features_model.Features.id == userReq.feature_id)
            feature = session.exec(statement=statement_feature).one()
        except:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=OpenAiResDTO(
                    reply=assistant_reply,
                    error="Not Found feature"
                ).dict()
            )
        
        # * save data to database
        # ! but if not work will return prompt result
        try:
            prompt_message_db = prompt_messages_model.Promptmessages(
                    input_message=userReq.input_message,
                    result_message=assistant_reply,
                    feature=feature,
                    tone=tone,
                    user=None,
                    date_time=datetime.now()
                )
        except:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=OpenAiResDTO(
                    reply=assistant_reply,
                    error="cannot create and save to db"
                ).dict()
            )

        try:
            session.add(prompt_message_db)
            session.commit()
            session.refresh(prompt_message_db)
        except:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=OpenAiResDTO(
                    reply=assistant_reply,
                    error="cannot save to db"
                ).dict()
            )

    response_data = JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=OpenAiResDTO(reply=assistant_reply, error="").dict(),
    )


    return response_data
