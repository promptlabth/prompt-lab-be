from pydantic import BaseModel

from typing import Optional

from app.model.users.users_model import Users
from app.model.plans.plans_model import Plans

from datetime import datetime


class LoginPlanResponse(BaseModel):
    id: Optional[int] 
    planType: str
    maxMessages: int
    product_id: Optional[str]
class LoginStripeResponse(BaseModel):
    product: LoginPlanResponse
    start_date: Optional[datetime]
    end_date: Optional[datetime]

class LoginResponse(BaseModel):
    user: Users
    plan: LoginStripeResponse

class LoginRequest(BaseModel):
    platform: str
    access_token:str

