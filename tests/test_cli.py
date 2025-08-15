# -*- coding: utf-8 -*-
"""Tests for CLI"""
import pytest

from loci.cli import main


def test_main(cli_runner):
    """Test main() CLI command."""
    result = cli_runner.invoke(main, "--help")
    assert result.exit_code == 0, f"Command failed with error {result.exception}"


if __name__ == "__main__":
    pytest.main([__file__, "-s"])
