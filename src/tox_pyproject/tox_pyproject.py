"""Code analysis front-end."""

import sys
from typing import Any

if sys.version_info < (3, 10):
    from importlib_metadata import entry_points
else:
    from importlib.metadata import entry_points


class ToxPyproject:
    """Tox pyproject."""

    def __init__(self) -> None:
        """Initialize."""
        self.discovery_plugins: dict[str, Any] = {}
        plugins = entry_points(group="tox_pyproject.plugins.discovery")
        print(f"discovered plugins: {plugins}")
        for plugin_type in plugins:
            plugin = plugin_type.load()
            self.discovery_plugins[plugin_type.name] = plugin()

    def run(self) -> bool:
        """Run."""
        success = True

        print("---Discovery---")
        discovery_plugins = []
        if not discovery_plugins:
            discovery_plugins = list(self.discovery_plugins)

        plugins_ran: list[Any] = []
        for plugin_name in discovery_plugins:
            if plugin_name not in self.discovery_plugins:
                print("Can't find specified discovery plugin %s!", plugin_name)
                return None, False

            plugin = self.discovery_plugins[plugin_name]
            if plugin.get_name() not in plugins_ran:
                print(f"Running {plugin.get_name()} discovery plugin...")
                plugin.scan()
                print(f"{plugin.get_name()} discovery plugin done.")
                plugins_ran.append(plugin.get_name())
        print(f"All plugins run: {plugins_ran}")
        print("---Discovery---")

        return success
