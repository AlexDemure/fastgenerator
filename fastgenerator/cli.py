import typer

from .add import add
from .create import create

app = typer.Typer(help="Generator")

app.add_typer(create, name="create")
app.add_typer(add, name="add")

if __name__ == "__main__":
    app()
