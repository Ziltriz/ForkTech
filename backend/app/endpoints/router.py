from fastapi import APIRouter
from app.endpoints.views import adress 


api_router = APIRouter()
api_router.include_router(adress.router)


