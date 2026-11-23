"""
Nox configuration file for testing against multiple python versions.

Copyright (C) 2026 "Daniel Mizsak" <daniel@mizsak.com>
"""

import nox

python_versions = nox.project.python_versions(nox.project.load_toml("pyproject.toml"))


@nox.session(python=python_versions, venv_backend="uv")
def test_supported_python_version(session: nox.Session) -> None:
    """Run the test suite."""
    session.run_install(
        "uv",
        "sync",
        "--quiet",
        f"--python={session.virtualenv.location}",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
    session.run("pytest")
