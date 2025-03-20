import json

import typer

from fastgenerator import const
from fastgenerator.utils import strings


def getcontext(keys: set[str]) -> dict:
    context = {}

    for key in keys:
        value = typer.prompt(const.TEXTS["getcontext"]["add"].format(key))
        context.update({key: strings.to_cases(value)})

    if context:
        typer.echo(const.TEXTS["getcontext"]["json"].format(json.dumps(context, indent=2)))

    return context
