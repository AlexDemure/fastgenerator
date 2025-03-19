import re

from fastgenerator.const import regexp
from fastgenerator.const import symbols


def separate(value: str) -> list[str]:
    return re.split(regexp.SEPARATOR_PATTERN, value)


def concat(words: list[str], symbol: str) -> str:
    return symbol.join(words)


def to_lower(value: str) -> str:
    return value.lower()


def to_upper(value: str) -> str:
    return value.upper()


def to_capitalize(value: str) -> str:
    return value.capitalize()


def to_title(value: str) -> str:
    return concat(words=[to_capitalize(word) for word in separate(value)], symbol=symbols.WHITESPACE)


def to_snake(value: str) -> str:
    return concat(separate(value), symbol=symbols.LOWER_HYPHEN).lower()


def to_kebab(value: str) -> str:
    return concat(separate(value), symbol=symbols.HYPHEN).lower()


def to_pascal(value: str) -> str:
    return concat(words=[to_capitalize(word) for word in separate(value)], symbol=symbols.EMPTY)


def to_cases(value: str) -> dict:
    return {
        "original": value,
        "lower": to_lower(value),
        "upper": to_upper(value),
        "title": to_title(value),
        "snake": to_snake(value),
        "kebab": to_kebab(value),
        "pascal": to_pascal(value),
    }


def sortimports(lines: list[str]) -> str:
    imports, code = [], []
    for line in lines:
        (imports if re.match(regexp.IMPORT_PATTERN, line) else code).append(line)
    return "".join(sorted(imports) + code)
