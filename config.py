from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class DBSettings(BaseSettings):
    MODE: str
    DB_DRIVER: str
    DB_USER: Optional[str] = None
    DB_PASSWORD: Optional[str] = None
    DB_HOST: Optional[str] = None
    DB_PORT: Optional[str] = None
    DB_NAME: str

    @property
    def URL(self):
        if self.MODE == 'DEV':
            return (
                f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@'
                f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
            )
        else:
            raise ValueError('Нет значения MODE для сервера.')

    class ConfigDict:
        env_file = '.env'
