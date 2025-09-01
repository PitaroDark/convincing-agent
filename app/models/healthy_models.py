from pydantic import BaseModel


class MessageHealthyModel(BaseModel):
    message: str
    status: str
    version: str
