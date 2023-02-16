# BLAB Chatbot Example (Python)

This repository contains a trivial implementation example of a chatbot
that can be integrated with [BLAB Controller](../../../blab-controller).
See [instructions](../../../blab-controller/ADDING_BOTS.md).

### Installation

- Clone or download this repository.

- In the directory that contains this *README.md* file, create a copy of the file `settings_example_TEMPLATE.py`
  and name it `settings_example.py`.

- Edit the file `settings_example.py` as needed, following the instructions in the file.

- Install [Poetry](https://python-poetry.org/) (version 1.2 or newer):

  ```shell
  curl -sSL https://install.python-poetry.org | python3 -
  ```
  If *~/.local/bin* is not in `PATH`, add it as suggested by the output of Poetry installer.

- In the root directory of the project (which contains this _README.md_ file),
  run Poetry to install the dependencies in a new virtual environment (_.venv_):

  ```shell
  POETRY_VIRTUALENVS_IN_PROJECT=true poetry install
  ```

- To open an interactive demo that answers questions (in this example, messages are echoed), run:

  ```shell
  poetry run python run.py answer
  ```
  

  

### Integration with BLAB Controller

- Open your controller settings file (`dev.py` or `prod.py`) and update
  the `CHAT_INSTALLED_BOTS` dictionary to include the Example Bot settings:

```python
CHAT_INSTALLED_BOTS.update({
    "Example": websocket_external_bot(url="http://localhost:25220"),
})
```


- To start the server that will interact with BLAB Controller, run:

  ```shell
  poetry run python run.py startserver
  ```
