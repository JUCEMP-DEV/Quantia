from functools import lru_cache
from pathlib import Path

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(str(BACKEND_DIR / ".env"), str(BACKEND_DIR / ".env.local")),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    project_name: str = "Quantia Backend"
    api_v1_prefix: str = "/api"
    debug: bool = False

    supabase_url: str = Field(default="", alias="SUPABASE_URL")
    supabase_anon_key: str = Field(default="", alias="SUPABASE_ANON_KEY")
    supabase_service_role_key: str = Field(default="", alias="SUPABASE_SERVICE_ROLE_KEY")
    supabase_key: str = Field(default="", alias="SUPABASE_KEY")

    backend_cors_origins: list[str] = Field(
        default_factory=lambda: [
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            "https://quantia-dun.vercel.app",
            "https://quantia-git-main-jucemp-devs-projects.vercel.app",
            "https://quantia-p3tt1813g-jucemp-devs-projects.vercel.app",
        ]
    )

    @field_validator("backend_cors_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, value):  # noqa: ANN001
        if isinstance(value, list):
            return value
        if isinstance(value, str):
            value = value.strip()
            if not value:
                return []
            return [item.strip() for item in value.split(",") if item.strip()]
        return []

    @field_validator("debug", mode="before")
    @classmethod
    def parse_debug(cls, value):  # noqa: ANN001
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            normalized = value.strip().lower()
            if normalized in {"1", "true", "yes", "on", "debug", "dev"}:
                return True
            if normalized in {"0", "false", "no", "off", "release", "prod", "production", ""}:
                return False
        return False

    @property
    def supabase_admin_key(self) -> str:
        return self.supabase_service_role_key or self.supabase_key or self.supabase_anon_key


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
