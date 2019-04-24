"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# if no input use datetime

date = input('Enter the date: ')
list_date = date.split()


def get_date(date):
    c = calendar.TextCalendar()
    year = datetime.now().year
    if len(date) == 0:
        month = datetime.now().month
        return c.prmonth(year, month)
    elif len(date) == 1:
        return c.prmonth(year, int(date[0]))
    elif len(date) == 2:
        return c.prmonth(int(date[1]), int(date[0]))
    else:
        return 'make sure you enter date as: month year'


print(get_date(list_date))
