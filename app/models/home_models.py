from pydantic import BaseModel


class MessageHomeModel(BaseModel):
    message: str
