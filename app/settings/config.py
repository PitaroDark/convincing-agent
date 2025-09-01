from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # SELF INFORMATION API
    API_NAME: str = "Convincing Agent API"
    API_DESCRIPTION: str = "A chatbot API that holds a debate and attempts to convince the other side."
    API_VERSION: str = "0.1.0"
    API_PORT: int = 8000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
