import os
import pathlib

from gadify.paths import *

from gadcodegen import const


def tree(workdir: pathlib.Path | str) -> tuple[set[pathlib.Path], set[pathlib.Path]]:
    if isinstance(workdir, str):
        workdir = define(workdir)

    folders, files = set(), set()

    for path, _, filenames in os.walk(workdir):
        path = pathlib.Path(path)

        if path.name.startswith(const.SYMBOL_DOT):
            continue

        folders.add(path)

        for filename in filenames:
            files.add(path / filename)

    return folders, files
