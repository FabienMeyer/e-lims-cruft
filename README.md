![CI](https://github.com/FabienMeyer/e-lims-cruft/actions/workflows/ci.yml/badge.svg)
![Codecov](https://img.shields.io/codecov/c/github/FabienMeyer/e-lims-cruft)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=FabienMeyer_e-lims&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=FabienMeyer_e-lims-cruft)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=FabienMeyer_e-lims&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=FabienMeyer_e-lims-cruft)
![PyPI](https://img.shields.io/pypi/v/e-lims-cruft.svg)
[![Documentation](https://img.shields.io/badge/GitHub-Pages-blue)](https://fabienmeyer.github.io/e-lims-cruft/)
![License](https://img.shields.io/github/license/FabienMeyer/e-lims-cruft)

A brief description of what e-lims-cruft does.

# Usage

## 1. Install template

``` bash
pip install --user cruft
cruft create https://github.com/FabienMeyer/e-lims-cruft.git
```

## 2. Configure Github

- Go to the Github repository > Settings > pages.
- In "Build and Deployment", select "Deploy from a branch" source

## 3. Configure codecov

- Go to [Codecov](https://app.codecov.io)
- Select "Configure" for your new project
- Follow the configuration steps for a GitHub CI

## 4. Congigure sonarcloud

- Go to [SonarCloud](https://sonarcloud.io/)
- Select "Analyze new projects"
- Follow the configuration steps for a GitHub CI

## 5. Configure Pypi

- Go to [Pypi](https://pypi.org/manage/projects/)
- Go to the Github repository > Settings > Actions secrets and variables.
- In Actions, create a repository secret with the name PYPI_TOKEN.

# Installation

## Install Python 3.12
If you haven’t installed Python 3.12 yet, you can download it from the [official Python website](https://www.python.org/downloads/).

## Install Poetry
If you haven’t installed Poetry yet, you can do so by following the [official Poetry installation guide](https://python-poetry.org/docs/#installation).

## Clone
Clone the repository to your local machine using.

``` bash
git clone https://github.com/FabienMeyer/e-lims-cruft.git
cd e-lims-cruft
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