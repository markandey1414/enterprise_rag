from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    PINECONE_API_KEY: str
    PINECONE_ENVIRONMENT: str
    DATABASE_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()