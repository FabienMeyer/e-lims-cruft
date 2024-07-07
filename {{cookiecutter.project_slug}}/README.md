![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }})
![CI](https://github.com/{{ cookiecutter.project_git_repository }}/actions/workflows/ci.yml/badge.svg)
![Codecov](https://img.shields.io/codecov/c/github/{{ cookiecutter.project_git_repository }})
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project={{ cookiecutter.sonarcloud }}&metric=security_rating)](https://sonarcloud.io/summary/new_code?id={{ cookiecutter.sonarcloud }})
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project={{ cookiecutter.sonarcloud }}&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id={{ cookiecutter.sonarcloud }})
![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_name }}.svg)
[![Documentation](https://img.shields.io/badge/GitHub-Pages-blue)](https://fabienmeyer.github.io/{{ cookiecutter.project_name }}/)
![License](https://img.shields.io/github/license/{{ cookiecutter.project_git_repository }})

A brief description of what {{ cookiecutter.project_name }} does.

# Installation

## Install Python 3.12
If you haven’t installed Python 3.12 yet, you can download it from the [official Python website](https://www.python.org/downloads/).

## Install Poetry
If you haven’t installed Poetry yet, you can do so by following the [official Poetry installation guide](https://python-poetry.org/docs/#installation).

## Clone
Clone the repository to your local machine using.

``` bash
git clone https://github.com/{{ cookiecutter.project_git_repository }}.git
cd {{ cookiecutter.project_name }}
```

## Configure Poetry
Configure Poetry to use a specific Python version and create a virtual environment in the project directory.
   
   ``` bash
   poetry env use "path to python 3.11 or 3.12"
   poetry config virtualenvs.in-project true
   ```

## Install dependencies
Navigate to the project directory and install the necessary dependencies using Poetry.

``` bash
poetry install
```

## Optional dependencies
If you are planning to write documentation, run quality checks, or run tests, you may need to install additional dependencies. You can do so by running.

``` bash
poetry install --with dev,doc,tests
```

## Activate the virtual environment

``` bash
      poetry shell
```