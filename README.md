## <div align="center">🐍 python-package-template</div>
<div align="center">
    <kbd>
        <a href="https://github.com/daniel-mizsak/python-package-template/actions/workflows/ci.yml" target="_blank"><img src="https://github.com/daniel-mizsak/python-package-template/actions/workflows/ci.yml/badge.svg" alt="build status"></a>
        <a href="https://codecov.io/gh/daniel-mizsak/python-package-template" target="_blank"><img src="https://codecov.io/gh/daniel-mizsak/python-package-template/graph/badge.svg?token=SDXG1S8PVM"/></a>
        <a href="https://results.pre-commit.ci/latest/github/daniel-mizsak/python-package-template/main" target="_blank"><img src="https://results.pre-commit.ci/badge/github/daniel-mizsak/python-package-template/main.svg" alt="pre-commit.ci status"></a>
        <a href='https://python-package-template-pypi.readthedocs.io/en/latest/?badge=latest'><img src='https://readthedocs.org/projects/python-package-template-pypi/badge/?version=latest' alt='docs status' /></a>
        <a href="https://img.shields.io/github/license/daniel-mizsak/python-package-template" target="_blank"><img src="https://img.shields.io/github/license/daniel-mizsak/python-package-template" alt="license"></a>
    </kbd>
</div>

## Overview
A GitHub template with my python package configurations.


