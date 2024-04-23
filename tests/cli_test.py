"""
Tests for the CLI module.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

from typing import Any

from python_package_template.cli import main


def test_main(monkeypatch: Any, capsys: Any) -> None:  # noqa: ANN401
    cli_arguments = ["", "7"]  # sys.argv[0] is the name of the script
    monkeypatch.setattr("sys.argv", cli_arguments)
    main()

    captured = capsys.readouterr()
    assert "Adding 5 to 7 gives 12." in captured.out
    assert "Subtracting 3 from 7 gives 4." in captured.out
