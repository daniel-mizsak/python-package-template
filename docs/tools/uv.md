# Uv

[Uv](https://docs.astral.sh/uv/){target} is a package manager, similar to `pip`.

It is extremely fast and makes packaging projects less painful.

I do not often interact with `uv` directly, as I tend to call commands via `just`, but some useful commands are:

- `uv sync`: Set up development environment based on the `pyproject.toml` and the `.python-version` file.
- `uv run <package>`: Run a package installed in the virtual environment (without activating it).
- `uv build`: Build the package.
