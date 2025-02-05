# Mealie Curator

Command-line toolkit for maintaining and organizing your Mealie recipe database


## Usage

TBW

## Setup

### Dependencies

- python
- poetry [pip]
- make (optional)
- pytest (optional, installed by poetry, but it's more convenient to have it installed on the system) [pip]
- pre-commit (optional, installed by poetry, but it's more convenient to have it installed on the system) [pip]

### Development Environment Configuration

- Configure the project (poetry, pre-commit):
  ```bash
  make setup
  ```
  or to have more strict pre-commit rules:
  ```bash
  make setup-strict
  ```
- Open VSCode and install the suggested extensions

#### Environment Variables

##### Development

Project specific environment variables are defined in the `.env` file. This file is not versioned and it's used for local development only. If you would like these to automatically be loaded, it is recommended that you install direnv and run `direnv allow`, which will then also automatically load the poetry virtual environment using the `layout_poetry` functionality in the `.envrc` file.

##### Production

For production it is not recommended to use a `.envrc` file or direnv.

##### Adding Python Package Registry Credentials

To add credentials to the Poetry configuration outside of Docker, use the following commands:

```bash
poetry config http-basic.my_registry your_username your_personal_access_token
poetry source add my_registry https://gitlab.mycompany.com/api/v4/projects/1234/packages/pypi/simple
poetry add private-package@0.1.0 --source my_registry
```

## Versioning

This project is tagged with versions according to [SemVer](https://semver.org/). To bump the project version:

```bash
make bump
```
