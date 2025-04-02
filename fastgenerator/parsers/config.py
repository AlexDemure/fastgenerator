from pathlib import Path

from fastgenerator import const
from fastgenerator.os import HTTP
from fastgenerator.os import File
from fastgenerator.utils import temp
from fastgenerator.utils import urls


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
