import shlex
import subprocess
import json
import typer
from jinja2 import Template
from fastgenerator import const
from fastgenerator import parsers
from fastgenerator.os import File
from fastgenerator.os import Folder
from fastgenerator.utils import paths
from fastgenerator.utils import prints
from fastgenerator.utils import strings

app = typer.Typer(help="Fastgenerator")


@app.command()
def generate(
    file: str = typer.Option(..., "-f", "--file", help="Path or link to configuration file"),
    context: str = typer.Option("{}", "-c", "--context", help="JSON context for templates")
) -> None:
    cwd = paths.current()

    file, temp = parsers.getconfig(file)

    config = strings.to_toml(File.read(file))

    workdir = paths.define(config.get(const.TAG_WORKDIR, ""))

    context = json.loads(context)

    before = paths.tree(workdir)

    modified = set()

    folders = config.get(const.TAG_FOLDERS, [])
    files = config.get(const.TAG_FILES, [])
    exclude = set(config.get(const.TAG_EXCLUDE, []))

    for folder in folders:
        path = workdir / Template(folder).render(context)
        pyfile = path / const.FILE_PYINIT
        Folder.create(path)

        if str(pyfile.relative_to(workdir)) not in exclude:
            File.create(pyfile)

    for f in files:
        mode = f.get(const.ATTRIBUTE_FILE_MODE, const.FILE_WRITE)
        path = workdir / Template(f[const.ATTRIBUTE_FILE_PATH]).render(context)
        content = Template(parsers.getcontent(cwd, f[const.ATTRIBUTE_FILE_CONTENT])).render(context)

        if str(path.relative_to(workdir)) not in exclude:
            File.create(path)
            File.write(path, content, mode)

        if mode == const.FILE_APPEND:
            modified.add(path)

    scripts = config.get(const.TAG_SCRIPTS, [])

    for script in scripts:
        command = Template(script.get(const.ATTRIBUTE_SCRIPT_COMMAND)).render(context)
        check = script.get(const.ATTRIBUTE_SCRIPT_CHECK, False)
        subprocess.run(shlex.split(command), cwd=workdir, text=True, check=check)

    after = paths.tree(workdir)

    new = (after[0] - before[0]) | (after[1] - before[1])

    prints.prettytree(workdir, new, modified)

    if temp:
        file.unlink(missing_ok=True)


if __name__ == "__main__":
    app()
