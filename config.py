"""Application configuration module."""

from os import getenv, environ
from pathlib import Path  # python3 only

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)


class Config(object):
    """App base configuration."""

    SQLALCHEMY_DATABASE_URI = getenv(
        'DATABASE_URI',)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    """App production configuration."""

    pass


class DevelopmentConfig(Config):
    """App development configuration."""

    DEBUG = True


class TestingConfig(Config):
    """App testing configuration."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = getenv(
        'TEST_DATABASE_URI',)


config = {
    'development': DevelopmentConfig,
    'staging': ProductionConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
