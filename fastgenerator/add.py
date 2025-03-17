from pathlib import Path

import typer

from .module import Module

add = typer.Typer(help="Add commands")


@add.command(name="module")
def add_module(
    name: str,
    file: Path = typer.Option(..., "--file", "-f", help="File"),
) -> None:
    """Command to generate a model in the app."""
    Module.add(file, name)
