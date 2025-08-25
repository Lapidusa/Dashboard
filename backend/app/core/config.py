from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Settings(BaseSettings):
  DATABASE_URL: str

  class Config:
    env_file = "../../.env"
    env_file_encoding = "utf-8"
    extra = "allow"

settings = Settings()
