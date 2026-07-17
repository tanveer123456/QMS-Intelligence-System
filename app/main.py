from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.logger import logger
from app.api.v1.endpoints.auth import router as auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs when the application starts
    """

    logger.info("=" * 60)
    logger.info(f"{settings.app_name} Starting...")
    logger.info(f"Environment : {settings.environment}")
    logger.info("=" * 60)

    yield

    logger.info("=" * 60)
    logger.info("Application Shutdown")
    logger.info("=" * 60)


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Enterprise Quality Intelligence Platform",
    lifespan=lifespan,
)

app.include_router(
    auth_router,
    prefix="/api/v1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "status": "Running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "environment": settings.environment,
    }