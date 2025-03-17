from pathlib import Path

from .alembic import Alembic
from .code import Code
from .config import Config
from .const import DEFAULT_PYFILE, FILE_WRITE_MODE
from .files import File, Folder
from .format import Format
from .uv import UV


class App:
    @classmethod
    def create(cls, file: Path) -> None:
        cwd = Path.cwd()

        config = Config.loadfile(file)

        app = config.get("app", {})
        tree = app.get("tree", {})
        files = app.get("files", [])

        stack = [(cwd, tree)]

        while stack:
            path, tree = stack.pop()
            for folder, data in tree.items():
                if isinstance(data, dict):
                    Folder.add(path / folder)
                    if data.pop(DEFAULT_PYFILE, True):
                        File.add(path / folder / DEFAULT_PYFILE)
                    stack.append((path / folder, data))

        if uv := config.get("uv", {}):
            for group, packages in uv.items():
                for package in packages:
                    UV.add_package(cwd, group, package)

        if alembic := config.get("alembic"):
            Alembic.init(cwd, alembic.get("init"))
            Alembic.upgrade(cwd)

        for file in files:
            File.add(cwd / file["path"])
            Code.add(path=cwd / file["path"], content=file["content"], mode=FILE_WRITE_MODE)

        Format.run(cwd)
