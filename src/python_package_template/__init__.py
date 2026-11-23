"""
Python package template configuration.

Copyright (C) 2026 "Daniel Mizsak" <daniel@mizsak.com>
"""

from importlib.metadata import version

from python_package_template.main import add_five, subtract_three

__version__ = version("python-package-template-pypi")

__all__ = [
    "__version__",
    "add_five",
    "subtract_three",
]
