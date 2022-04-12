"""Contains the implementation of the Date class"""

from typing import Any, Optional


class Date:
    """Date implementation"""

    def __init__(self, day: Optional[int] = None, month: Optional[int] = None, year: Optional[int] = None):
        """Initialise Date object"""

        self.year: int = year if year is not None else 1900
        self.month: int = month if month is not None else 1
        self.day: int = day if day is not None else 1

    @property
    def day(self) -> int:
        """Getter for days"""

        return self._day

    @day.setter
    def day(self, other: int):
        """Setter for days"""

        if other > self.days_in_month():
            raise ValueError(f"{other} is not a valid day count for the given month")
        self._day = other

    @property
    def month(self) -> int:
        """Getteer for months"""

        return self._month

    @month.setter
    def month(self, other: int):
        """Setter for months"""

        if not 1 <= other <= 12:
            raise ValueError(f"{other} is not a valid month")
        self._month = other

    @property
    def year(self) -> int:
        """Getter for years"""

        return self._year

    @year.setter
    def year(self, other: int):
        """Setter for years"""

        self._year = other

    def __str__(self) -> str:
        """String representation for date"""

        return f"{self.day}/{self.month}/{self.year}"

    def __gt__(self, other: Any):
        """Implement greater than for Date objects"""

        if isinstance(other, Date):
            if self.year > other.year:
                return True
            if self.year == other.year and self.month > other.month:
                return True
            if self.year == other.year and self.month == other.month and self.day > other.day:
                return True
        return False

    def __ge__(self, other: Any) -> bool:
        """Implement greater than or equal for Date objects"""

        return self > other or self == other

    def __le__(self, other: Any) -> bool:
        """Implement less than or equal for Date objects"""

        return self < other or self == other

    def __lt__(self, other: Any) -> bool:
        """Implement less than for Date objects"""

        if isinstance(other, Date):
            return not self >= other
        return False

    def __eq__(self, other: Any) -> bool:
        """Check for date object equality"""

        if isinstance(other, Date):
            return (
                self.year == other.year
                and self.month == other.month
                and self.day == other.day
            )
        return False

    def days_in_month(self) -> int:
        """Count the days in a given month"""

        max_days = 31
        if self.month == 2:
            max_days = 28
            if self.leap_year():
                max_days += 1
        elif self.month in {4, 6, 9, 11}:
            max_days = 30
        return max_days

    def next_day(self, previous: Optional['Date'] = None):
        """Move to the next day"""

        if previous is not None:
            self.year = previous.year
            self.month = previous.month
            self.day = previous.day

        if self.day + 1 > self.days_in_month():
            if self.month + 1 > 12:
                self.year += 1
                self.month = 1
            else:
                self.month += 1
            self.day = 1
        else:
            self.day += 1

    def print(self):
        """Print the current day"""

        print(self)

    def leap_year(self) -> bool:
        """Check if the current year is a leap year"""

        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False

        return self.year % 4 == 0

    def days_between(self, other: 'Date') -> int:
        """Return the number of days between two given date objects"""

        days = 0

        destination = self
        start = Date(other.day, other.month, other.year)
        if self < other:
            destination = other
            start = Date(self.day, self.month, self.year)

        while start < destination:
            start.next_day()
            days += 1
            print(start, destination)

        return days

    def days_since_new_year(self) -> int:
        """Return the number of days since new year"""

        new_year = Date(1, 1, self.year)
        return self.days_between(new_year)


def week_later(date: Date) -> Date:
    """Return a new Date object a week later from the given date"""

    new_date = Date(date.day, date.month, date.year)
    for _ in range(7):
        new_date.next_day()
    return new_date
