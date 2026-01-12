# MyPy

[MyPy](https://mypy.readthedocs.io/en/stable/){target} is a static type checker.

Python is a dynamically typed language, meaning it will only complain about potential type inconsistencies during runtime. (Which is too late!)

Being explicit about types during development can help to avoid bugs. MyPy makes sure that the types are correct and consistent throughout the code.

The `mypy` related settings are defined in the `pyproject.toml` file.

Call `mypy` by running:

```bash
uv run mypy .
```

Or (preferably) use `just`:

```bash
just type
```
