
from typing import Annotated

from fastapi import Depends, APIRouter

from app.middlewares.authentication import get_current_user
from app.model.users.users_model import Users


from app.usecases.user_balance_message import UserBalanceMessageUsecase
from app.usecases.users import UsersUsecase
from app.usecases.plans import PlanUsecases



from app.schemas.pydantic.userSchema import (
    UserUpdateRequest,
    ListUserResponse,
    UserUpdateresponse,
)

from app.schemas.pydantic.response_schema import ResponseSchema

userRouter = APIRouter(
    tags=["User Services", "v1"],
    prefix="/v1/user",
    responses={
        404:{"discription": "NOT FOUND!!"}
    },
)

@userRouter.get("/remaining-message", status_code=200)
def remind_message(
    firebase_user: Annotated[str, Depends(get_current_user)],

    # usecase
    userMessageRemindUsecase: Annotated[UserBalanceMessageUsecase, Depends()]
):
    return userMessageRemindUsecase.getUserBalance(firebase_user["uid"]).balance_message

@userRouter.post("/increase-usage", status_code=200)
def increase_usage(
    firebase_user: Annotated[str, Depends(get_current_user)],

    # usecase
    userBalanceMessageUsecase: Annotated[UserBalanceMessageUsecase, Depends()]
    
):
    total = userBalanceMessageUsecase.getUserBalance(firebase_user["uid"])
    total.balance_message += 1
    userBalanceMessageUsecase.upsertUserBalance(total)
    return {"status" : "ok"}
    

@userRouter.get("/max-message", status_code=200)
def get_max_message(
    firebase_user: Annotated[dict, Depends(get_current_user)],

    # usecase
    usersUsecase: Annotated[UsersUsecase, Depends()]
):
    max_message = usersUsecase.get_max_message_of_user(firebase_user["uid"])
    if max_message == None:
        return ResponseSchema(
            status_code=200,
            data=60
        )
    return ResponseSchema(
        status_code=200, 
        data= max_message
    )

# * endpoint to list a user data please disable in product
# @userRouter.get("/", status_code=200, response_model=ListUserResponse)
def list_user(
    # middleware for authen firebase
    firebase_user: Annotated[dict, Depends(get_current_user)], 
    usersUsecase: UsersUsecase = Depends()
) -> ListUserResponse:
    result = ListUserResponse(
            data=usersUsecase.list()
        )
    return result


# * patch a user data please disable in production
# @userRouter.patch("/", status_code=200, response_model=UserUpdateresponse)
def update_user(
        user: UserUpdateRequest,
        usersUsecase: UsersUsecase = Depends()
):
    result = UserUpdateresponse(
        data=usersUsecase.update(user.id, user)
    )
    return result