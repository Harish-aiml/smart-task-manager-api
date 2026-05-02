from fastapi import FastAPI
from database import engine
from models import Base
from routers.tasks import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Professional FastAPI project running"}