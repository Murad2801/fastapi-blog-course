from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)


@app.get("/")
def hello():
    return {"msg": "Hello FastAPI"}


@app.get("/about")      # This is for /about
def about():
    return {"info": "About this API"}
