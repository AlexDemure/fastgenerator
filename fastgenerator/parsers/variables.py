import re
from pathlib import Path

from fastgenerator.const import regexp
from fastgenerator.os import File


def getvariables(file: Path) -> set:
    file = File.read(file)

    pattern = re.compile(regexp.RENDER_TEMPLATE_VARIABLES_PATTERN)

    variables = set()

    for string in file:
        matches = pattern.findall(string)
        for match in matches:
            variables.add(match[0])

    return variables
