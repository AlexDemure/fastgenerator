from pathlib import Path


class Folder:
    @classmethod
    def create(cls, path: Path) -> None:
        if not path.parent.exists():
            path.parent.mkdir(parents=True, exist_ok=True)

        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
