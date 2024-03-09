"""
Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

Built docs locally with:
sphinx-build -b html docs/source/ docs/build/html

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

from datetime import UTC, datetime

from python_package_template import __version__

# Project
author = "Daniel Mizsak"
project = "python-package-template"
copyright = f"{datetime.now(tz=UTC).year} {author}"  # noqa: A001
version = __version__

# General
master_doc = "index"
source_suffix = ".rst"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_copybutton",
]
nitpicky = True

# HTML
html_theme = "furo"
html_title = "python-package-template"
pygments_style = "sphinx"
pygments_dark_style = "monokai"
html_static_path = ["_static"]
