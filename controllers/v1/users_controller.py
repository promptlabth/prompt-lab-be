
from usecases.users import UsersUsecase
from typing import Annotated

from fastapi import Depends, APIRouter

from middlewares.authentication import get_current_user
from model.users.users_model import Users


from usecases.user_message_remind import UserMessageRemindUsecase


from schemas.pydantic.userSchema import (
    UserUpdateRequest,
    ListUserResponse,
    UserUpdateresponse
)

userRouter = APIRouter(
    tags=["User Services", "v1"],
    prefix="/v1/user",
    responses={
        404:{"discription": "NOT FOUND!!"}
    },
)

@userRouter.get("remaining-message", status_code=200)
def remind_message(
    firebase_user: Annotated[str, Depends(get_current_user)],

    # usecase
    userMessageRemindUsecase: Annotated[UserMessageRemindUsecase, Depends()]
):
    return userMessageRemindUsecase.getUserRemind(firebase_user["uid"]).message_reminded
    

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