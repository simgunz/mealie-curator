import typer

from mealiecurator.api import MealieClient
from mealiecurator.config import get_config

foods_cmd = typer.Typer(
    no_args_is_help=True,
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["-h", "--help"]},
)


@foods_cmd.command()
def to_lower_case(ctx: typer.Context) -> None:
    """Convert food names to lower case."""
    config = get_config(ctx.obj["config_path"])

    if not config["mealie_url"] or not config["mealie_api_token"]:
        typer.echo(
            "Please configure mealie_url and mealie_api_token in your config file"
        )
        raise typer.Exit(1)

    client = MealieClient(config["mealie_url"], config["mealie_api_token"])

    foods = client.get_all_foods()
    processed = 0
    skipped = 0

    with typer.progressbar(foods, label="Processing foods") as progress:
        for food in progress:
            original_name = food["name"]
            if original_name.islower():
                skipped += 1
                continue
            food["name"] = original_name.lower()
            try:
                client.update_food(food["id"], food)
                processed += 1
            except Exception as e:
                typer.echo(f"Error updating food {original_name}: {e}")

    typer.echo(f"Processed {processed} foods ({skipped} already lowercase)")
