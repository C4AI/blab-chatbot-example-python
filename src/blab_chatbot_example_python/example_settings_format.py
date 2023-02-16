from typing import Protocol, TypedDict, runtime_checkable

from blab_chatbot_bot_client.settings_format import BlabBotClientSettings


class ExampleSettings(TypedDict):

    GREETING_TEXT: str


@runtime_checkable
class BlabExampleClientSettings(BlabBotClientSettings, Protocol):
    BLAB_CONNECTION_SETTINGS: ExampleSettings
    EXAMPLE_SETTINGS: ExampleSettings
