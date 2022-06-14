#!/usr/bin/env python3

from pathlib import Path
from sys import path

here = Path(__file__).parent
path.insert(0, str(here / "src"))

from blab_chatbot_example.example_bot import start  # noqa: E402

start()
