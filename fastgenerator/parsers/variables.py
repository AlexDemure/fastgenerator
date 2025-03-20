import re
from pathlib import Path

from fastgenerator import const
from fastgenerator.os import File


def getvariables(strings: list[str]) -> set:
    pattern = re.compile(const.REGEXP_RENDER_TEMPLATE_VARIABLES_PATTERN)

    variables = set()

    for string in strings:
        matches = pattern.findall(string)
        for match in matches:
            variables.add(match[0])

    return variables


def replacevariables(template: str, context: dict) -> str:
    def _replace(match) -> str:
        key, subkey = match.groups()
        if key in context and subkey in context[key]:
            return context[key][subkey]
        elif key in context and subkey is None:
            return context[key]["original"]
        return match.group(0)

    return re.sub(const.REGEXP_RENDER_TEMPLATE_VARIABLES_PATTERN, _replace, template)
