from datetime import datetime, timedelta


armstrong = datetime(1969, 7, 21, 14, 56, 15)

duration = timedelta(
    weeks=3,
    days=2,
    hours=21,
    minutes=5,
    seconds=12,
    milliseconds=10,
    microseconds=55)
# datetime.timedelta(days=23, seconds=75912, microseconds=10055)


between_dates = armstrong - duration
# datetime.datetime(1969, 6, 27, 17, 51, 2, 989945)
