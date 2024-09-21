"""
Main module of the package.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

import numpy as np


def add_five(x: int) -> int:
    """Increment the input by 5.

    Args:
        x (int): The input number.

    Returns:
        int: The input incremented by 5.
    """
    return x + 5


def subtract_three(x: int) -> int:
    """Decrement the input by 3.

    Args:
        x (int): The input number.

    Returns:
        int: The input decremented by 3.
    """
    return int(np.subtract(x, 3))
