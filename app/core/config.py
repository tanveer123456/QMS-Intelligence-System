from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application Settings
    """

    # -------------------------
    # Application
    # -------------------------
    app_name: str
    app_version: str
    environment: str
    debug: bool

    # -------------------------
    # Server
    # -------------------------
    host: str
    port: int

    # -------------------------
    # Database
    # -------------------------
    database_url: str

    # -------------------------
    # LLM
    # -------------------------
    llm_provider: str
    perplexity_api_key: str

    # -------------------------
    # Security
    # -------------------------
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    # -------------------------
    # Logging
    # -------------------------
    log_level: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings instance.
    """
    return Settings()


settings = get_settings()