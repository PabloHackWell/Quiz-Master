from fastapi import FastAPI
from database import engine
import models
from routes import router

app = FastAPI(title="Quiz API")

models.Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Quiz Backend Running"}