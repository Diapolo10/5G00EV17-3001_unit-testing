"""Fixtures for use in test cases."""

import pytest

from unit_testing import date


@pytest.fixture()
def default_date() -> date.Date:
    """Create a default date.Date object for testing."""
    return date.Date()
