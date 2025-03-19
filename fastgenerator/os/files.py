import tempfile
import urllib.request
from pathlib import Path

import tomli

from fastgenerator.const import files
from fastgenerator.utils import strings


class File:
    @classmethod
    def create(cls, path: Path) -> None:
        if not path.parent.exists():
            path.parent.mkdir(parents=True, exist_ok=True)

        if not path.exists():
            path.touch()

    @classmethod
    def write(cls, path: Path, content: str, mode: str) -> None:
        cls.create(path)

        with path.open(mode, encoding=files.ENCODING) as f:
            f.write(content)

        with path.open(files.READ, encoding=files.ENCODING) as f:
            content = strings.sortimports(f.readlines())

        with path.open(files.WRITE, encoding=files.ENCODING) as f:
            f.write(content)

    @classmethod
    def read(cls, path: Path) -> list[str]:
        with path.open(files.READ, encoding=files.ENCODING) as f:
            return f.readlines()

    @classmethod
    def toml(cls, path: Path) -> dict:
        with path.open(files.READ_BINARY) as file:
            return tomli.load(file)

    @classmethod
    def download(cls, url: str, extension: str) -> Path:
        file = tempfile.NamedTemporaryFile(delete=False, suffix=extension)

        with urllib.request.urlopen(url) as response:
            with open(file.name, files.WRITE_BINARY) as f:
                f.write(response.read())

        return Path(file.name)
