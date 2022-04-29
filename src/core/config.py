from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_PREFIX = '/v1'


settings = Settings()
