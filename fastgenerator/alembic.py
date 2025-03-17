import contextlib
import subprocess
from pathlib import Path


class Alembic:
    @classmethod
    def init(cls, path: Path, migrations: Path) -> None:
        with contextlib.suppress(subprocess.CalledProcessError):
            subprocess.run(["alembic", "init", str(migrations)], cwd=path, check=True)

    @classmethod
    def revision(cls, path: Path, commit: str) -> None:
        with contextlib.suppress(subprocess.CalledProcessError):
            subprocess.run(["alembic", "revision", "-m", commit, "--autogenerate"], cwd=path, check=True)

    @classmethod
    def upgrade(cls, path: Path) -> None:
        with contextlib.suppress(subprocess.CalledProcessError):
            subprocess.run(["alembic", "upgrade", "head"], cwd=path, check=True)
