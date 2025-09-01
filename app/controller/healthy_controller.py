from fastapi import APIRouter
from models.healthy_models import MessageHealthyModel
from settings.config import settings

router = APIRouter(prefix="", tags=["Healthy"])


@router.get("/health")
async def healthy() -> MessageHealthyModel:
    return MessageHealthyModel(message="Convincing Agent API is running.", status="healthy", version=settings.API_VERSION)
