from fastapi import FastAPI
from dotenv import load_dotenv

from api.routers import router

load_dotenv()

app = FastAPI(title='AegisQ - Async Job Queue')

app.include_router(router)