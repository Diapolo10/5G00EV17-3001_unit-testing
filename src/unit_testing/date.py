"""Contains the implementation of the Date class."""

from __future__ import annotations

from enum import IntEnum

DEFAULT_DAY = 1
DEFAULT_MONTH = 1
DEFAULT_YEAR = 1900
DAYS_IN_FEBRUARY = 28
DAYS_IN_OTHER_MONTHS = 30
MAX_DAYS_IN_MONTH = 31


class Months(IntEnum):
    """Enum for months."""

    JANUARY   = 1
    FEBRUARY  = 2
    MARCH     = 3
    APRIL     = 4
    MAY       = 5
    JUNE      = 6
    JULY      = 7
    AUGUST    = 8
    SEPTEMBER = 9
    OCTOBER   = 10
    NOVEMBER  = 11
    DECEMBER  = 12


class Date:
    """Date implementation."""

    def __init__(self: Date, day: int | None = None, month: int | None = None, year: int | None = None) -> None:
        """Initialise Date object."""
        self.year: int = year if year is not None else DEFAULT_YEAR
        self.month: int = month if month is not None else DEFAULT_MONTH
        self.day: int = day if day is not None else DEFAULT_DAY

    @property
    def day(self: Date) -> int:
        """Getter for days."""
        return self._day

    @day.setter
    def day(self: Date, other: int) -> None:
        """Setter for days."""
        if other > self.days_in_month():
            msg = f"{other} is not a valid day count for the given month"
            raise ValueError(msg)
        self._day = other

    @property
    def month(self: Date) -> int:
        """Getter for months."""
        return self._month

    @month.setter
    def month(self: Date, other: int) -> None:
        """Setter for months."""
        if not Months.JANUARY <= other <= Months.DECEMBER:
            msg = f"{other} is not a valid month"
            raise ValueError(msg)
        self._month = other

    @property
    def year(self: Date) -> int:
        """Getter for years."""
        return self._year

    @year.setter
    def year(self: Date, other: int) -> None:
        """Setter for years."""
        self._year = other

    def __str__(self: Date) -> str:
        """Date string representation."""
        return f"{self.day}/{self.month}/{self.year}"

    def __gt__(self: Date, other: object) -> bool:
        """Implement greater than for Date objects."""
        if isinstance(other, Date):
            if self.year > other.year:
                return True
            if self.year == other.year and self.month > other.month:
                return True
            if self.year == other.year and self.month == other.month and self.day > other.day:
                return True
        return False

    def __ge__(self: Date, other: object) -> bool:
        """Implement greater than or equal for Date objects."""
        return self > other or self == other

    def __le__(self: Date, other: object) -> bool:
        """Implement less than or equal for Date objects."""
        return self < other or self == other

    def __lt__(self: Date, other: object) -> bool:
        """Implement less than for Date objects."""
        if isinstance(other, Date):
            return not self >= other
        return False

    def __eq__(self: Date, other: object) -> bool:
        """Check for date object equality."""
        if isinstance(other, Date):
            return hash(self) == hash(other)

        return False

    def __hash__(self: Date) -> int:
        """Hash the Date object."""
        return hash((self.year, self.month, self.day))

    def days_in_month(self: Date) -> int:
        """Count the days in a given month."""
        max_days = MAX_DAYS_IN_MONTH
        if self.month == Months.FEBRUARY:
            max_days = DAYS_IN_FEBRUARY
            if self.leap_year():
                max_days += 1
        elif self.month in {Months.APRIL, Months.JUNE, Months.SEPTEMBER, Months.NOVEMBER}:
            max_days = DAYS_IN_OTHER_MONTHS
        return max_days

    def next_day(self: Date, previous: Date | None = None) -> None:
        """Move to the next day."""
        if previous is not None:
            self.year = previous.year
            self.month = previous.month
            self.day = previous.day

        if self.day + 1 > self.days_in_month():
            if self.month + 1 > Months.DECEMBER:
                self.year += 1
                self.month = 1
            else:
                self.month += 1
            self.day = 1
        else:
            self.day += 1

    def print(self: Date) -> None:
        """Print the current day."""
        print(self)  # noqa: T201

    def leap_year(self: Date) -> bool:
        """Check if the current year is a leap year."""
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False

        return self.year % 4 == 0

    def days_between(self: Date, other: Date) -> int:
        """Return the number of days between two given date objects."""
        days = 0

        destination = self
        start = Date(other.day, other.month, other.year)
        if self < other:
            destination = other
            start = Date(self.day, self.month, self.year)

        while start < destination:
            start.next_day()
            days += 1

        return days

    def days_since_new_year(self: Date) -> int:
        """Return the number of days since new year."""
        new_year = Date(1, 1, self.year)
        return self.days_between(new_year)


def week_later(date: Date) -> Date:
    """Return a new Date object a week later from the given date."""
    new_date = Date(date.day, date.month, date.year)
    for _ in range(7):
        new_date.next_day()
    return new_date
