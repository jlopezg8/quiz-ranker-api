from typing import Literal, Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    environment: Literal['dev', 'prod'] = 'dev'
    deta_project_key: Optional[str]


settings = Settings(
    _env_file='.env'
)
