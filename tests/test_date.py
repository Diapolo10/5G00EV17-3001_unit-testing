"""Unit tests for the date.Date class"""

import pytest

from unit_testing.date import Date, week_later

DEFAULT_DAY = 1
DEFAULT_MONTH = 1
DEFAULT_YEAR = 1900


def test_date_default_attributes(default_date):
    """Tests the default state of the date object"""

    assert default_date.day == DEFAULT_DAY
    assert default_date.month == DEFAULT_MONTH
    assert default_date.year == DEFAULT_YEAR


def test_date_default_methods(default_date):
    """Tests the methods on a default date object"""

    assert default_date.leap_year() is False

    default_date.next_day()

    assert default_date.day == DEFAULT_DAY+1
    assert default_date.month == DEFAULT_MONTH
    assert default_date.year == DEFAULT_YEAR


def test_date_next_day(default_date):
    """Tests setting the 'previous'-parameter for Date.next_day"""

    date = Date(30, 3, 2022)
    default_date.next_day(previous=date)

    assert default_date.day == 31
    assert default_date.month == 3
    assert default_date.year == 2022


def test_date_year_change():
    """Tests if year change is correctly implemented"""

    date = Date(31, 12, 1999)
    date.next_day()

    assert date.day == 1
    assert date.month == 1
    assert date.year == 2000
    assert date.leap_year() is True


def test_date_month_change():
    """Tests if month change is correctly implemented"""

    date = Date(28, 2, 2001)
    date.next_day()

    assert date.day == 1
    assert date.month == 3
    assert date.year == 2001


def test_date_day_error():
    """Tests that invalid days raise an error"""

    with pytest.raises(ValueError):
        Date(31, 2, 2020)


def test_date_month_error():
    """Tests that invalid months raise an error"""

    with pytest.raises(ValueError):
        Date(7, 21, 1998)


def test_date_print(default_date, capsys):
    """'Tests' the printing functionality"""

    default_date.print()
    captured = capsys.readouterr()
    assert captured.out == f'{DEFAULT_DAY}/{DEFAULT_MONTH}/{DEFAULT_YEAR}\n'


def test_date_comparisons():
    """Tests comparison operators for Date objects"""

    date_1 = Date(1, 1, 2000)
    date_2 = Date(6, 1, 2000)
    date_3 = Date(24, 12, 1999)
    date_4 = Date(2, 2, 2000)
    date_5 = Date(1, 1, 2000)

    assert date_1 < date_2
    assert date_2 > date_1
    assert date_1 <= date_2
    assert date_2 >= date_1

    assert date_1 > date_3
    assert date_3 < date_1
    assert date_1 >= date_3
    assert date_3 <= date_1

    assert date_1 < date_4
    assert date_4 > date_1
    assert date_1 <= date_4
    assert date_4 >= date_1

    assert date_1 == date_5
    assert date_1 <= date_5
    assert date_1 >= date_5

    assert (date_1 < None) is False
    assert (date_1 > None) is False
    assert (date_1 <= None) is False
    assert (date_1 >= None) is False
    assert (date_1 == 'foo') is False


def test_date_leap_year():
    """Tests that leap years are correctly implemented"""

    date_1 = Date(1, 1, 2000)
    date_2 = Date(1, 1, 2100)
    date_3 = Date(1, 1, 2004)
    date_4 = Date(1, 1, 2001)

    assert date_1.leap_year() is True
    assert date_2.leap_year() is False
    assert date_3.leap_year() is True
    assert date_4.leap_year() is False


def test_date_days_between():
    """Tests calculating difference in days betweeen dates"""

    date_1 = Date(24, 1, 1998)
    date_2 = Date(31, 1, 1998)
    date_3 = Date(5, 2, 1998)
    date_4 = Date(24, 1, 2005)

    assert date_1.days_between(date_2) == 7
    assert date_1.days_between(date_3) == 12
    assert date_1.days_between(date_4) == 2557
    assert date_4.days_between(date_1) == 2557


def test_date_days_since_new_year():
    """Tests calculating number of days since the last new year"""

    date_1 = Date(31, 1, 2022)
    date_2 = Date(31, 12, 2022)

    assert date_1.days_since_new_year() == 30
    assert date_2.days_since_new_year() == 364


def test_week_later(default_date):
    """Tests calculating the data a week later"""

    new_date = week_later(default_date)

    assert new_date.day == DEFAULT_DAY+7
    assert new_date.month == DEFAULT_MONTH
    assert new_date.year == DEFAULT_YEAR
