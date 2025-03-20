import typer

from fastgenerator import const


def iscontinue() -> None:
    confirm = typer.prompt(const.TEXTS["continue"], default=const.TEXT_YES).lower()
    if confirm == const.TEXT_NO:
        raise typer.Exit()
