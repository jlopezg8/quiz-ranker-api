from typing import Literal

from pydantic import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    environment: Literal['dev', 'prod'] = 'dev'


settings = Settings(
    _env_file='.env'
)
