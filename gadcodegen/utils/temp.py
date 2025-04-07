import tempfile
from pathlib import Path

from gadcodegen import const


def getfile(content: str, extension: str) -> Path:
    with tempfile.NamedTemporaryFile(delete=False, suffix=extension, mode=const.FILE_WRITE) as f:
        f.write(content)
    return Path(f.name)
