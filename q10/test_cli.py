import pytest
from greetlab.cli import main
import sys

def test_blank_name_exits(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['cli', '--name', '   '])
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 2
