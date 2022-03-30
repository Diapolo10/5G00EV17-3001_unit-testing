"""Stub unit test file"""

import pytest

from unit_testing import date

@pytest.fixture
def default_date():
    return date.Date()


def test_default_attributes(default_date):
    assert default_date.day == 1
    assert default_date.month == 1
    assert default_date.year == 1900


def test_default_methods(default_date):
    assert default_date.leap_year() == False
    
    default_date.next_day()

    assert default_date.day == 2
    assert default_date.month == 1
    assert default_date.year == 1900


def test_year_change():
    d = date.Date(31, 12, 1999)
    d.next_day()

    assert d.day == 1
    assert d.month == 1
    assert d.year == 2000
    assert d.leap_year() == True


def test_month_change():
    d = date.Date(28, 2, 2001)
    d.next_day()

    assert d.day == 1
    assert d.month == 3
    assert d.year == 2001


def test_date_error():
    with pytest.raises(ValueError):
        d = date.Date(31, 2, 2020)


def test_month_error():
    with pytest.raises(ValueError):
        d = date.Date(7, 21, 1998)
