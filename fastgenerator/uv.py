import contextlib
import subprocess
from pathlib import Path


class UV:
    @classmethod
    def add_package(cls, path: Path, group: str, package: str) -> None:
        cmd = ["uv", "add", "--group", group, package] if group != "main" else ["uv", "add", package]
        with contextlib.suppress(subprocess.CalledProcessError):
            subprocess.run(cmd, cwd=path, check=True)
