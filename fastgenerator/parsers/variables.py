import re

from fastgenerator import const


def getvariables(strings: list[str]) -> set:
    pattern = re.compile(const.REGEXP_RENDER_TEMPLATE_VARIABLES_PATTERN)

    variables = set()

    for string in strings:
        matches = pattern.findall(string)
        for match in matches:
            variables.add(match[0])

    return variables


def replacevariables(template: str, context: dict) -> str:
    def replace(match) -> str:
        key, subkey = match.groups()

        if key in context:
            value = context[key]

            if subkey and isinstance(value, dict) and subkey in value:
                return value[subkey]
            elif isinstance(value, dict) and "original" in value:
                return value["original"]
            elif isinstance(value, str):
                return value

        return match.group(0)

    return re.sub(const.REGEXP_RENDER_TEMPLATE_VARIABLES_PATTERN, replace, template)
