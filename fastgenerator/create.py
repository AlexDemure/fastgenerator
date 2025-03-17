from pathlib import Path

import typer

from .app import App

create = typer.Typer(help="Create commands")


@create.command(name="app")
def create_app(file: Path = typer.Option(..., "--file", "-f", help="File")) -> None:
    """Command to generate app template."""
    App.create(file)
