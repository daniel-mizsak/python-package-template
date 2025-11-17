# Nox

[Nox](https://nox.thea.codes/en/stable/index.html){target} is a testing automation framework for multiple Python environments.

I use `nox` to run my test suite against multiple Python versions to make sure the package is compatible with all of them. This also means that I do not use `nox` for applications, where it is sufficient to test against a single Python version.

The `nox` related configurations are defined in the `noxfile.py` file.

Call `nox` by running:

```bash
uv run nox
```

Or (preferably) use `just`:

```bash
just test-all-python
```

A `nox` alternative is [tox](https://tox.wiki/){target}. It is just as capable.
