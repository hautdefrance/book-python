from datetime import datetime, date, time


d1 = date(1969, 7, 21)
t1 = time(14, 56, 15)

dt1 = datetime(
    year=d1.year,
    month=d1.month,
    day=d1.day,
    hour=t1.hour,
    minute=t1. minute,
    second=t1.second)
# datetime.datetime(1969, 7, 21, 14, 56, 15)


dt2 = datetime(d1.year, d1.month, d1.day, t1.hour, t1. minute, t1.second)
# datetime.datetime(1969, 7, 21, 14, 56, 15)
