from fastapi import FastAPI
from api.routes import users
from api.routes import repos
app = FastAPI()
app.include_router(users.router, prefix="/api")
app.include_router(repos.router, prefix="/api")