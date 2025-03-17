from pathlib import Path

import typer

from .app import App
from .module import Module

app = typer.Typer(help="Create commands")


@app.command(name="app")
def create_app(file: Path = typer.Option(..., "--file", "-f", help="File")) -> None:
    """Command to generate app template."""
    App.create(file)


@app.command(name="module")
def create_module(
    name: str,
    file: Path = typer.Option(..., "--file", "-f", help="File"),
) -> None:
    """Command to generate a model in the app."""
    Module.create(file, name)
