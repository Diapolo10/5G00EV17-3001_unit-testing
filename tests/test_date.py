"""Unit tests for the date.Date class"""

import pytest

from unit_testing import date


@pytest.fixture
def default_date():
    """Creates a default date.Date object for testing"""

    return date.Date()


def test_date_default_attributes(default_date):
    """Tests the default state of the date object"""

    assert default_date.day == 1
    assert default_date.month == 1
    assert default_date.year == 1900


def test_date_default_methods(default_date):
    """Tests the methods on a default date object"""

    assert default_date.leap_year() is False

    default_date.next_day()

    assert default_date.day == 2
    assert default_date.month == 1
    assert default_date.year == 1900


def test_date_next_day(default_date):
    d1 = date.Date(30, 3, 2022)
    default_date.next_day(previous=d1)

    assert default_date.day == 31
    assert default_date.month == 3
    assert default_date.year == 2022


def test_date_year_change():
    """Tests if year change is correctly implemented"""

    d = date.Date(31, 12, 1999)
    d.next_day()

    assert d.day == 1
    assert d.month == 1
    assert d.year == 2000
    assert d.leap_year() is True


def test_date_month_change():
    """Tests if month change is correctly implemented"""

    d = date.Date(28, 2, 2001)
    d.next_day()

    assert d.day == 1
    assert d.month == 3
    assert d.year == 2001


def test_date_day_error():
    """Tests that invalid days raise an error"""

    with pytest.raises(ValueError):
        _ = date.Date(31, 2, 2020)


def test_date_month_error():
    """Tests that invalid months raise an error"""

    with pytest.raises(ValueError):
        _ = date.Date(7, 21, 1998)


def test_date_print(default_date, capsys):
    """'Tests' the printing functionality"""

    default_date.print()
    captured = capsys.readouterr()
    assert captured.out == '1/1/1900\n'


def test_date_comparisons():
    d1 = date.Date(1, 1, 2000)
    d2 = date.Date(6, 1, 2000)
    d3 = date.Date(24, 12, 1999)
    d4 = date.Date(2, 2, 2000)
    d5 = date.Date(1, 1, 2000)

    assert d1 < d2
    assert d2 > d1
    assert d1 <= d2
    assert d2 >= d1

    assert d1 > d3
    assert d3 < d1
    assert d1 >= d3
    assert d3 <= d1

    assert d1 < d4
    assert d4 > d1
    assert d1 <= d4
    assert d4 >= d1

    assert d1 == d5
    assert d1 <= d5
    assert d1 >= d5

    assert (d1 < None) is False
    assert (d1 > None) is False
    assert (d1 <= None) is False
    assert (d1 >= None) is False
    assert (d1 == 'foo') is False


def test_date_leap_year():
    """Tests that leap years are correctly implemented"""

    d1 = date.Date(1, 1, 2000)
    d2 = date.Date(1, 1, 2100)
    d3 = date.Date(1, 1, 2004)
    d4 = date.Date(1, 1, 2001)

    assert d1.leap_year() is True
    assert d2.leap_year() is False
    assert d3.leap_year() is True
    assert d4.leap_year() is False


def test_date_days_between():
    """Tests calculating difference in days betweeen dates"""

    d1 = date.Date(24, 1, 1998)
    d2 = date.Date(31, 1, 1998)
    d3 = date.Date(5, 2, 1998)
    d4 = date.Date(24, 1, 2005)

    assert d1.days_between(d2) == 7
    assert d1.days_between(d3) == 12
    assert d1.days_between(d4) == 2557
    assert d4.days_between(d1) == 2557


def test_date_days_since_new_year():
    d = date.Date(31, 1, 2022)
    d1 = date.Date(31, 12, 2022)
    assert d.days_since_new_year() == 30
    assert d1.days_since_new_year() == 364


def test_week_later(default_date):
    new_date = date.week_later(default_date)

    assert new_date.day == 8
    assert new_date.month == 1
    assert new_date.year == 1900
