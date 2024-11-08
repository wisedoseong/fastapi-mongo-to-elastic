from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.infrastructure.config.database import db

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 시작 시 실행
    await db.connect()
    yield
    # 종료 시 실행
    await db.close()
    
app = FastAPI(lifespan=lifespan)

# API 라우터 등록
# app.include_router(...)