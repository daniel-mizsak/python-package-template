# Pytest

[Pytest](https://docs.pytest.org/en/latest/){target} is a modern testing framework.

It is way too complex to explain it here, but it runs all the tests from the `tests` directory and also checks the code coverage (using `pytest-cov`).

The `pytest` related settings are defined in the `pyproject.toml` file.

Call `pytest` by running:

```bash
uv run pytest
```

Or (preferably) use `just`:

```bash
just test
```
