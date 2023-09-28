"""

    06_using_datetime.py
    Working with date, datetime objects.

"""

from datetime import date, datetime


now1 = datetime.now()      # current date & time
now2 = date.today()        # current date
print(now1, now2)

d = date(2023, 2, 17)
print(d.year, d.month, d.day)

dt_fmt = d.strftime('Day %d of %B, Day %j in %Y')
print(dt_fmt)

d2 = date(2024, 6, 7)
print(d2 - d)
