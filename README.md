# Mealie Curator

Command-line toolkit for maintaining and organizing your Mealie recipe database

> [!warning]
> This tool is in early development and may not work as expected. Use at your own risk.

> [!warning]
>  This tool directly modifies your Mealie database. Always create a backup of your database before using it. You can create a backup from the Mealie admin interface at `http(s)://<MEALIE_HOST>/admin/backups`.

## Setup

1. Generate an API token from `http(s)://<MEALIE_HOST>/user/profile/api-tokens`
2. Configure `mealiecurator`

    ```bash
    mealiecurator config mealie_url http(s)://<MEALIE_HOST>
    mealiecurator config mealie_api_token <API_TOKEN>
    ```


## Usage

> [!tip]
> You can use the `--dry-run` option to see the changes that will be made without actually modifying the database.

Make all the foods lowercase

```bash
mealiecurator foods to-lower-case
```
