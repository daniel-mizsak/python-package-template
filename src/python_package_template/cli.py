"""
Command line interface for the Python package template.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

import argparse

from python_package_template.main import add_five, subtract_three


def main() -> None:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(description="Run the PPT CLI.")

    parser.add_argument("number", type=int, help="The number to run the operations on.")
    args = parser.parse_args()

    plus_five = add_five(args.number)
    print(f"Adding 5 to {args.number} gives {plus_five}.")  # noqa: T201

    minus_three = subtract_three(args.number)
    print(f"Subtracting 3 from {args.number} gives {minus_three}.")  # noqa: T201
