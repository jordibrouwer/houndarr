"""FastAPI application factory."""

from __future__ import annotations

from fastapi import FastAPI

from houndarr import __version__
from houndarr.config import get_settings


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()

    app = FastAPI(
        title="Houndarr",
        description="A focused, self-hosted companion for Sonarr and Radarr.",
        version=__version__,
        docs_url="/api/docs" if settings.dev else None,
        redoc_url=None,
    )

    return app
