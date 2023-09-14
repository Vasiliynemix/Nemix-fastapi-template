import os
from dataclasses import dataclass

from dotenv import load_dotenv
from sqlalchemy import URL

load_dotenv()


@dataclass
class LoggingConfig:
    file_name: str = os.getenv('LOG_FILE_NAME')


@dataclass
class DatabaseConfig:
    name: str | None = os.getenv("DB_NAME")
    user: str | None = os.getenv("DB_USER")
    passwd: str | None = os.getenv("DB_PASSWORD")
    port: int = int(os.getenv("DB_PORT"))
    host: str = os.getenv("DB_HOST")

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
    db = DatabaseConfig()
    logger = LoggingConfig()


conf = Config()
