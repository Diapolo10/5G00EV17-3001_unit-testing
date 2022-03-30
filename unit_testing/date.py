"""Contains the implementation of the Date class"""

from typing import Optional

class Date:
    def __init__(self, day: Optional[int] = None, month: Optional[int] = None, year: Optional[int] = None):
        self.year = year if year is not None else 1900
        self.month = month if month is not None else 1
        self.day = day if day is not None else 1

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, other):
        if other > self.days_in_month():
            raise ValueError(f"{other} is not a valid day count for the given month")
        self._day = other

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, other):
        if not 1 <= other <= 12:
            raise ValueError(f"{other} is not a valid month")
        self._month = other

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, other):
        self._year = other

    def days_in_month(self):
        max_days = 31
        if self.month == 2:
            max_days = 28
        elif self.month in {4, 6, 9, 11}:
            max_days = 30
        return max_days

    def next_day(self):
        
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
        print(self)

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

    def leap_year(self):

        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True

        return False
