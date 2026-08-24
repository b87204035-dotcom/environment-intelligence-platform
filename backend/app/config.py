from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    database_url: str
    openai_api_key: str | None = None
    openai_model: str = "gpt-5-mini"
    source_snapshot_dir: str = "/data/snapshots"
    cors_origins: str = ""
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
settings = Settings()
