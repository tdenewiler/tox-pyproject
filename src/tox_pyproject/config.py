"""Plugin configuration."""


class Config:
    """Plugin configuration."""
    def __init__(self, default_level: str = "threshold") -> None:
        """Initialize configuration."""
        self.default_level = default_level
