# ./app/routes/health.py

from fastapi import APIRouter, Request
from app.utils.logger import logger

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/")
def health_check(request: Request):
    logger.info(f"Health check accessed from {request.client.host} via {request.method}")
    return {"status": "ok"}
