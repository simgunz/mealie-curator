"""Configuration management for mealiecurator."""

from pathlib import Path


def ensure_config_dir(config_dir_path: Path) -> None:
    """Ensure the config directory exists."""
    config_dir_path.mkdir(parents=True, exist_ok=True)
