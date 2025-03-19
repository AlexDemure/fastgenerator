import json

import typer

from fastgenerator.const import texts
from fastgenerator.utils import strings


def getcontext(keys: list[str]) -> dict:
    context = {}

    for key in keys:
        value = typer.prompt(texts.SPEECHES["getcontext"]["add"].format(key))
        context.update({key: strings.to_cases(value)})

    if context:
        typer.echo(texts.SPEECHES["getcontext"]["json"].format(json.dumps(context, indent=2)))

    return context
