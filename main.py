from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.database.database import engine
from app.database.models import Base

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.posts import router as posts_router
from app.routers.like import router as like_router
from app.routers.comments import router as comments_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://127.0.0.1", 
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "null",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(posts_router)
app.include_router(like_router)
app.include_router(comments_router)


@app.on_event("startup")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("База данных инициализирована")
    
@app.on_event("shutdown")
async def setup_database():
    await engine.dispose()
    print("База данных закрыта")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)