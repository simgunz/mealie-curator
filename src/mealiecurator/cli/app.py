"""mealiecurator CLI."""

from pathlib import Path
from typing import Annotated, Optional

import appdirs
import typer
from typing_extensions import TypeAlias

from mealiecurator import __version__, logs
from mealiecurator.config import get_config
from mealiecurator.logs import LogLevel

CONFIG_DIR_PATH = Path(appdirs.user_config_dir("mealiecurator", appauthor=False))
DEFAULT_CONFIG_PATH = CONFIG_DIR_PATH / "mealiecuratorrc"

CallbackContext: TypeAlias = typer.Context

app = typer.Typer()


def version_callback(value: bool) -> None:
    if value:
        typer.echo(f"mealiecurator version {__version__}")
        raise typer.Exit()


@app.callback()
def cli(
    ctx: CallbackContext,
    config_path: Annotated[
        Optional[Path],
        typer.Option(help="Path to the configuration file"),
    ] = DEFAULT_CONFIG_PATH,
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
    """Common options and main CLI entrypoint for mealiecurator."""
    ctx.ensure_object(dict)
    ctx.obj["config_path"] = config_path
    logs.set_level(log_level.value)


@app.command()
def config(
    ctx: CallbackContext,
    key: Annotated[str, typer.Argument(help="Configuration key to get/set")],
    value: Annotated[Optional[str], typer.Argument(help="Value to set")] = None,
) -> None:
    """Get or set a configuration value."""
    config_obj = get_config(ctx.obj["config_path"])
    if value is None:
        config_value = config_obj[key]
        typer.echo(config_value)
    else:
        config_obj[key] = value
        config_obj.write()
        typer.echo(f"Set {key} to {value}")
