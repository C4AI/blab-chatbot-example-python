"""This module contains settings for the Example Bot client."""

from __future__ import annotations

from typing import Any


BLAB_CONNECTION_SETTINGS: dict[str, str | int] = {

    # Address of the local HTTP server that the controller will connect to:
    "BOT_HTTP_SERVER_HOSTNAME": "127.0.0.1",

    # Port of the aforementioned server:
    "BOT_HTTP_SERVER_PORT": 25229,

    # BLAB Controller address for WebSocket connections:
    "BLAB_CONTROLLER_WS_URL": "ws://localhost:8000",

}

EXAMPLE_SETTINGS: dict[str, Any] = {

    # Text sent to the user when a conversation starts:
    'GREETING_TEXT': "Hey!",

}
