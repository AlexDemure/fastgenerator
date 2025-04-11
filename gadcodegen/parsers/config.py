from pathlib import Path

from gadify import temp
from gadify import urls

from gadcodegen import const
from gadcodegen.os import HTTP
from gadcodegen.os import File


def getconfig(file: str) -> tuple[Path, bool]:
    if urls.checkurl(file):
        return temp.getfile(HTTP.download(file), extension=const.EXTENSION_TOML), True
    else:
        return Path(file), False


def getcontent(workdir: Path, content: str) -> str:
    if content.startswith(const.SYNTAX_FILES_CONTENT_FILE):
        path = Path(content[len(const.SYNTAX_FILES_CONTENT_FILE) :].strip())

        if not path.is_absolute():
            path = workdir / path

        if path.exists() and path.is_file():
            return File.read(path)

    elif urls.checkurl(content):
        return HTTP.download(content)

    return content
