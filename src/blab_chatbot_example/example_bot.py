import json
import uuid
from threading import Thread, Timer

import websocket  # type: ignore

from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def bot():

    bot_participant_id = request.json["bot_participant_id"]

    def on_message(ws_app, m):
        contents = json.loads(m)
        if "message" in contents:
            message = contents["message"]
            # ignore system messages and our own messages
            if message["type"] == "S" or message["sender_id"] == bot_participant_id:
                return
            # generate answer
            text = f"YOU SAID: «{message['text']}»"
            msg_type = "T"
            local_id = str(uuid.uuid4()).replace("-", "")
            answer = {
                "type": msg_type,
                "text": text,
                "local_id": local_id,
            }
            # send answer after delay
            delay = 1
            Timer(
                delay,
                lambda: ws_app.send(json.dumps(answer)),
            ).start()

    def on_open(ws_app):
        # generate greeting message
        text = "HELLO!"
        msg_type = "T"
        local_id = str(uuid.uuid4()).replace("-", "")
        greeting = {
            "type": msg_type,
            "text": text,
            "local_id": local_id,
        }
        # send greeting message
        ws_app.send(json.dumps(greeting))

    ws_url = "ws://localhost:8000/ws/chat/" + request.json["conversation_id"] + "/"
    ws = websocket.WebSocketApp(
        ws_url,
        on_message=on_message,
        cookie="sessionid=" + request.json["session"],
        on_open=on_open,
    )
    Thread(target=ws.run_forever).start()
    return ""


def start():
    app.run(host="127.0.0.1", port=25226)
