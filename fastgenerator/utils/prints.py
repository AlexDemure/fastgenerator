from pathlib import Path

from fastgenerator.const import symbols


def prettytree(workdir: Path, new: set[Path], modified: set[Path]) -> None:
    stack = [(workdir, "", False)]

    while stack:
        path, prefix, is_last = stack.pop()

        marker = symbols.EMPTY
        if path in new:
            marker = symbols.TREE_MARKER_NEW
        elif path in modified:
            marker = symbols.TREE_MARKER_EDIT

        connector = symbols.TREE_LAST if is_last else symbols.TREE_MIDDLE

        print(f"{prefix}{connector}{path.name}{symbols.SLASH if path.is_dir() else symbols.EMPTY}{marker}")

        if path.is_dir():
            entries = sorted(path.iterdir(), key=lambda e: (e.is_file(), e.name.lower()))
            total = len(entries)

            for i, entry in enumerate(reversed(entries)):
                new_prefix = prefix + (symbols.TREE_SPACE if is_last else symbols.TREE_BRANCH)
                stack.append((entry, new_prefix, i == total - 1))
