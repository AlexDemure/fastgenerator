from pathlib import Path


class File:
    @classmethod
    def add(cls, path: Path) -> None:
        if not path.parent.exists():
            path.parent.mkdir(parents=True, exist_ok=True)

        if not path.exists():
            path.touch()


class Folder:
    @classmethod
    def add(cls, path: Path) -> None:
        if not path.parent.exists():
            path.parent.mkdir(parents=True, exist_ok=True)

        if not path.exists():
            path.mkdir()
