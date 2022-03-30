"""Stub unit test file"""

import pytest

from unit_testing import date

@pytest.fixture
def default_date():
    return date.Date()


def test_default_atttributes(default_date):
    assert default_date.day == 1
    assert default_date.month == 1
    assert default_date.year == 1900


def test_default_methods(default_date):
    assert default_date.leap_year() == False
    
    default_date.next_day()

    assert default_date.day == 2
    assert default_date.month == 1
    assert default_date.year == 1900
