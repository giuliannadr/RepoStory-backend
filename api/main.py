from fastapi import FastAPI
from services.github_service import get_user_info

app = FastAPI()
@app.get("/user/{username}")
def read_user(username: str):
    return get_user_info(username)