"""mealiecurator CLI."""

from pathlib import Path
from typing import Annotated, Optional

import appdirs
import typer

from mealiecurator import __version__, logs
from mealiecurator.config import get_config
from mealiecurator.logs import LogLevel

app = typer.Typer()


def version_callback(value: bool) -> None:
    if value:
        typer.echo(f"mealiecurator version {__version__}")
        raise typer.Exit()


@app.command()
def cli(
    log_level: Annotated[
        Optional[LogLevel],
        typer.Option(
            case_sensitive=False,
            envvar="LOG_LEVEL",
            help="Set the logging level.",
        ),
    ] = LogLevel.INFO,
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-V",
            callback=version_callback,
            is_eager=True,
            help="Show the application's version and exit.",
        ),
    ] = None,
) -> None:
    """Engage with mealiecurator using this CLI."""
    logs.set_level(log_level.value)


@app.command()
def config(
    key: Annotated[str, typer.Argument(help="Configuration key to get/set")],
    value: Annotated[Optional[str], typer.Argument(help="Value to set")] = None,
) -> None:
    """Get or set a configuration value."""
    config_dir_path = Path(appdirs.user_config_dir("mealiecurator", appauthor=False))
    config_path = config_dir_path / "mealiecuratorrc"
    config = get_config(config_path)
    if value is None:
        config_value = config[key]
        typer.echo(config_value)
    else:
        config[key] = value
        config.write()
        typer.echo(f"Set {key} to {value}")
