"""Discover A files to analyze."""

from tox_pyproject.config import Config


class ADiscoveryPlugin():
    """Discover A files to analyze."""

    def get_name(self) -> str:
        """Get name of discovery type."""
        return "A"

    def scan(self) -> list[str]:
        """Scan package looking for A files."""
        config = Config()
        a_files: list[str] = []
        a_files.append(config.default_level)

        return a_files
