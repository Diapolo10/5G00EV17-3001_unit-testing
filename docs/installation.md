# Installation

Here's a short tutorial for installing the project locally.

## Installing requirements

You'll need:

- Python 3.6 or newer ([CPython](https://python.org) and [PyPy](https://www.pypy.org) are both supported platforms, others have not been tested but may work)
- Poetry (once Python is installed, install Poetry via `pip install poetry`)

## Installing the project

Installing should be as simple as running `poetry install`; depending on your system you may need to specify `python3 -m poetry install` or `py -m poetry install`, but the end result is the same. Poetry should create a new virtual environment, install all the dependencies it reads from [`poetry.lock`](../poetry.lock) (if it exists) or [`pyproject.toml`](../pyproject.toml), and once it's done everything should be good to go.

If you run into issues during installation, try running `poetry update` to update `poetry.lock` with newer dependencies and try installing again.

The virtual environment can be activated as simply as running `poetry shell`.
