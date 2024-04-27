from pydantic import BaseModel

from typing import Optional

from app.model.users.users_model import Users
from app.model.plans.plans_model import Plans

from datetime import datetime

class LoginStripeResponse(BaseModel):
    product: Plans
    start_date: Optional[datetime]
    end_date: Optional[datetime]

class LoginResponse(BaseModel):
    user: Users
    plan: LoginStripeResponse

class LoginRequest(BaseModel):
    platform: str
    access_token:str