from pathlib import Path

from .const import FILE_APPEND_MODE, FILE_ENCODING, SYMBOL_NEW_LINE
from .utils import sortlines


class Code:
    @classmethod
    def add(cls, path: Path, content: str, mode: str = FILE_APPEND_MODE) -> None:
        with path.open(mode, encoding=FILE_ENCODING) as f:
            f.write(SYMBOL_NEW_LINE + content.strip())
        sortlines(path)
