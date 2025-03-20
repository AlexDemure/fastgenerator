from pathlib import Path

from fastgenerator import const


def prettytree(workdir: Path, new: set[Path], modified: set[Path]) -> None:
    stack = [(workdir, "", False)]

    while stack:
        path, prefix, is_last = stack.pop()

        marker = const.SYMBOL_EMPTY
        if path in new:
            marker = const.TREE_MARKER_NEW
        elif path in modified:
            marker = const.TREE_MARKER_EDIT

        connector = const.TREE_LAST if is_last else const.TREE_MIDDLE

        print(f"{prefix}{connector}{path.name}{const.SYMBOL_SLASH if path.is_dir() else const.SYMBOL_EMPTY}{marker}")

        if path.is_dir():
            entries = sorted(path.iterdir(), key=lambda e: (e.is_file(), e.name.lower()))
            total = len(entries)

            for i, entry in enumerate(reversed(entries)):
                new_prefix = prefix + (const.TREE_SPACE if is_last else const.TREE_BRANCH)
                stack.append((entry, new_prefix, i == total - 1))
