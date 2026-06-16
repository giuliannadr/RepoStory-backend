from fastapi import APIRouter
from services.github_service import get_user_repos
from services.github_service import get_repo_commits
from services.github_service import get_repo_stats
from services.ai_service import generate_repo_story

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

@router.get("/user/{username}/{repo_name}/story")
def read_repo_story(username: str, repo_name: str):
    stats = get_repo_stats(username, repo_name)
    commits = get_repo_commits(username, repo_name)
    return generate_repo_story(stats, commits)