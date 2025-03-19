import re

from fastgenerator.const import regexp


def loadenv(template: str, context: dict) -> str:
    def replace(match) -> str:
        key, subkey = match.groups()
        if key in context and subkey in context[key]:
            return context[key][subkey]
        elif key in context and subkey is None:
            return context[key]["original"]
        return match.group(0)

    return re.sub(regexp.RENDER_TEMPLATE_VARIABLES_PATTERN, replace, template)
