from pathlib import Path

from gadcodegen import const
from gadcodegen.utils import sorting


class File:
    @classmethod
    def create(cls, path: Path) -> None:
        if not path.parent.exists():
            path.parent.mkdir(parents=True, exist_ok=True)

        if not path.exists():
            path.touch()

    @classmethod
    def write(cls, path: Path, content: str, mode: str = const.FILE_WRITE) -> None:
        cls.create(path)

        with path.open(mode=mode, encoding=const.FILE_ENCODING) as f:
            f.write(const.SYMBOL_NEWLINE + content if mode == const.FILE_APPEND else content)

        with path.open(mode=const.FILE_READ, encoding=const.FILE_ENCODING) as f:
            content = sorting.sortimports(f.readlines())

        with path.open(mode=const.FILE_WRITE, encoding=const.FILE_ENCODING) as f:
            f.write(content)

    @classmethod
    def read(cls, path: Path, tolist: bool = False, mode: str = const.FILE_READ) -> str | list[str]:
        with path.open(mode=mode, encoding=const.FILE_ENCODING) as f:
            return f.readlines() if tolist else f.read()
