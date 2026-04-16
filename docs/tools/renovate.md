# Renovate

[Renovate](https://docs.renovatebot.com/){target} is a dependency update automation tool.

It scans the repository configuration and opens pull requests when supported dependencies can be updated. This keeps the project dependencies current without having to manually track new releases.

The `renovate` related settings are defined in the `.github/renovate.json5` file.

In this template I use `renovate` to update:

- `github-actions` dependencies,
- `pep621` dependencies from `pyproject.toml`,
- `pre-commit` dependencies from `.pre-commit-config.yaml`.

I also prefer grouping updates by manager and waiting at least 7 days before new releases are updated.

`Renovate` is used as a [GitHub App](https://github.com/apps/renovate){target}. Once it is installed for the repository, it will automatically read the configuration and start opening pull requests.
