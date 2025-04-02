from fastapi import APIRouter
from app.endpoints.views import adress, queries


api_router = APIRouter()
api_router.include_router(adress.router)
api_router.include_router(queries.router)


