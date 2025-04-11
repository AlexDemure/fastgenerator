import json
import shlex
import subprocess

import typer
from jinja2 import Template

from gadcodegen import const
from gadcodegen import parsers
from gadcodegen.os import File
from gadcodegen.os import Folder
from gadcodegen.utils import paths
from gadcodegen.utils import prints
from gadcodegen.utils import toml

app = typer.Typer(help="gadcodegen")


@app.command()
def generate(
    file: str = typer.Option(..., "-f", "--file", help="Path or link to configuration file"),
    context: str = typer.Option("{}", "-c", "--context", help="JSON context for templates"),
) -> None:
    cwd = paths.current()

    file, buffer = parsers.getconfig(file)

    config = toml.todict(File.read(file))

    workdir = paths.define(config.get(const.SYNTAX_WORKDIR))

    context = json.loads(context)

    before = paths.tree(workdir)

    modified = set()

    folders = config.get(const.SYNTAX_FOLDERS, [])
    files = config.get(const.SYNTAX_FILES, [])
    exclude = set(config.get(const.SYNTAX_EXCLUDE, []))

    for folder in folders:
        path = workdir / Template(folder).render(context)
        pyfile = path / const.PYTHON_INIT
        Folder.create(path)

        if str(pyfile.relative_to(workdir)) not in exclude:
            File.create(pyfile)

    for f in files:
        mode = f.get(const.SYNTAX_FILES_MODE, const.FILE_WRITE)
        path = workdir / Template(f[const.SYNTAX_FILES_PATH]).render(context)
        content = Template(parsers.getcontent(cwd, f[const.SYNTAX_FILES_CONTENT])).render(context)

        if str(path.relative_to(workdir)) not in exclude:
            File.create(path)
            File.write(path, content, mode)

        if mode == const.FILE_APPEND:
            modified.add(path)

    scripts = config.get(const.SYNTAX_SCRIPTS, [])

    for script in scripts:
        command = Template(script.get(const.SYNTAX_SCRIPTS_COMMAND)).render(context)
        check = script.get(const.SYNTAX_SCRIPTS_CHECK, False)
        subprocess.run(shlex.split(command), cwd=workdir, text=True, check=check)

    after = paths.tree(workdir)

    new = (after[0] - before[0]) | (after[1] - before[1])

    prints.prettytree(workdir, new, modified)

    if buffer:
        file.unlink(missing_ok=True)


if __name__ == "__main__":
    app()
