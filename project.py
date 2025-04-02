from typing import Literal
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    base_url: str = 'https://stellarburgers.nomoreparties.site/'
    window_width: int = 1920
    window_height: int = 1080
