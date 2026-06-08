from fastapi import APIRouter
from services.github_service import get_user_repos

router = APIRouter()
@router.get("/user/{username}/repos")
def read_user_repos(username: str):
    return get_user_repos(username)