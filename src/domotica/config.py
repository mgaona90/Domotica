from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "Domotica"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    app_debug: bool = False


settings = Settings()
