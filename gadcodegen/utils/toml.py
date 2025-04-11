import tomli


def todict(content: str) -> dict:
    return tomli.loads(content)
