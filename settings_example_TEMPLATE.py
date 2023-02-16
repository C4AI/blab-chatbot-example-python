"""This module contains settings for the Example Bot client."""

from __future__ import annotations

from typing import Any


BLAB_CONNECTION_SETTINGS: dict[str, str | int] = {

    # address of the local HTTP server that the controller will connect to
    # (it should be "127.0.0.1" to accept only local connections from the controller)
    "BOT_HTTP_SERVER_HOSTNAME": "127.0.0.1",

    # port of the aforementioned server (any valid port)
    "BOT_HTTP_SERVER_PORT": 25229,

    # BLAB Controller address for WebSocket connections (it starts with ws:// or wss://)
    "BLAB_CONTROLLER_WS_URL": "ws://localhost:8000",

}

EXAMPLE_SETTINGS: dict[str, Any] = {

    # text sent to the user when a conversation starts
    'GREETING_TEXT': "Hey!",

}
