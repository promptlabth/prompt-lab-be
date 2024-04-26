import random
import os
from typing import Annotated
from datetime import datetime

from fastapi import APIRouter, Depends, Response

from schemas.pydantic.generateSchema import (
    GenerateMessageRequest,
    GenerateMessageResponse
)

from services.generate_service import GenerateService

from middlewares.authentication import get_current_user

from model.promptMessages.prompt_messages_model import Promptmessages

from usecases.users import UsersUsecase
from usecases.prompt_messages import PromptMessageUsecase
from usecases.plans import PlanUsecases
from usecases.tones import ToneUsecase
from usecases.languages import LanguageUsecase
from usecases.features import FeatureUsecase
from usecases.input_prompts import InputPromptUsecase
from usecases.models import ModelUsecase
from usecases.user_message_remind import UserMessageRemindUsecase



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
    userMessageRemindUsecase: Annotated[UserMessageRemindUsecase, Depends()]

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
        total_messages_this_month = userMessageRemindUsecase.getUserRemind(user.firebase_id)
        maxMessage = plan.maxMessages
        if(total_messages_this_month.message_reminded >= maxMessage):
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

    # random a model choices 
    model_language_choices = ["GPT", "CLAUDE", "VERTEX"]
    weights = [0.5, 0.3, 0.2]
    # if os.environ.get("ENV") == "DEV":
    #     # ! in dev state will random to VERTEX only
    #     weights = [0, 1]
    result = ""
    # generate a text message 
    try:
        # try to generate a model
        while len(model_language_choices) > 0:
            # if model in choice is have will loop
            model_language = random.choices(model_language_choices, weights, k=1)[0] # random model
            if(model_language == "GPT"):
                # if choice is a GPT
                try:
                    model = modelUsecase.get_by_name(model_language)
                    db_prompt = inputPromptUsecase.get_by_feature_id_and_model_id(
                        feature.id, model.id, language.id
                    )
                    if db_prompt is None:
                        raise Exception('not found prompt')
                    input_prompt = db_prompt.prompt_input.format(
                        input = generateMessageRequest.input_message,
                        type = tone.tone_name
                    )
                    result = generate_service.generateMessageOpenAI(input_prompt)
                    break
                except:
                    # when GPT Model is DOWN !!
                    index = model_language_choices.index(model_language)
                    data = weights.pop(index)
                    weights[0] += data
                    model_language_choices.remove(model_language)
                    continue
            elif(model_language == "VERTEX"):
                # if select model is a vertex model
                try:
                    model = modelUsecase.get_by_name("VERTEX")
                    db_prompt = inputPromptUsecase.get_by_feature_id_and_model_id(
                        feature.id, model.id, language.id
                    )
                    if db_prompt is None:
                        raise Exception('not found prompt')
                    input_prompt = db_prompt.prompt_input.format(
                        input = generateMessageRequest.input_message,
                        type = tone.tone_name
                    )
                    result = generate_service.generateMessageVertexAI(
                        input_prompt,
                        feature.name
                    )
                    break
                except:
                    # WHEN VERTEX AI IS DOWN!!
                    index = model_language_choices.index(model_language)
                    data = weights.pop(index)
                    weights[0] += data
                    model_language_choices.remove(model_language)
                    continue
            elif(model_language == "CLAUDE"):
                # if select model is a CLAUDE model
                try:
                    model = modelUsecase.get_by_name(model_language)
                    db_prompt = inputPromptUsecase.get_by_feature_id_and_model_id(
                        feature.id, model.id, language.id
                    )
                    if db_prompt is None:
                        raise Exception('not found prompt')
                    input_prompt = db_prompt.prompt_input.format(
                        input = generateMessageRequest.input_message,
                        type = tone.tone_name
                    )
                    result = generate_service.claudeGennertor(input_prompt)
                    break
                except:
                    # when CLAUDE Model is DOWN !!
                    print("CLAUDE IS DOWN LOGGING")
                    index = model_language_choices.index(model_language)
                    data = weights.pop(index)
                    weights[0] += data
                    model_language_choices.remove(model_language)
                    continue
    except Exception as e:
        response.status_code = 404
        return GenerateMessageResponse(
            reply= "กรุณาลองใหม่ในภายหลัง",
            error= "process generate error exception"
        )
    
    if result == "":
        response.status_code = 404
        return GenerateMessageResponse(
            reply= "กรุณาลองใหม่ในภายหลัง",
            error= "process error"
        )


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

    total_messages_this_month = userMessageRemindUsecase.getUserRemind(user.firebase_id)
    total_messages_this_month.message_reminded+=1

    # upsert a total message of the month
    userMessageRemindUsecase.upsertUserRemind(total_messages_this_month)

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
