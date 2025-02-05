"""Configuration management for mealiecurator."""

from pathlib import Path

from appdirs import user_config_dir
from configobj import ConfigObj
from validate import Validator

CONFIG_DIR = Path(user_config_dir("mealiecurator", appauthor=False))
CONFIG_SPEC = """
[DEFAULT]
""".splitlines()


def ensure_config_dir(config_dir_path: Path) -> None:
    """Ensure the config directory exists."""
    config_dir_path.mkdir(parents=True, exist_ok=True)


def get_config(config_path: Path) -> ConfigObj:
    """Get the configuration object."""
    ensure_config_dir(config_path.parent)
    config = ConfigObj(str(config_path), configspec=CONFIG_SPEC)
    validator = Validator()
    config.validate(validator)
    return config
