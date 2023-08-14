
"""
Router for openAI Service
"""

import os

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

dotenv.load_dotenv()

class TextGenerationResponse(BaseModel):
    """
    this class is model for text genneration on BaseModel
    """
    generated_text: str

# DTO model for get data from users
class OpenAiRequest(BaseModel):
    """
    this class is model for Request on BaseModel
    """
    prompt: str
    model: str
    input_message: str
    tone_id: int
    feature_id: int

class OpenAiResDTO(BaseModel):
    reply:str
    error:str

# DTO for request method
class OpenAiRequestWithUser(BaseModel):
    """
    this class is model for Request on BaseModel
    request with firebase id of user
    """
    user_id: str # firebase ID
    prompt: str
    model: str
    input_message: str
    tone_id: int
    feature_id: int




openai.api_key = os.environ.get("OPENAI_KEY")


router = APIRouter(
    tags=["OpenAI Service"],
    responses={404: {"description": "Not found in"}},
)

router_with_dependency = APIRouter(
    tags=["OpenAI Service-Login"],
    responses={404: {"description": "Not found in"}},
    dependencies=[
        Depends(authentication.authentication_middleware())
    ],
)



async def testDepen(
        req: Request,
        res: Response
) -> str:  
    print(req.headers.get("Authorization"))
    res.headers["test"] = "tell"
    # raise HTTPException(status_code=401, detail="Fail")

    return "test"


@router.post("/test")
def getdata(
    data : Annotated[str, Depends(testDepen)]
):
    return data

# general generate
# can be use all prompt in this url
# TODO: 1. create a api for all feature in this app


"""
This function is for user to collect data
"""


class Message(BaseModel):
    id:int
    user_id:int
    tone_id:int
    tone:str
    date_time: datetime
    feature_id:str
    feature:str
    input_message:str
    result_message: str

@router.get("/get-caption", status_code=200)
def get_old_caption_by_user(
    # userid,
    response: Response,
    user: Annotated[str, Depends(authentication.auth_depen_new)],
    Authorization: str = Header(default=None),
    RefreshToken: str = Header(default=None),
):
    """
    In this function is will be return a old message of user by userid
    """

    messages = []
    # print(userid)

    with database.session_engine() as session:
        
        # Find id of user by firebase id
        
        try:
            statement_prompt = select(users_model.Users).where(
                users_model.Users.firebase_id == user
            ) 
            user_exec = session.exec(statement=statement_prompt).one()
            # print("userid = ", user_exec.id)
        except:
            return JSONResponse(
                content={
                        "error": "Not found a user by userid"
                },
                status_code=status.HTTP_404_NOT_FOUND
            )


        # Find a all prompt by userid
        try:
            statement_prompt = select(prompt_messages_model.Promptmessages).where(
                prompt_messages_model.Promptmessages.user_id == user_exec.id

            ) 
            prompt_messages_by_id = session.exec(statement=statement_prompt).all()
        except:
            return JSONResponse(
                content={
                        "error": "Not found a Prompt by userid"
                },
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        try:
            for prompt in prompt_messages_by_id:
                ms = Message(
                    id=prompt.id,
                    feature_id=prompt.feature_id,
                    feature=prompt.feature.name,
                    date_time=prompt.date_time,
                    input_message=prompt.input_message,
                    result_message=prompt.result_message,
                    tone_id=prompt.tone_id,
                    tone=prompt.tone.tone_name,
                    user_id=prompt.user_id
                )
                # print(ms)
                messages.append(ms)

            
            # print(messages)
            return messages
        
        except:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Found a error // you not have a prompt message, get one?"
            )




# TODO: 2. create a api with middleware in this app
@router.post("/gennerate-with-user", status_code=200, response_model=OpenAiResDTO) # login require
def proxy_open_ai_with_user(
    request: Request,
    response: Response,
    userReq: OpenAiRequestWithUser, 
    userid: Annotated[str, Depends(authentication.auth_depen_new)],
    Authorization:str = Header(default=None), 
    RefreshToken:str = Header(default=None),
    # auth:str = Depends(authentication.authentication_middleware)
    ) -> OpenAiResDTO:
    """
    this function to create proxy to openai with userid
    
    """
    # ! We need to all user can be get everything prompt 
    # ! So if we can't be collect data of user must send prompt result only
    # ! don't worry if data of user is not collect.

    openai.api_key = os.environ.get("OPENAI_KEY")
    
    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": userReq.prompt},
        ],
    )
    assistant_reply = result['choices'][0]['message']['content']

    # return OpenAiResDTO(
    #     reply=assistant_reply,
    #     error=""
    # )


    # # TODO: add a database zone for collect promptMessages
    with database.session_engine() as session:
        # * find user by firebase id if found will collect to user val 
        # ! but if not will return prompt result 
        try:
            statement_user = select(users_model.Users).where(users_model.Users.firebase_id == userReq.user_id)
            user = session.exec(statement=statement_user).one()
        except:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=OpenAiResDTO(
                    reply=assistant_reply,
                    error="Not Found Users"
                ).dict()
            )
        
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
                    user=user,
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
    
    try:
        response_data = JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=OpenAiResDTO(reply=assistant_reply, error="").dict(),
            headers={
                "AccessToken":response.headers["access-token"],
                "RefreshToken":response.headers["refresh-token"]
            }
        )
    except:
        response_data=JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=OpenAiResDTO(reply=assistant_reply, error="").dict(),
        )
        
    return response_data
