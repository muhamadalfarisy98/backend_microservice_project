from fastapi import FastAPI
from routes.educational_routes import router as educational_router

app = FastAPI()

#jalan server : uvicorn main:app --reload

app.include_router(educational_router)

