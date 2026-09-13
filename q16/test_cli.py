import sys

import pytest

from greetlab.cli import main


def test_normal_name(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["cli", "--name", "Alice"])
    main()
    captured = capsys.readouterr()
    assert "Hello, Alice!" in captured.out


def test_blank_name_exits(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["cli", "--name", "   "])
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 2
