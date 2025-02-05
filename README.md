# Mealie Curator

Command-line toolkit for maintaining and organizing your Mealie recipe database

## Setup

1. Generate an API token from `http(s)://<MEALIE_HOST>/user/profile/api-tokens`
2. Configure `mealiecurator`

    ```bash
    mealiecurator config mealie_url http(s)://<MEALIE_HOST>
    mealiecurator config mealie_api_token <API_TOKEN>
    ```

## Usage

Make all the foods lowercase

```bash
mealiecurator foods to-lower-case
```
