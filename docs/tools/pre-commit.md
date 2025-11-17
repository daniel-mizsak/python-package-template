# Pre-Commit

[Pre-Commit](https://pre-commit.com){target} is a git pre-commit hook manager.

With `pre-commit` a list of checks can be defined that will be executed on the code before it is committed. If the checks fail, the commit is aborted. This ensures that the code being committed follows certain standards, but many programmers also find this limiting.

The `pre-commit` related settings are defined in the `.pre-commit-config.yaml` file.

<!-- prettier-ignore-start -->

!!! info
    To use `pre-commit`, it has to be installed in the virtual environment and also added to the git hooks by running `pre-commit install`.
<!-- prettier-ignore-end -->

Call pre-commit by making a git commit or by running:

```bash
uv run pre-commit run --all-files
```

Or (alternatively) use `just`:

```bash
just pre-commit
```
