"""
Tests for the main module.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

from python_package_template.main import add_five, subtract_three


def test_add_five() -> None:
    assert add_five(5) == 10
    assert add_five(0) == 5
    assert add_five(-5) == 0


def test_subtract_three() -> None:
    assert subtract_three(5) == 2
    assert subtract_three(0) == -3
    assert subtract_three(-5) == -8
