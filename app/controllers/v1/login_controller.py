from typing import Annotated

from fastapi import (
    Depends, 
    APIRouter, 
    Header, 
    HTTPException
)

from app.schemas.pydantic.loginSchema import (
    LoginResponse, 
    LoginRequest,
    LoginStripeResponse,
    LoginPlanResponse
)

from app.schemas.pydantic.userSchema import (
    UserUpdateRequest
)

from app.external_service.firebase_service import (
    FirebaseService
)
from app.external_service.stripe_service import StripeService

from app.middlewares.authentication import get_current_user

from app.usecases.users import UsersUsecase
from app.usecases.plans import PlanUsecases
from app.usecases.user_balance_message import UserBalanceMessageUsecase

from app.model.users.users_model import Users
from app.model.user_balance_messages.user_balance_messages_model import UserMessageBalance



loginRouter = APIRouter(
    tags=["User Services", "v1"],
    prefix="/v1/login",
    responses={
        404:{"discription": "Not Found a URL or this URL is invalid"}
    },
)

@loginRouter.post("", status_code=200, response_model=LoginResponse)
def login(
    request: LoginRequest,
    userUsecases: Annotated[UsersUsecase, Depends()] ,
    planUsecases: Annotated[PlanUsecases, Depends()] ,
    userBalanceMessageUsecases: Annotated[UserBalanceMessageUsecase, Depends()],
    firebase_user: Annotated[dict, Depends(get_current_user)]
) -> LoginResponse:
    """
    For Login to a website service
    """

    # initial Service Class
    stripe_service = StripeService()

    
    if firebase_user is None:
        raise HTTPException(status_code=401, detail="DON'T AUTH OR TOKEN IS Expire")
    firebase_user_id = firebase_user["uid"]
    try:
        firebase_user_email = firebase_user["email"]
    except:
        firebase_user_email = None

    old_user = userUsecases.get_by_firebase_id(firebase_user_id)
    user : Users
    if old_user is None:

        """
        incase don't have a old user
        
        create a new user to table
        """
        free_plan = planUsecases.get_by_plan_type("Free")
        if free_plan is None:
            raise HTTPException(status_code=401, detail="Free Plan is not found [create failed]")
        new_user = Users(
            email = firebase_user_email,
            name=firebase_user["name"],
            profilepic=firebase_user["picture"],
            firebase_id=firebase_user["uid"],
            platform=request.platform,
            access_token=request.access_token,
            plan_id=free_plan.id
        )
        
        user = userUsecases.create(new_user)

        new_user_remind = UserMessageBalance(
            firebase_id=user.firebase_id,
            balance_message=0
        )
        user_remind = userBalanceMessageUsecases.upsertUserBalance(new_user_remind)
    else:
        # will update a profile 

        # prepare a data for update to database
        user_update = UserUpdateRequest(
            email = firebase_user_email,
            firebase_id=firebase_user["uid"],
            name=firebase_user["name"],
            profilepic=firebase_user["picture"],
            platform=request.platform,
            access_token=request.access_token,
            stripe_id=old_user.stripe_id,
            plan_id=old_user.plan_id
        )

        # update a data to database
        user = userUsecases.update(
            old_user.id,
            user_update
        )

        # create if userRemindIsNotFound
        user_remind = userBalanceMessageUsecases.getUserBalance(user.firebase_id)
        if user_remind == None:
            new_user_remind = UserMessageBalance(
                firebase_id=user.firebase_id,
                balance_message=0
            )
            user_remind = userBalanceMessageUsecases.upsertUserBalance(new_user_remind)
    
    # get a plan from stripe service
    
    user = userUsecases.get(user.id)
    if(user.stripe_id is None):
        # incase user don't have a stripe id
        plan = planUsecases.get_by_id(user.plan_id)
        planRes = LoginPlanResponse(
            id=plan.id,
            maxMessages=plan.max_messages,
            planType=plan.plan_type,
            product_id=plan.product_id
        )
        stripe_res = LoginStripeResponse(
            product=planRes,
            start_date=None,
            end_date=None
        )
        return LoginResponse(
            user=user,
            plan=stripe_res
        )
    else:
        # incase user have a stripe id (prev is have some action to payment to stripe)
        start_end_period = stripe_service.get_start_end_date(user.stripe_id)
        plan = planUsecases.get_by_id(user.plan_id)
        stripe_res = LoginStripeResponse(
            product=plan,
            start_date=start_end_period.start_date,
            end_date=start_end_period.end_date
        )
        return LoginResponse(
            user=user,
            plan=stripe_res
        )