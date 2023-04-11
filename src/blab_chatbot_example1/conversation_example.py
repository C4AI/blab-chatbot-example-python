from overrides import overrides

from blab_chatbot_bot_client.conversation_websocket import (
    WebSocketBotClientConversation,
)
from blab_chatbot_bot_client.data_structures import (
    OutgoingMessage,
    MessageType,
    Message,
)

from blab_chatbot_example1.example_settings_format import BlabExampleClientSettings


class ExampleWebSocketBotClientConversation(WebSocketBotClientConversation):

    settings: BlabExampleClientSettings

    @overrides
    def on_connect(self):
        greeting_text = self.settings.EXAMPLE_SETTINGS['GREETING_TEXT']
        greeting = OutgoingMessage(
            type=MessageType.TEXT,
            text=greeting_text,
            local_id=self.generate_local_id(),
        )
        self.enqueue_message(greeting)

    @overrides
    def on_receive_message(self, message: Message) -> None:
        if message.sent_by_human and message.type == MessageType.TEXT:
            for answer in self.generate_answer(message):
                self.enqueue_message(answer)

    @overrides
    def generate_answer(self, message: Message) -> list[OutgoingMessage]:
        answer = OutgoingMessage(
            type=MessageType.TEXT,
            text="Pernambuco",
            local_id=self.generate_local_id(),
            quoted_message_id=message.id,
        )
        return [answer]
