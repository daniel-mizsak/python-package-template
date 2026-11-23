"""
Tests for the main module.

Copyright (C) 2026 "Daniel Mizsak" <daniel@mizsak.com>
"""

import pytest

from python_package_template.main import add_five, subtract_three


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        pytest.param(5, 10, id="positive"),
        pytest.param(0, 5, id="zero"),
        pytest.param(-5, 0, id="negative"),
    ],
)
def test_add_five__increments_input_by_five(number, expected) -> None:
    result = add_five(number)

    assert result == expected


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        pytest.param(5, 2, id="positive"),
        pytest.param(0, -3, id="zero"),
        pytest.param(-5, -8, id="negative"),
    ],
)
def test_subtract_three__decrements_input_by_three(number, expected) -> None:
    result = subtract_three(number)

    assert result == expected
