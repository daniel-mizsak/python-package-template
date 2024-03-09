"""
Init file for the package.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

import importlib.metadata

from python_package_template.main import add_five

__all__ = ["add_five"]
__version__ = importlib.metadata.version("python-package-template-pypi")
