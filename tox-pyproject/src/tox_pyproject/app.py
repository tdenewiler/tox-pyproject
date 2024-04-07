#!/usr/bin/env python3
"""Executable script for running tox-pyproject."""

import sys

from tox_pyproject.tox_pyproject import ToxPyproject


def run(tox_pyproject: ToxPyproject) -> bool:  # pragma: no cover
    """Run tox-pyproject"""
    success = tox_pyproject.run()

    return success


def main() -> None:  # pragma: no cover
    """Run tox-pyproject."""
    tox_pyproject = ToxPyproject()
    print("start")

    success = run(tox_pyproject)
    print(f"success: {success}")

    if not success:
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":  # pragma: no cover
    main()
