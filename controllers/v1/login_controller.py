from typing import Annotated

from fastapi import (
    Depends, 
    APIRouter, 
    Header, 
    HTTPException
)

from schemas.pydantic.loginSchema import (
    LoginResponse, 
    LoginRequest,
    LoginStripeResponse
)

from schemas.pydantic.userSchema import (
    UserUpdateRequest
)

from services.firebase_service import (
    FirebaseService
)
from services.stripe_service import StripeService

from middlewares.authentication import get_current_user

from usecases.users import UsersUsecase
from usecases.plans import PlanUsecases

from model.users.users_model import Users



loginRouter = APIRouter(
    tags=["User Services"],
    prefix="/v1/login",
    responses={
        404:{"discription": "Not Found a URL or this URL is invalid"}
    },
)

@loginRouter.post("/", status_code=200, response_model=LoginResponse)
def login(
    request: LoginRequest,
    userUsecases: Annotated[UsersUsecase, Depends()] ,
    planUsecases: Annotated[PlanUsecases, Depends()] ,
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
    
    # get a plan from stripe service
    
    user = userUsecases.get(user.id)
    if(user.stripe_id is None):
        # incase user don't have a stripe id
        plan = planUsecases.get_by_id(user.plan_id)
        stripe_res = LoginStripeResponse(
            product=plan,
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