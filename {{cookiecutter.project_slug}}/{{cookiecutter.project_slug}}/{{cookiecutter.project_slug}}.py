"""{{ cookiecutter.project_name }} main."""


def hello(name: str) -> str:
    """Say hello.

    >>> hello('{{ cookiecutter.project_name }}')
    'Hello {{ cookiecutter.project_name }}!'
    """
    return f"Hello {name}!"
