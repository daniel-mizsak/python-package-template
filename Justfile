@_:
    just --list --unsorted

[group("lifecycle")]
clean:
    rm -rf \
        .artifacts \
        .cache \
        .coverage \
        .mypy_cache \
        .nox \
        .pytest_cache \
        .ruff_cache \
        coverage.xml \
        htmlcov \
        .venv
    find . -name ".DS_Store" -type f -delete
    find . -type d -name "__pycache__" -exec rm -r {} +

[group("lifecycle")]
install *args:
    uv sync --all-groups {{ args }}

[group("lifecycle")]
upgrade:
    just install --upgrade

[group("lifecycle")]
fresh: clean install

[group("qa")]
lint:
    uv run ruff check
    uv run ruff format --diff

[group("qa")]
type:
    uv run mypy .

[group("qa")]
test *args:
    uv run pytest {{ args }}

[group("qa")]
test-all-python:
    uv run nox

[group("qa")]
coverage:
    uv run coverage run --source=tests --module pytest
    uv run coverage report --fail-under=100 --show-missing

    uv run coverage run --source=python_package_template --module pytest
    uv run coverage report --show-missing
    uv run coverage xml -o .artifacts/coverage.xml
    uv run coverage html -d .artifacts/htmlcov

[group("qa")]
check-all: lint type test-all-python coverage

[group("qa-extra")]
megalinter:
    npx mega-linter-runner --flavor cupcake --env "MEGALINTER_CONFIG=.github/linters/.megalinter.yml"

[group("qa-extra")]
pre-commit:
    uv run pre-commit run --all-files

[group("build")]
build-documentation:
    uv run zensical build --clean --strict

[group("build")]
build-package:
    uv build --out-dir .artifacts/dist

[group("build")]
build-all: build-documentation build-package

[group("serve")]
serve-documentation:
    uv run zensical serve --open
