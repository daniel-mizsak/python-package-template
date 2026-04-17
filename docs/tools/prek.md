# Prek

[Prek](https://prek.j178.dev/){target} is a git hook manager for pre-commit checks.

With `prek` a list of pre-commit checks can be defined that will be executed on the code before it is committed. If the checks fail, the commit is aborted. This ensures that the code being committed follows certain standards, but many programmers also find this limiting.

The `prek` related settings are defined in the `.pre-commit-config.yaml` file.

<!-- prettier-ignore-start -->

!!! info
    To use `prek`, it has to be installed in the virtual environment and also added to the git hooks by running `prek install`.
<!-- prettier-ignore-end -->

Call `prek` by making a git commit or by running:

```bash
uv run prek run --all-files
```

Or (alternatively) use `just`:

```bash
just prek
```

I used to use [pre-commit](https://pre-commit.com){target} before, but switched to `prek` as it seems to be more actively maintained.
