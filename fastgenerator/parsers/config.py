from pathlib import Path

from fastgenerator import const
from fastgenerator.os import HTTP
from fastgenerator.os import File
from fastgenerator.utils import temp
from fastgenerator.utils import urls


def getconfig(file: str) -> tuple[Path, bool]:
    if urls.checkurl(file):
        return temp.getfile(HTTP.download(file), extension=const.FILE_TOML), True
    else:
        return Path(file), False


def getcontent(workdir: Path, content: str) -> str:
    if content.startswith(const.ATTRIBUTE_FILE_CONTENT_SYNTAX_FILE):
        path = Path(content[len(const.ATTRIBUTE_FILE_CONTENT_SYNTAX_FILE) :].strip())

        if not path.is_absolute():
            path = workdir / path

        if path.exists() and path.is_file():
            return File.read(path)

    elif urls.checkurl(content):
        return HTTP.download(content)

    return content
