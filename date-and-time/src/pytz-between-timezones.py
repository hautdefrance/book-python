from datetime import datetime
from pytz import utc, timezone


gagarin = datetime(1961, 4, 12, 14, 7, tzinfo=timezone('Asia/Almaty'))

in_utc = gagarin.astimezone(utc)                        # datetime.datetime(1961, 4, 12, 8, 59, tzinfo=<UTC>)
print(f'{in_utc:%Y-%m-%d %H:%M:%S %z}')               # 1961-04-12 08:59:00 +0000

in_waw = gagarin.astimezone(timezone('Europe/Warsaw'))  # datetime.datetime(1961, 4, 12, 9, 59, tzinfo=<DstTzInfo 'Europe/Warsaw' CET+1:00:00 STD>)
print(f'{in_waw:%Y-%m-%d %H:%M:%S %z}')               # 1961-04-12 09:59:00 +0100
