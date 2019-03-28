from datetime import datetime
from pytz import timezone, utc


class TimeConverter:
    def __get__(self, parent, type):
        return parent.utc.astimezone(self.tz)

    def __set__(self, parent, value):
        parent.utc = self.tz.localize(value).astimezone(utc)

    def __del__(self, parent):
        parent.utc = datetime(1, 1, 1)


class EuropeWarsaw(TimeConverter):
    tz = timezone('Europe/Warsaw')


class EuropeMoscow(TimeConverter):
    tz = timezone('Europe/Moscow')


class Time:
    warsaw = EuropeWarsaw()
    moscow = EuropeMoscow()

    def __init__(self, dt=datetime.now(tz=utc)):
        self.utc = dt


now = Time()

print(now.warsaw)
# 2019-03-28 13:07:14.486365+01:00

now.warsaw = datetime(2019, 3, 28, 13, 00, 00)

print(now.utc)
# 2019-03-28 12:00:00+00:00

print(now.moscow)
# 2019-03-28 15:00:00+03:00
