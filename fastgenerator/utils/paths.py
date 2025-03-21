import os
from pathlib import Path


def current() -> Path:
    return Path.cwd()


def define(workdir: str | None = None) -> Path:
    if not workdir:
        return current()
    elif workdir.startswith("/"):
        return Path(workdir)
    else:
        return current() / workdir


def tree(workdir: Path | str) -> tuple[set[Path], set[Path]]:
    if isinstance(workdir, str):
        workdir = define(workdir)

    folders, files = set(), set()

    for path, _, filenames in os.walk(workdir):
        path = Path(path)

        if path.name.startswith("."):
            continue

        folders.add(path)

        for filename in filenames:
            files.add(path / filename)

    return folders, files
