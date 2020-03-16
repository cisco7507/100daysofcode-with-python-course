#! env python
from datetime import datetime, timedelta, date

print(
    'Problem 1: We kicked off our 100 Days of Code project on March 30th, 2017. Calculate what date we finished the full 100 days!')
print('Solution:')
kicked_off_date = datetime(2017, 3, 30)
delta = timedelta(days=100)
finish_date = kicked_off_date + delta
print(f'Code project started on {kicked_off_date.date()} finalizing 100 days later on: {finish_date.date()}')

print(
    "Problem 2: PyBites was founded on the 19th of December 2016. We're attending our first PyCon together on May 8th, 2018. Can you calculate how many days from PyBites' inception to our first PyCon meet up?")
print('Solution:')

foundation_date = datetime(2016,12,19)
first_pycon = datetime(2018,5,8)
delta_days = first_pycon - foundation_date
print(f'{delta_days.days} days')
