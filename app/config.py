import os
from dataclasses import dataclass

from dotenv import load_dotenv
from sqlalchemy import URL

load_dotenv()


@dataclass
class APIVersionConfig:
    v1: str = os.getenv("API_DEFAULT_PATH_V1")


@dataclass
class LoggerConfig:
    file_name: str = os.getenv("LOG_FILE_NAME")


@dataclass
class AuthConfig:
    access_token_expires: int = int(os.getenv("ACCESS_TOKEN_EXPIRES"))
    hash_password_algorithm: str = os.getenv("HASHED_PASSWORD_ALGORITHM")
    token_algorithm: str = os.getenv("TOKEN_ALGORITHM")
    secret_key: str = os.getenv("SECRET_KEY_FOR_TOKEN")
    reset_verify_token: str = os.getenv("RESET_VERIFY_TOKEN")


@dataclass
class DatabaseConfig:
    name: str = os.getenv("POSTGRES_DB")
    user: str = os.getenv("POSTGRES_USER")
    passwd: str = os.getenv("POSTGRES_PASSWORD")
    port: int = int(os.getenv("DB_PORT", 5432))
    host: str = os.getenv("DB_HOST", "db")

    database_system: str = os.getenv("DB_SYSTEM")
    driver: str = os.getenv("DB_DRIVER")

    debug: bool = bool(os.getenv("DEBUG"))

    def build_connection_str(self) -> str:
        return URL.create(
            drivername=f"{self.database_system}+{self.driver}",
            username=self.user,
            database=self.name,
            password=self.passwd,
            port=self.port,
            host=self.host,
        ).render_as_string(hide_password=False)


@dataclass
class Config:
    api_version = APIVersionConfig()
    db = DatabaseConfig()
    logger = LoggerConfig()
    auth = AuthConfig()


conf = Config()
