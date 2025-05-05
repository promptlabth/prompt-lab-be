import random
import os
from typing import Annotated
from datetime import datetime

from fastapi import APIRouter, Depends, Response

from app.schemas.pydantic.generateSchema import (
    GenerateMessageRequest,
    GenerateMessageResponse
)

from app.external_service.generate_service import GenerateService

from app.middlewares.authentication import get_current_user

from app.model.promptMessages.prompt_messages_model import Promptmessages

from app.usecases.users import UsersUsecase
from app.usecases.prompt_messages import PromptMessageUsecase
from app.usecases.plans import PlanUsecases
from app.usecases.tones import ToneUsecase
from app.usecases.languages import LanguageUsecase
from app.usecases.features import FeatureUsecase
from app.usecases.input_prompts import InputPromptUsecase
from app.usecases.models import ModelUsecase
from app.usecases.user_balance_message import UserBalanceMessageUsecase



prompt_routers = APIRouter(
    tags=["Generate AI Service \"Can't run in page\"", "v1"],
    prefix="/v1/generate",
    responses={
        404:{"description": "Generate API Error or Not Found"}
        }
)


@prompt_routers.post("/messages", status_code=200, response_model=GenerateMessageResponse)
def generate_message_api(
    response:Response,
    generateMessageRequest: GenerateMessageRequest,

    # middleware for authen firebase
    firebase_user: Annotated[dict, Depends(get_current_user)], 

    # usecase for this controllers
    userUsecase: Annotated[UsersUsecase, Depends()],
    promptMessageUsecase: Annotated[PromptMessageUsecase, Depends()],
    planUsecase: Annotated[PlanUsecases, Depends()],
    toneUsecase: Annotated[ToneUsecase, Depends()],
    languageUsecase: Annotated[LanguageUsecase, Depends()],
    featureUsecase: Annotated[FeatureUsecase, Depends()],
    inputPromptUsecase: Annotated[InputPromptUsecase, Depends()],
    modelUsecase: Annotated[ModelUsecase, Depends()],
    userBalanceMessageUsecase: Annotated[UserBalanceMessageUsecase, Depends()]

) -> GenerateMessageResponse:
    """
    this function will generate a message and save this message to user history
    all message generate will need to authorize 
    """

    user = userUsecase.get_by_firebase_id(firebase_user["uid"])
    if user is None:
        # if not found a user in database
        response.status_code = 404
        return GenerateMessageResponse(
            reply="การเข้าสู่ระบบมีปัญหา กรุณา Login ใหม่อีกครั้ง",
            error="Firebase Login is Exp"
        )
    
    # get plan of user
    plan = planUsecase.get_by_id(user.plan_id)
    if plan is None:
        # if not found a plan in database
        response.status_code = 404
        return GenerateMessageResponse(
            reply="แพลนที่ใช้งานมีปัญหา กรุณาลองใหม่อีกครั้ง",
            error="Plan is Not found"
        )
    
    # handle when user limit message per month
    enableLimitMessage = True
    if(enableLimitMessage):
        total_messages_this_month = userBalanceMessageUsecase.getUserBalance(user.firebase_id)
        maxMessage = plan.max_messages
        if(total_messages_this_month.balance_message >= maxMessage):
            return GenerateMessageResponse(
                reply="คุณใช้งานเกินจำนวนที่กำหนดแล้ว กรุณาลองใหม่ในเดือนถัดไป หรือปรับระดับ plan",
                error="limit message"
            )
    
    # get tone by id
    tone = toneUsecase.get_by_id(generateMessageRequest.tone_id)
    if tone is None:
        # if not found a tone from database
        response.status_code = 404
        return GenerateMessageResponse(
            reply="กรุณาลองใหม่ในภายหลัง",
            error="tone is not found user add a maunal tone id"
        )
    
    # get language by id
    language = languageUsecase.get_by_id(tone.language_id)
    if language is None:
        # if not found a language from database
        response.status_code = 404
        return GenerateMessageResponse(
            reply="กรุณาลองใหม่ในภายหลัง",
            error="language is not found something is error"
        )
    
    # get feature by id
    feature = featureUsecase.get_by_id(generateMessageRequest.feature_id)
    if feature is None:
        # if not found a feature from database
        response.status_code = 404
        return GenerateMessageResponse(
            reply="กรุณาลองใหม่ในภายหลัง",
            error="feature is not found user add a maunal feature id"
        )

    # call generate service
    generate_service = GenerateService()
    
    result = ""
    # generate a text message 
    try:
        # Get Gemini model
        model = modelUsecase.get_by_name("GEMINI")
        if model is None:
            raise Exception('Gemini model not found in database')
            
        # Get prompt template
        db_prompt = inputPromptUsecase.get_by_feature_id_and_model_id(
            feature.id, model.id, language.id
        )
        if db_prompt is None:
            raise Exception('Prompt template not found')
            
        # Format the prompt
        input_prompt = db_prompt.prompt_input.format(
            input = generateMessageRequest.input_message,
            type = tone.tone_name
        )
        
        # Generate with Gemini
        result = generate_service.generateMessageGemini(input_prompt)
        
    except Exception as e:
        print(f"Error in generation: {str(e)}")  # Add logging
        response.status_code = 404
        return GenerateMessageResponse(
            reply= "กรุณาลองใหม่ในภายหลัง",
            error= f"process generate error: {str(e)}"
        )
    
    if result == "":
        response.status_code = 404
        return GenerateMessageResponse(
            reply= "กรุณาลองใหม่ในภายหลัง",
            error= "process error: empty response"
        )

    # Save the generated message
    promptMessage = Promptmessages(
        input_message=generateMessageRequest.input_message,
        result_message=result,
        feature=feature,
        tone=tone,
        user=user,
        model=model,
        date_time=datetime.now()
    )
    prompt_message_db = promptMessageUsecase.create(promptMessage)

    # Update user balance
    total_messages_this_month = userBalanceMessageUsecase.getUserBalance(user.firebase_id)
    total_messages_this_month.balance_message+=1
    userBalanceMessageUsecase.upsertUserBalance(total_messages_this_month)

    if prompt_message_db is None:
        response = GenerateMessageResponse(
            reply= result,
            error= "can't save data to database something error"
        )
        return response

    response = GenerateMessageResponse(
        reply= prompt_message_db.result_message,
        error= ""
    )
    return response
