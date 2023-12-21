
from pydantic import BaseModel

from typing import List

from model.users.users_model import Users

class ListUserResponse(BaseModel):
    data: List[Users]

class UserUpdateresponse(BaseModel):
    data: Users


class UserUpdateRequest(BaseModel):
    id: int | None
    firebase_id: str | None = None
    name: str | None = None
    email: str | None = None
    profilepic: str | None = None
    platform: str | None = None
    access_token: str | None = None
    stripe_id: str | None = None

    plan_id: int | None = None

