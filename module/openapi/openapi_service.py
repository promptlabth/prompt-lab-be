
"""
Router for openAI Service
"""

import os

from fastapi import APIRouter, Depends, Header, status, Request, Response
import openai
from pydantic import BaseModel
import dotenv
from middlewares import authentication
from fastapi.responses import JSONResponse

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
    tone: str
    feature: str

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
    tags=["OpenAI Service-Free"],
    responses={404: {"description": "Not found in"}},
)

router_with_dependency = APIRouter(
    tags=["OpenAI Service-Login"],
    responses={404: {"description": "Not found in"}},
    dependencies=[
        Depends(authentication.authentication_middleware())
    ],
)

@router.post("/test")
def getdata():
    return openai.api_key

# general generate
# can be use all prompt in this url
# TODO: 1. create a api for all feature in this app

@router.post("/gennerate-with-user", status_code=200, response_model=str) # No login require
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
    return OpenAiResDTO(
        reply=assistant_reply,
        error=""
    )


"""
This function is for user to collect data
"""



# TODO: 2. create a api with middleware in this app
# @router.post("/gennerate-with-user", status_code=200, response_model=OpenAiResDTO) # login require
# def proxy_open_ai_with_user(
#     request: Request,
#     response: Response,
#     userReq: OpenAiRequestWithUser, 
#     Authorization:str = Header(default=None), 
#     RefreshToken:str = Header(default=None),
#     # auth:str = Depends(authentication.authentication_middleware)
#     ) -> OpenAiResDTO:
#     """
#     this function to create proxy to openai
    
#     """
#     # ! We need to all user can be get everything prompt 
#     # ! So if we can't be collect data of user must send prompt result only
#     # ! don't worry if data of user is not collect.
    
#     result = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "user", "content": userReq.prompt},
#         ],
#     )
#     assistant_reply = result['choices'][0]['message']['content']


#     # TODO: add a database zone for collect promptMessages
#     with database.session_engine() as session:
#         # * find user by firebase id if found will collect to user val 
#         # ! but if not will return prompt result 
#         try:
#             statement_user = select(users_model.Users).where(users_model.Users.firebase_id == userReq.user_id)
#             user = session.exec(statement=statement_user).one()
#         except:
#             return JSONResponse(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 content=OpenAiResDTO(
#                     reply=assistant_reply,
#                     error="Not Found Users"
#                 ).dict()
#             )
        
#         # * find tone by tone id
#         # ! but if not will return prompt result
#         try:
#             statement_tone = select(tone_model.Tones).where(tone_model.Tones.id == userReq.tone_id)
#             tone = session.exec(statement=statement_tone).one()
#         except:
#             return JSONResponse(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 content=OpenAiResDTO(
#                     reply=assistant_reply,
#                     error="Not Found Tones"
#                 ).dict()
#             )
        
#         # * find tone by feature id
#         # ! but if not will return prompt result
#         try:
#             statement_feature = select(features_model.Features).where(features_model.Features.id == userReq.feature_id)
#             feature = session.exec(statement=statement_feature).one()
#         except:
#             return JSONResponse(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 content=OpenAiResDTO(
#                     reply=assistant_reply,
#                     error="Not Found feature"
#                 ).dict()
#             )
        
#         # * save data to database
#         # ! but if not work will return prompt result
#         try:
#             prompt_message_db = prompt_messages_model.Promptmessages(
#                 input_message=userReq.input_message,
#                 result_message=assistant_reply,
#                 feature_id=feature.id,
#                 tone_id=tone.id,
#                 user_id=user.id,
#                 date_time=datetime.now()
#             )
#             session.add(prompt_message_db)
#             session.commit()
#             session.refresh(prompt_message_db)
#         except:
#             return JSONResponse(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 content=OpenAiResDTO(
#                     reply=assistant_reply,
#                     error="cannot create and save to db"
#                 ).dict()
#             )
    
#     try:
#         response_data = JSONResponse(
#             status_code=status.HTTP_201_CREATED,
#             content=OpenAiResDTO(reply=assistant_reply, error="").dict(),
#             headers={
#                 "AccessToken":response.headers["access-token"],
#                 "RefreshToken":response.headers["refresh-token"]
#             }
#         )
#     except:
#         response_data=JSONResponse(
#             status_code=status.HTTP_201_CREATED,
#             content=OpenAiResDTO(reply=assistant_reply, error="").dict(),
#         )
        
#     return response_data
