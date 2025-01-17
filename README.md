## <div align="center"> 🐍 python-package-template</div>

<div align="center">
<a href="https://github.com/daniel-mizsak/python-package-template/actions/workflows/ci.yml" target="_blank"><img src="https://github.com/daniel-mizsak/python-package-template/actions/workflows/ci.yml/badge.svg" alt="build status"></a>
<a href="https://codecov.io/gh/daniel-mizsak/python-package-template" target="_blank"><img src="https://codecov.io/gh/daniel-mizsak/python-package-template/graph/badge.svg?token=SDXG1S8PVM"/></a>
<a href="https://results.pre-commit.ci/latest/github/daniel-mizsak/python-package-template/main" target="_blank"><img src="https://results.pre-commit.ci/badge/github/daniel-mizsak/python-package-template/main.svg" alt="pre-commit.ci status"></a>
<a href='https://python-package-template-pypi.readthedocs.io/en/latest/?badge=latest'><img src='https://readthedocs.org/projects/python-package-template-pypi/badge/?version=latest' alt='docs status' /></a>
<a href="https://img.shields.io/github/license/daniel-mizsak/python-package-template" target="_blank"><img src="https://img.shields.io/github/license/daniel-mizsak/python-package-template" alt="license"></a>
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
- [Hatch](https://hatch.pypa.io/latest/) - Package building
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

Codecov is set up to be part of the [tox reusable workflow](https://github.com/daniel-mizsak/workflows/blob/main/.github/workflows/tox.yml), but for this action it is important to generate the coverage report using the `--cov-report=xml` flag in the `pyproject.toml` file.

### Pre-Commit
Pre-Commit is used to run certain checks on the code before it is committed.\
These checks are defined in the `.pre-commit-config.yaml` file.\
To use pre-commit is has to be installed in the virtual environment and also added to the git hooks by running `pre-commit install`.

In this repository pre-commit is set up for a number of general issues and to run formatting and linting checks with `ruff`.

Call pre-commit by running:

```bash
pre-commit run --all-files
```

### Hatch
Hatch is primarily used to build the package, but it can also be used to run certain tests in isolated environments.\
If the package building is more complex and requires additional settings or files it is recommended to read the hatch documentation.\
In this repository hatch is set up with the local path of the package as it differs from the one specified in the `pyproject.toml` file which is used for publishing to PyPI.

The isolated environment settings for hatch are defined in the `hatch.toml` file.\
I was thinking about replacing `tox` with `hatch`, but for now `tox` fits more into my workflows.

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
Tox is useful for running the above tools in an isolated environment.\
It makes sure that the package setup is consistent and that the tools are working as expected.\
It can be used to test different python versions and different testing scenarios.

In this repository tox is set up to use python 3.11, 3.12 and run pytest, ruff, mypy and documentation tests.
The settings are specified in the `tox.ini` file.

Call tox by running:

```bash
tox
```

### Documentation
The documentation is built with Sphinx and it is hosted both on ReadTheDocs and GitHub Pages.\
Both of these services are recommended, however ReadTheDocs requires a bit more setup, but I prefer it as it does not require an extra feature branch to be present.

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

Environments:\
`pypi`

- Deployment protection rules:
- Required reviewers:
    `daniel-mizsak`
- Allow administrators to bypass configured protection rules

<br>

Pages/Build and deployment:

- Source: Deploy from branch
- Branch: `gh-pages` (root)

## Setup PyPi trusted publishing
[PyPI publishing settings](https://pypi.org/manage/account/publishing/)

Add a new pending publisher:

- PyPI Project Name: `python-package-template-pypi` (has to match the project name in `pyproject.toml`)
- Owner: `daniel-mizsak`
- Repository name: `python-package-template`
- Workflow name: `release.yml`

(I am currently not using trusted publishing, as it does not support getting called from a reusable GitHub workflow.\
Instead, I am calling my [PyPI publishing workflow](https://github.com/daniel-mizsak/workflows/blob/main/.github/workflows/pypi.yml) with an API token.)

## More examples
I am trying to use this template in all of my repositories and also contribute back here with new best practices I find.
Some of my other repositories that may be interesting to look at:
- [falcon-formation](https://github.com/daniel-mizsak/falcon-formation) - Create evenly distributed hockey teams.
- [checkmark](https://github.com/daniel-mizsak/checkmark) - Automated assessment generator and evaluator system.
- [pythonvilag-website](https://github.com/PythonVilag/pythonvilag-website) - Source code that powers the Python Világ website.
- [private-lecture-automation](https://github.com/PythonVilag/private-lecture-automation) - Automation tools for private lecture management.

I have also integrated some of the above mentioned tools into my `vscode` settings. You can find them in my [macos-setup](https://github.com/daniel-mizsak/macos-setup/blob/main/dotfiles/vscode/settings.json) repository.
