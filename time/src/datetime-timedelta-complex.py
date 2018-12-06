from datetime import datetime, timedelta, date


armstrong = datetime(1969, 7, 21, 14, 56, 15)

duration = timedelta(
    weeks=3,
    days=2,
    hours=21,
    minutes=5,
    seconds=12,
    milliseconds=10,
    microseconds=55,
)

armstrong - duration
