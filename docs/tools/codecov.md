# Codecov

[Codecov](https://about.codecov.io){target} is a platform for tracking code coverage.

In my `Justfile`, under the `coverage` command I specify that `pytest` should run while generating an `xml` and an `html` report. The `html` report is used locally to inspect the coverage, while the `xml` report is the one getting uploaded to `Codecov`.

One way of uploading is the [codecov-cli](https://docs.codecov.com/docs/the-codecov-cli){target}, but I prefer my [reusable python-ci GitHub Workflow](https://github.com/daniel-mizsak/workflows/blob/main/.github/workflows/python-ci.yml){target} that calls the `codecov/codecov-action` action.

`Codecov` has a [GitHub App](https://github.com/apps/codecov){target}.
