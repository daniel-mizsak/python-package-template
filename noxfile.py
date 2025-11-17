"""
Nox configuration file for testing against multiple python versions.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

import nox

python_versions = ["3.12", "3.13", "3.14"]


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
