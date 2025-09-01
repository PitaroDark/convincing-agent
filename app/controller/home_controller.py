from fastapi import APIRouter
from models.home_models import MessageHomeModel

router = APIRouter(prefix="", tags=["Home"])


@router.get("/")
async def home() -> MessageHomeModel:
    return MessageHomeModel(message="Convincing Agent API is running.")
