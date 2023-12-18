
from usecases.users import UsersUsecase

from fastapi import Depends, APIRouter

from model.users.users_model import Users

from schemas.pydantic.userSchema import (
    UserUpdateRequest,
    ListUserResponse,
    UserUpdateresponse
)

userRouter = APIRouter(
    tags=["User Services"],
    prefix="/v1/user",
    responses={
        404:{"discription": "NOT FOUND!!"}
    },
)

@userRouter.get("/", status_code=200, response_model=ListUserResponse)
def list_user(
    usersUsecase: UsersUsecase = Depends()
) -> ListUserResponse:
    result = ListUserResponse(
            data=usersUsecase.list()
        )
    return result


@userRouter.patch("/", status_code=200, response_model=UserUpdateresponse)
def update_user(
        user: UserUpdateRequest,
        usersUsecase: UsersUsecase = Depends()
):
    result = UserUpdateresponse(
        data=usersUsecase.update(user.id, user)
    )
    return result