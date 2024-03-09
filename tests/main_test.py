"""
Tests for the main module.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

from python_package_template.main import add_five


def test_add_five() -> None:
    assert add_five(5) == 10
    assert add_five(0) == 5
    assert add_five(-5) == 0
