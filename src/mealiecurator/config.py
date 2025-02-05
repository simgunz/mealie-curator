"""Configuration management for mealiecurator."""

from pathlib import Path

from appdirs import user_config_dir

CONFIG_DIR = Path(user_config_dir("mealiecurator", appauthor=False))


def ensure_config_dir(config_dir_path: Path) -> None:
    """Ensure the config directory exists."""
    config_dir_path.mkdir(parents=True, exist_ok=True)
