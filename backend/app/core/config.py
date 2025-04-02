import secrets
import warnings
from typing import Annotated, Any, Literal

from pydantic import (
    AnyUrl,
    BeforeValidator,
    PostgresDsn,
    computed_field,
    model_validator,
    Field,
)
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Self


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # Use top level .env file (one level above ./backend/)
        env_file="../.env",
        env_ignore_empty=True,
        extra="ignore",
    )
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    ENVIRONMENT: Literal["local", "staging", "production"] = "local"

    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []

    @computed_field  # type: ignore[prop-decorator]
    @property
    def all_cors_origins(self) -> list[str]:
        return (
            [
                str(origin).rstrip("/") for origin in self.BACKEND_CORS_ORIGINS
            ] +
            [
                self.FRONTEND_HOST
            ]
        )

    PROJECT_NAME: str = Field(
        default="TestForkTech",
        description="Название проекта для документации"
    )


    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  
    
    DB_USER: str = ""
    DB_PASSWORD: str = ""
    DB_HOST: str = ""
    DB_PORT: str = ""
    DB_NAME: str = ""
    
    TRON_URI: str = ""
    TRON_API_KEY: str = ""

    @computed_field  # type: ignore[prop-decorator]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        SQLALCHEMY_DATABASE_URL: str =  "".join([
            "postgresql+asyncpg://",
            self.DB_USER+":",
            self.DB_PASSWORD+"@",
            self.DB_HOST + (':' + self.DB_PORT if self.DB_PORT is not None else '' ) + "/",
            self.DB_NAME + '?',
        ])
        return SQLALCHEMY_DATABASE_URL

    FIRST_SUPERUSER_PASSWORD: str = Field(
        default="changeth",
        description="Пароль первого суперпользователя",
        min_length=8
    )

    def _check_default_secret(self, var_name: str, value: str | None) -> None:
        if value == "changethis":
            message = (
                f'The value of {var_name} is "changethis", '
                "for security, please change it, at least for deployments."
            )
            if self.ENVIRONMENT == "local":
                warnings.warn(message, stacklevel=1)
            else:
                raise ValueError(message)

    @model_validator(mode="after")
    def _enforce_non_default_secrets(self) -> Self:
        self._check_default_secret("SECRET_KEY", self.SECRET_KEY)
        self._check_default_secret(
            "FIRST_SUPERUSER_PASSWORD", self.FIRST_SUPERUSER_PASSWORD
        )

        return self


settings = Settings()
