import os
import subprocess
from pathlib import Path


class Format:
    @classmethod
    def run(cls, path: Path) -> None:
        if os.path.exists("format.sh"):
            subprocess.run(["sh", "format.sh"], cwd=path, check=True)
