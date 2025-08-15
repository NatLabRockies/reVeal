# -*- coding: utf-8 -*-
"""
pytest fixtures
"""
import pytest
from click.testing import CliRunner

from loci import PACKAGE_DIR

TEST_DATA_DIR = PACKAGE_DIR.parent.joinpath("tests", "data")


@pytest.fixture
def data_dir():
    """Return path to test data directory"""
    return TEST_DATA_DIR


@pytest.fixture
def cli_runner():
    """Return a click CliRunner for testing commands"""
    return CliRunner()
