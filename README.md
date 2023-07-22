# Language App Backend

## Installation

By installing the project as a package you can import the modules within the package in other Python modules by using:

> `import langapp`

To install the project just type
> `pip install .`

in your command line tool. The `.` stands for the current directory. Thus, you must be in the project root directory.

## Developer Instructions

Install [poetry](https://python-poetry.org/docs/#installation).

Install in "develop" or "editable" mode (change directory to the root folder with the `pyproject.toml` in it and execute via the anaconda prompt for example):

> `poetry install`

It puts a link (actually *.pth files) into the python installation to your code, so that your package is installed, but any changes will immediately take effect.
Furthermore, it installs some useful libraries for developing, which are defined in the `pyproject.toml` file.

In order to test the package execute

> `pytest --pyargs langapp`

## Rationale Project Structure

- The `tests` folder needs a `__init__.py` file, otherwise VS Code can not execute the tests.
