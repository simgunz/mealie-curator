"""mealiecurator CLI."""
from typing import Annotated, Optional

import typer

from mealiecurator import __version__, logs
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
