# Ty

[Ty](https://docs.astral.sh/ty/){target} is a static type checker.

Python is a dynamically typed language, meaning it will only complain about potential type inconsistencies during runtime. (Which is too late!)

Being explicit about types during development can help to avoid bugs. Ty makes sure that the types are correct and consistent throughout the code.

Call `ty` by running:

```bash
uv run ty check
```

Or (preferably) use `just`:

```bash
just type
```
