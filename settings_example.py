"""This module contains settings for Haystack."""

from __future__ import annotations

BLAB_CONNECTION_SETTINGS: dict[str, str | int] = {
    "BOT_HTTP_SERVER_HOSTNAME": "localhost",
    "BOT_HTTP_SERVER_PORT": 25229,
    "BLAB_CONTROLLER_WS_URL": "ws://localhost:8000",
}