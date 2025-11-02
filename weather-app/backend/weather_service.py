# weather_service.py
"""
Weather service module for fetching current conditions and forecast data.

- Supports OpenWeatherMap-compatible endpoints by default.
- Reads API key and base URL from config.Config or environment variables.
- Provides helpers to query by city or lat/lon and returns normalized payloads
  that are easy to use in a frontend.

Usage:
    svc = WeatherService()  # uses config.Config values
    now = svc.get_current_by_city("Orlando,US", units="imperial")
    fc  = svc.get_forecast_by_city("Orlando,US", units="imperial", hours=24)

If you use a different provider, ensure your BASE_URL points to endpoints with
similar query parameters (q, lat, lon, appid, units, lang) or adjust _request().
"""

from __future__ import annotations

import os
from typing import Any, Dict, List, Optional, Tuple, Union
from datetime import datetime, timedelta, timezone

import requests

try:
    # Prefer your repo's config module if available
    from config import Config  # type: ignore
except Exception:
    # Fallback to env vars to avoid hard failure during local scripts/tests
    class _FallbackConfig:
        WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
        WEATHER_API_BASE_URL = os.getenv(
            "WEATHER_API_BASE_URL", "https://api.openweathermap.org/data/2.5"
        )
    Config = _FallbackConfig()  # type: ignore


# ------------------------- Exceptions ------------------------- #

class WeatherServiceError(Exception):
    """Base error for weather service."""


class WeatherAuthError(WeatherServiceError):
    """Raised when API key or auth is invalid/missing."""


class WeatherNotFound(WeatherServiceError):
    """Raised when a requested location cannot be found."""


class WeatherRateLimited(WeatherServiceError):
    """Raised when provider rate limits the client."""


class WeatherUpstreamError(WeatherServiceError):
    """Raised for general upstream/provider errors."""


# ------------------------- Service ------------------------- #

class WeatherService:
    """
    Thin client around a weather API (OpenWeather-compatible).

    Parameters
    ----------
    api_key : str | None
        API key for the provider. If None, reads from Config/ENV.
    base_url : str | None
        Base API URL. Defaults to Config/ENV or OpenWeather's v2.5.
    session : requests.Session | None
        Optional shared session (helps with connection pooling).
    default_units : str
        'standard' | 'metric' | 'imperial'. Defaults to 'metric'.
    default_lang : str
        Response language. Defaults to 'en'.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        session: Optional[requests.Session] = None,
        default_units: str = "metric",
        default_lang: str = "en",
    ) -> None:
        self.api_key = api_key or getattr(Config, "WEATHER_API_KEY", None)
        self.base_url = (base_url or getattr(Config, "WEATHER_API_BASE_URL", None)
                         or "https://api.openweathermap.org/data/2.5")
        self.session = session or requests.Session()
        self.default_units = default_units
        self.default_lang = default_lang

        if not self.api_key:
            raise WeatherAuthError(
                "WEATHER_API_KEY is missing. Set it in your environment or config.py."
            )

    # --------------------- Public API: Current --------------------- #

    def get_current_by_city(
        self,
        city_query: str,
        units: Optional[str] = None,
        lang: Optional[str] = None,
        timeout: float = 10.0,
    ) -> Dict[str, Any]:
        """
        Fetch current conditions by city string, e.g., "Orlando,US" or "Paris,FR".
        """
        params = {
            "q": city_query,
            "appid": self.api_key,
            "units": units or self.default_units,
            "lang": lang or self.default_lang,
        }
        raw = self._request("/weather", params=params, timeout=timeout)
        return self._normalize_current(raw)

    def get_current_by_coords(
        self,
        lat: Union[float, str],
        lon: Union[float, str],
        units: Optional[str] = None,
        lang: Optional[str] = None,
        timeout: float = 10.0,
    ) -> Dict[str, Any]:
        """
        Fetch current conditions by geographic coordinates.
        """
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": units or self.default_units,
            "lang": lang or self.default_lang,
        }
        raw = self._request("/weather", params=params, timeout=timeout)
        return self._normalize_current(raw)

    # --------------------- Public API: Forecast --------------------- #

    def get_forecast_by_city(
        self,
        city_query: str,
        units: Optional[str] = None,
        lang: Optional[str] = None,
        hours: int = 24,
        timeout: float =

