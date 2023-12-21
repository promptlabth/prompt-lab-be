from pydantic import BaseModel

from typing import List

from model.users.users_model import Users
from model.plans.plans_model import Plans

from datetime import datetime

class LoginStripeResponse(BaseModel):
    product: Plans
    start_date: datetime | None
    end_date: datetime | None

class LoginResponse(BaseModel):
    user: Users
    plan: LoginStripeResponse

class LoginRequest(BaseModel):
    platform: str
    access_token:str