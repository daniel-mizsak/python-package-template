"""
Main module of the package.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

import numpy as np


def add_five(number: int) -> int:
    """Increment the input by 5.

    Args:
        number (int): The input number.

    Returns:
        int: The input incremented by 5.
    """
    return number + 5


def subtract_three(number: int) -> int:
    """Decrement the input by 3.

    Args:
        number (int): The input number.

    Returns:
        int: The input decremented by 3.
    """
    return int(np.subtract(number, 3))
