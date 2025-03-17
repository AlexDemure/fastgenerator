import re
from pathlib import Path

from .const import FILE_ENCODING, FILE_READ_MODE, FILE_WRITE_MODE, REGEX_IMPORT, REGEX_NORMALIZED_TEXT, SYMBOL_NEW_LINE


def variations(text: str) -> dict[str, str]:
    normalized = re.sub(REGEX_NORMALIZED_TEXT, " ", text).strip()

    words = normalized.split()

    return dict(
        pascal="".join(word.capitalize() for word in words),
        snake="_".join(word.lower() for word in words),
        kebab="-".join(word.lower() for word in words),
    )


def sortlines(path: Path) -> None:
    with path.open(FILE_READ_MODE, encoding=FILE_ENCODING) as f:
        lines = f.readlines()

    imports = []
    code = []

    for line in lines:
        if line.strip():
            if re.match(REGEX_IMPORT, line):
                imports.append(line.strip())
            else:
                code.append(line.rstrip())

    with path.open(FILE_WRITE_MODE, encoding=FILE_ENCODING) as f:
        f.writelines(SYMBOL_NEW_LINE.join(imports + code))
