from fastapi import FastAPI
from src.api.v1.api import api_router as api_v1
from src.core.config import settings

app = FastAPI()

app.include_router(api_v1, prefix=settings.API_V1_PREFIX)
