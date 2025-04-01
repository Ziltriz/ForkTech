from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


from app.db.session import engine
from app.db.base import Base
from app.endpoints.router import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://autofill.yandex.ru", "https://oauth.yandex.ru"],
    allow_methods=["*"]
)
app.include_router(api_router)



