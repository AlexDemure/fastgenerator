from pathlib import Path
from typing import Any

import yaml

from .const import FILE_ENCODING, FILE_READ_MODE


class Config:
    @classmethod
    def loadfile(cls, path: Path) -> dict[str, Any]:
        with path.open(FILE_READ_MODE, encoding=FILE_ENCODING) as file:
            return yaml.safe_load(file)
