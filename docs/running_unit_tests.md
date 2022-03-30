# Running unit tests

The project's unit tests have been designed to be deceptively simple to run. They run automatically whenever code is pushed to GitHub (via GitHub Actions, using the [`unit_tests.yml` script](../.github/workflows/unit_tests.yml)), and they can be run manually via Poetry.

## Unit tests in GitHub Actions

When a new push is made to GitHub, GitHub Actions runs all the workflows in the project's `.github` directory that have the right triggers. The unit test script uses Tox to create several virtual test environments to run unit tests in parallel on multiple Python versions across all major platforms - Windows, Linux (Ubuntu), and Mac OS. This project in particular is tested using Python versions from 3.6 to 3.10, and an extra test run is made using the PyPy implementation on Ubuntu. All tests must pass on every platform, and on every Python version.

Additionally, while noot unit testing, two linter workflows for Pylint and Flake8 are also run in parallel to the unit tests to ensure only the highest quality of code makes it into production. Both of them are configured in [`pyproject.toml`](../pyproject.toml), as is Pytest, the test suite used by the project.

## Unit tests locally

The project's unit tests can be run via Poetry, which takes care of the unit test configuration and other things. To run the unit tests, the project must first be installed - more on that [here](installation.md). Once the project has been installed, the unit tests can be run by first activating the project's virtual environment (`poetry shell`), and then telling Poetry to run the unit tests (`poetry run pytest`). In the same vein, linters can be run locally via `poetry run pflake8` and `poetry run pylint unit_testing`.

On Linux distros and Mac OS, you may alternatively use the provided [`Makefile`](../Makefile) and simply run `make all` to run everything. The shell commands it uses are not compatible with Windows, unless specifically using a Bash terminal.

## Coverage reports

The unit tests are configured to always produce coverage reports when successful, they can be found in the [`reports`](../tests/reports/) directory. It should contain both a HTML version as well as an XML report, they should be equivalent in terms of the information they contain.