To make sure that the all the tools are available in your [virtual environment](https://docs.python.org/3/library/venv.html) (and that you are running your code with its latest modifications), install the package in editable mode by running:

```bash
pip install --editable ".[dev]"
```

Alternatively, you can `Dev Containers: Reopen in Container` in Visual Studio Code if `Docker` is installed.


> [!WARNING]
> This template represents my personal understanding of the current best practices.\
> It is advised to do further research before implementing these configurations in your environment.

Feel free to [open a new issue](https://github.com/daniel-mizsak/python-package-template/issues/new/choose) if you have any questions or suggestions.

## Package tools
This template package relies on the synchronized cooperation of several exceptional tools.\
These tools include:
- [Codecov](https://docs.codecov.com/docs/quick-start) - Code coverage
- [Pre-Commit](https://pre-commit.com/) - Git hooks running on commits
- [MyPy](https://mypy.readthedocs.io/en/stable/) - Static type checking
- [Pytest](https://docs.pytest.org/en/latest/) - Testing and code coverage
- [Ruff](https://docs.astral.sh/ruff/) - Formatting and linting
- [Tox](https://tox.readthedocs.io/en/latest/) - Orchestration of the above tools

For documentation:
- [Sphinx](https://www.sphinx-doc.org/en/master/) - Documentation building
- [ReadTheDocs](https://readthedocs.org/) - Documentation hosting
- [GitHub Pages](https://pages.github.com/) - Documentation hosting

### Codecov
Codecov is used to check the code coverage of the tests.\
It also provides a badge that can be added to the README file.

Codecov is set up to be part of the [tox reusable workflow](https://github.com/daniel-mizsak/workflows/blob/main/.github/workflows/tox.yml), but for this action it is important to generate the coverage report. Currently it is achieved by adding `--cov-report=xml:{work_dir}/artifacts/coverage.xml` as part of the `tox.toml` configuration and uploading/downloading the results using [GitHub Artifacts](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/storing-and-sharing-data-from-a-workflow).

### Pre-Commit
Pre-Commit is used to run certain checks on the code before it is committed.\
These checks are defined in the `.pre-commit-config.yaml` file.\
To use pre-commit is has to be installed in the virtual environment and also added to the git hooks by running `pre-commit install`.

In this repository pre-commit is set up for a number of general issues and to run formatting and linting checks with `ruff`.

Call pre-commit by running:

```bash
pre-commit run --all-files
```

### MyPy
Python by default is a dynamically typed language, but being explicit about types can help to avoid bugs.\
MyPy makes sure that the types are correct and consistent throughout the code.

The `mypy` related settings are defined in the `pyproject.toml` file.\
In this repository MyPy is set up be `strict` and it also checks for some additional issues.

Call mypy by running:

```bash
mypy src tests
```

### Pytest
Pytest is a modern testing framework for python.\
It is way too complex to explain it here, but it runs all the tests from the `tests` directory and also checks the code coverage.

Its settings are defined in the `pyproject.toml` file.

Call pytest by running:

```bash
pytest
```

### Ruff
Ruff is a formatter and linter that is built on top of a lot of open source tools.\
It is very fast and unifies all the useful code quality solutions into a single tool.\
By default it is not too strict, but I like to make it strict by selecting all the available rules.
The exact configuration is defined in the `ruff.toml` file.

If for some reason it makes sense not to comply with a certain rule, it can be disabled for that line using `# noqa: <rule number>`.

Call ruff by running:

```bash
ruff check src tests
```

### Tox
Tox is useful for running the above tools in isolated environments.\
It makes sure that the package setup is consistent and that the tools are working as expected.\
It can be used to test different python versions and different testing scenarios.
I am also using it to automatically generate the documentation and build the package.

In this repository tox is set up to use python 3.11, 3.12 and run codecov, pytest, ruff, mypy, docs and package building.\
The settings are specified in the `tox.toml` file.

Call tox by running:

```bash
tox
```

### Documentation
The documentation is built with Sphinx and it is hosted both on ReadTheDocs and GitHub Pages.\
Both of these services are recommended, however ReadTheDocs requires a bit more setup.

## GitHub repository settings
The following settings are enabled in my repository settings:

Code/About:

- Releases

<br>

General/Features:

- Issues
- Preserve this repository

<br>

General/Pull Requests:

- Allow squash merging
- Always suggest updating pull request branches
- Automatically delete head branches

<br>

Rules/Rulesets:
`main`\
Target branches: `Default`

- Restrict deletions
- Require pull request before merging
    - Dismiss stale pull request approvals when new commits are pushed
    - Require review from Code Owners
    - Allowed merge methods: `Squash`
- Require status checks to pass before merging
    - Require branches to be up to date before merging
    - `pre-commit.ci - pr`
    - `tox / tox (3.11)`
    - `tox / tox (3.12)`
- Block force pushes

<br>

Pages/Build and deployment:

- Source: Github Actions
The actual deployment is done by the `release` workflow.

## Setup PyPi trusted publishing
[PyPI publishing settings](https://pypi.org/manage/account/publishing/)

Add a new pending publisher:

- PyPI Project Name: `python-package-template-pypi` (has to match the project name in `pyproject.toml`)
- Owner: `daniel-mizsak`
- Repository name: `python-package-template`
- Workflow name: `release.yml`

Currently I am using a reusable GitHub workflow to test and build the package ([tox](https://github.com/daniel-mizsak/workflows/blob/main/.github/workflows/tox.yml)), and do the publishing with a separate "non-reusble" workflow, so that trusted publishing can be used.

## More examples
I am trying to use this template in all of my repositories and also contribute back here with new best practices I find.
Some of my other repositories that may be interesting to look at:
- [falcon-formation](https://github.com/daniel-mizsak/falcon-formation) - Create evenly distributed hockey teams.
- [checkmark](https://github.com/daniel-mizsak/checkmark) - Automated assessment generator and evaluator system.
- [pythonvilag-website](https://github.com/PythonVilag/pythonvilag-website) - Source code that powers the Python Világ website.
- [private-lecture-automation](https://github.com/PythonVilag/private-lecture-automation) - Automation tools for private lecture management.

I have also integrated some of the above mentioned tools into my `vscode` settings. You can find them in my [more-than-just-dotfiles](https://github.com/daniel-mizsak/mtjd/blob/main/dotfiles/vscode/settings.json) repository.

<hr>

<div align="center">
    <strong>⭐ Star the repository if you found it useful ⭐</strong>
    <br>
    <a href="https://github.com/daniel-mizsak/repository-template" target="_blank">Repository Template</a> |
    <a href="https://github.com/daniel-mizsak/workflows" target="_blank">Reusable Workflows</a> |
    <a href="https://github.com/daniel-mizsak/mtjd" target="_blank">Development Environment </a>
</div>
