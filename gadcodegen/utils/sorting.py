import re

from gadcodegen import const


def sortimports(lines: list[str]) -> str:
    imports, code = [], []
    for line in lines:
        (imports if re.match(const.REGEXP_IMPORT_PATTERN, line) else code).append(line)
    return const.SYMBOL_EMPTY.join(sorted(imports) + code)
