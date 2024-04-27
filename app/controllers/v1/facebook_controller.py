


from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from app.usecases.facebook import FacebookUsecase


facebook_router = APIRouter(
    tags=["Facebook Services"],
    prefix="/v1/facebook",
    responses={
        404:{"discription": "Not Found a URL or this URL is invalid"}
    },
)

@facebook_router.get("/token")
async def get_facebook_token(
    firebase_id: str,
    facebbokUsecase: Annotated[FacebookUsecase, Depends()]
):
    token = facebbokUsecase.get_facebook_token_by_user_id(firebase_id)
    if token is None:
        raise HTTPException(status_code=404, detail="Token Not Found")
    print(token)
    return {"token": token}