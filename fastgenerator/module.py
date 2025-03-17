import string
from pathlib import Path

from .alembic import Alembic
from .code import Code
from .config import Config
from .const import FILE_APPEND_MODE, FILE_WRITE_MODE
from .files import File
from .format import Format
from .utils import variations


class Module:
    @classmethod
    def create(cls, path: Path, name: str) -> None:
        cwd = Path.cwd()

        config = Config.loadfile(path)

        module = config.get("module", {})
        alembic = config.get("alembic", {})
        files = module.get("files", [])

        context = variations(name)

        for file in files:
            path = cwd / string.Template(file["path"]).safe_substitute(context)
            content = string.Template(file["content"]).safe_substitute(context)
            mode = FILE_WRITE_MODE if file.get("override") else FILE_APPEND_MODE
            File.add(path)
            Code.add(path, content, mode)

        if alembic:
            Alembic.revision(cwd, context["snake"])
            Alembic.upgrade(cwd)

        Format.run(cwd)
