from fastapi import APIRouter
from services.github_service import get_user_info

router = APIRouter()
@router.get("/user/{username}")
def read_user(username: str):
    return get_user_info(username)