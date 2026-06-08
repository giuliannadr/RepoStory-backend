from fastapi import APIRouter
from services.github_service import get_user_repos
from services.github_service import get_repo_commits
from services.github_service import get_repo_stats

router = APIRouter()
@router.get("/user/{username}/repos")
def read_user_repos(username: str):
    return get_user_repos(username)

@router.get("/user/{username}/{repo_name}/commits")
def read_repo_commits(username: str, repo_name: str):
  return get_repo_commits(username, repo_name)

@router.get("/user/{username}/{repo_name}/stats")
def read_repo_stats(username: str, repo_name: str):  
   return get_repo_stats(username, repo_name)