# Installation

Here's a short tutorial for installing the project locally.

## Installing requirements

You'll need:

- Python 3.11 or newer ([CPython](https://python.org) and [PyPy](https://www.pypy.org) are both supported platforms, others have not been tested but may work)
- uv (once Python is installed, install uv via `pip install uv`)

## Installing the project

Installing should be as simple as running `uv sync`. `uv` should create a new virtual environment, install all the dependencies it reads from [`uv.lock`](../uv.lock) (if it exists) or [`pyproject.toml`](../pyproject.toml), and once it's done everything should be good to go.
