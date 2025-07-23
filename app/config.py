import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    TOP_K: int = int(os.getenv("TOP_K", "3"))

settings = Settings()