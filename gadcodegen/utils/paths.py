import os
from pathlib import Path

from gadify.paths import *

from gadcodegen import const


def tree(workdir: Path | str) -> tuple[set[Path], set[Path]]:
    if isinstance(workdir, str):
        workdir = define(workdir)

    folders, files = set(), set()

    for path, _, filenames in os.walk(workdir):
        path = Path(path)

        if path.name.startswith(const.SYMBOL_DOT):
            continue

        folders.add(path)

        for filename in filenames:
            files.add(path / filename)

    return folders, files
