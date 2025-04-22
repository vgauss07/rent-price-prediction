"""
This module sets up the logger configuration.

It utilizes Pydantic's BaseSettings for configuration management,
allowing settings to be read from environment variables and a .env file
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from loguru import logger


class LoggerSettings(BaseSettings):
    """
    Logger Configuration settings for the application

    Attributes:
        log_level (str): Logging level for the application.
    """
    model_config = SettingsConfigDict(env_file='config/.env',
                                      env_file_encoding='utf-8',
                                      extra='ignore')
    log_level: str


def configure_logging(log_level: str) -> None:
    """
    configure the logging for the application

    Args:
        log_level (str): The log level to be set for the logger
    """

    # logger.remove() # to stop logger from displaying status in the console
    logger.add('logs/app.log',
               rotation='1 day',
               retention='2 days',
               compression='zip',
               level=log_level)


configure_logging(log_level=LoggerSettings().log_level)
