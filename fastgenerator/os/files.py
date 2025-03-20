from pathlib import Path

from fastgenerator import const
from fastgenerator.utils import strings


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
            f.write(content)

        with path.open(mode=const.FILE_READ, encoding=const.FILE_ENCODING) as f:
            content = strings.sortimports(f.readlines())

        with path.open(mode=const.FILE_WRITE, encoding=const.FILE_ENCODING) as f:
            f.write(content)

    @classmethod
    def read(cls, path: Path, tolist: bool = False) -> list[str] | str:
        with path.open(mode=const.FILE_READ, encoding=const.FILE_ENCODING) as f:
            return f.readlines() if tolist else f.read()
