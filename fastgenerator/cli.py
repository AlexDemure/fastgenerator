import typer

from .create import app as create_app

app = typer.Typer(help="Generator")

app.add_typer(create_app, name="create")

if __name__ == "__main__":
    app()
