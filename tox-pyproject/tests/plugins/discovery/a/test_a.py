"""Unit tests for the A discovery plugin."""

import sys

from tox_pyproject.plugins.discovery.a import ADiscoveryPlugin

if sys.version_info < (3, 10):
    from importlib_metadata import entry_points
else:
    from importlib.metadata import entry_points


def test_a_discovery_plugin_found():
    """Test that the plugin manager finds the A discovery plugin."""
    discovery_plugins = {}
    plugins = entry_points(group="tox_pyproject.plugins.discovery")
    for plugin_type in plugins:
        plugin = plugin_type.load()
        discovery_plugins[plugin_type.name] = plugin()
    assert any(
        plugin.get_name() == "A" for _, plugin in list(discovery_plugins.items())
    )


def test_a_discovery_plugin_scan_valid():
    """Test that the A discovery plugin runs."""
    adp = ADiscoveryPlugin()
    found = adp.scan()
    assert found == ["threshold"]
