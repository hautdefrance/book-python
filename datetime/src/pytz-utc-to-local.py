from datetime import datetime
from pytz import timezone, utc


armstrong = datetime(1969, 7, 21, 14, 56, 15, tzinfo=utc)


utc_time = armstrong.astimezone(utc)
# datetime.datetime(1969, 7, 21, 14, 56, 15, tzinfo=<UTC>)

print(f'{utc_time:%Y-%m-%d %H:%M:%S %Z%z}')
# 1969-07-21 14:56:15 UTC+0000


waw_time = armstrong.astimezone(timezone('Europe/Warsaw'))
# datetime.datetime(1969, 7, 21, 15, 56, 15, tzinfo=<DstTzInfo 'Europe/Warsaw' CET+1:00:00 STD>)

print(f'{waw_time:%Y-%m-%d %H:%M:%S %Z%z}')
# 1969-07-21 15:56:15 CET+0100
