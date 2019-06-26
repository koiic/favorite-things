"""Application configuration module."""
import sys
from os import getenv
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
    FLASK_ENV = getenv('FLASK_ENV', 'production')
    JWT_SECRET_KEY = getenv('JWT_SECRET_KEY_STAGING')


class ProductionConfig(Config):
    """App production configuration."""
    JWT_SECRET_KEY = getenv('JWT_SECRET_KEY_PRODUCTION')

    pass


class DevelopmentConfig(Config):
    """App development configuration."""

    DEBUG = True


class TestingConfig(Config):
    """App testing configuration."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = getenv(
        'TEST_DATABASE_URI',)
    API_BASE_URL = getenv('API_BASE_URL', '/api/v1')
    JWT_SECRET_KEY = getenv('JWT_SECRET_KEY_TEST')


config = {
    'development': DevelopmentConfig,
    'staging': ProductionConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

AppConfig = TestingConfig if 'pytest' in sys.modules else config.get(getenv('FlASK_ENV'), 'development')