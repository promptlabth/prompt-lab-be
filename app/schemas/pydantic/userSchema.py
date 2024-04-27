
from pydantic import BaseModel

from typing import List, Optional

from app.model.users.users_model import Users

class ListUserResponse(BaseModel):
    data: List[Users]

class UserUpdateresponse(BaseModel):
    data: Users


class UserUpdateRequest(BaseModel):
    id: Optional[int] = None
    firebase_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    profilepic: Optional[str] = None
    platform: Optional[str] = None
    access_token: Optional[str] = None
    stripe_id: Optional[str] = None

    plan_id: Optional[int] = None

