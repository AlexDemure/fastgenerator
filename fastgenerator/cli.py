from pathlib import Path
from urllib.parse import urlparse

import typer

from fastgenerator import inputs
from fastgenerator import parsers
from fastgenerator.const import files
from fastgenerator.const import syntax
from fastgenerator.const import texts
from fastgenerator.os import File
from fastgenerator.os import Folder
from fastgenerator.utils import paths
from fastgenerator.utils import prints
from fastgenerator.utils import render

app = typer.Typer(help="Fastgenerator")


@app.command()
def generate(file: str = typer.Option(..., "-f", "--file", help="Path or link to configuration file")) -> None:
    if urlparse(file).scheme in ("http", "https"):
        file = File.download(url=file, extension=files.TOML)
    else:
        file = Path(file)

    variables = parsers.getvariables(file)

    context = inputs.getcontext(keys=list(variables))

    if context:
        confirm = typer.prompt(texts.SPEECHES["continue"], default=texts.YES).lower()
        if confirm == texts.NO:
            raise typer.Exit()

    config = File.toml(file)

    workdir = paths.define(config.get(syntax.WORKDIR, ""))

    before = paths.tree(workdir)

    modified = set()

    _folders = config.get(syntax.FOLDERS, [])
    _files = config.get(syntax.FILES, [])
    _exclude = set(config.get(syntax.EXCLUDE, []))

    for _folder in _folders:
        _path = workdir / render.loadenv(_folder, context)
        _pyfile = _path / files.INIT

        Folder.create(_path)

        if str(_pyfile.relative_to(workdir)) not in _exclude:
            File.create(_pyfile)

    for _file in _files:
        _path = workdir / render.loadenv(_file[syntax.FILE_PATH], context)
        _content = render.loadenv(_file[syntax.FILE_CONTENT], context)
        _mode = _file.get(syntax.FILE_MODE, files.WRITE)

        if str(_path.relative_to(workdir)) not in _exclude:
            File.create(_path)
            File.write(_path, _content, _mode)

        if _mode == files.APPEND:
            modified.add(_path)

    after = paths.tree(workdir)

    new = (after[0] - before[0]) | (after[1] - before[1])

    prints.prettytree(workdir, new, modified)


if __name__ == "__main__":
    app()
