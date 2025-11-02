# config.py

import os
from dotenv import load_dotenv
from datetime import timedelta

# Load environment variables from a .env file (if present)
load_dotenv()

class Config:
    """Base configuration."""
    # Secret key for Flask (or whichever backend)
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-should-change-this')

    # Weather API configuration
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', None)
    WEATHER_API_BASE_URL = os.getenv(
        'WEATHER_API_BASE_URL',
        'https://api.openweathermap.org/data/2.5'
    )

    # Application settings
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
    TESTING = os.getenv('TESTING', 'False').lower() in ('true', '1', 't')

    # Token / session configuration (if you have auth)
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', SECRET_KEY)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        seconds=int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES_SECONDS', 3600))
    )

    # Rate limiting / caching settings
    CACHE_TYPE = os.getenv('CACHE_TYPE', 'simple')  # e.g., “redis”, “memcached”
    CACHE_DEFAULT_TIMEOUT = int(os.getenv('CACHE_DEFAULT_TIMEOUT', 300))

    # Logging / other configs
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

    @staticmethod
    def init_app(app):
        """Initialize application with configuration (if needed)."""
        # e.g., setup logging handlers, things that rely on app context
        pass


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
    # If you use a local caching / redis root
    CACHE_REDIS_URL = os.getenv('CACHE_REDIS_URL', 'redis://localhost:6379/0')


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    # Example: use a real Redis/Memcached instance
    CACHE_REDIS_URL = os.getenv('CACHE_REDIS_URL', None)


# Dictionary to choose config class by environment
config_by_name = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,
    'default': DevelopmentConfig
}

