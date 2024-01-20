from fastapi import APIRouter
from module.facebook.services.page import get_facebook_page_data

router = APIRouter(
    tags=["Facebook Service"],
    responses={404: {"description": "Not found in"}},
)

@router.get("/get_page_date", status_code=200)
def get_page_data():
    """
    this function try to get data from facebook page
    """
    data = get_facebook_page_data()
    return data