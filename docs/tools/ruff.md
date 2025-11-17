# Ruff

[Ruff](https://docs.astral.sh/ruff/){target} is a code formatter and linter.

Formatters make sure that the code follows a consistent style, regardless of who wrote it. I like running the formatter every time a file is saved.

Linters highlight potential issues with the code based on a set of predefined rules. These suggestions usually help to simplify the code and avoid common pitfalls.

I like to make my project setup as strict as possible by enabling all available rules. (`Ruff` has a lot of rules defined as they reimplemented many existing rules from other open source projects.)

If for some reason it makes sense not to comply with a certain rule, it can be disabled for that line using `# noqa: <rule number>`.

The `ruff` related settings are defined in the `ruff.toml` file.

Call `ruff` by running:

```bash
uv run ruff check
uv run ruff format --diff
```

Or (preferably) use `just`:

```bash
just lint
```
