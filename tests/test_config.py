from pathlib import Path

from mealiecurator.config import ensure_config_dir, get_config


def test_ensure_config_dir_creates_new(tmp_path: Path):
    config_path = tmp_path / "config"

    ensure_config_dir(config_path)

    assert config_path.exists()
    assert config_path.is_dir()


def test_ensure_config_dir_existing(tmp_path: Path):
    config_path = tmp_path / "config"
    config_path.mkdir(parents=True)

    ensure_config_dir(config_path)

    assert config_path.exists()
    assert config_path.is_dir()


def test_get_config_default_mealie_url(tmp_path: Path):
    config_path = tmp_path / "config" / "configrc"

    config = get_config(config_path)

    assert config["mealie_url"] == ""


def test_get_config_set_mealie_url(tmp_path: Path):
    config_path = tmp_path / "config" / "configrc"
    mealie_url = "http://mealie.example.com"

    config = get_config(config_path)
    config["mealie_url"] = mealie_url
    config.write()

    new_config = get_config(config_path)
    assert new_config["mealie_url"] == mealie_url
