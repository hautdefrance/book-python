from datetime import datetime
from pytz import utc, timezone


gagarin = datetime(1961, 4, 12, 14, 7, tzinfo=timezone('Asia/Almaty'))
in_utc = gagarin.astimezone(utc)
in_waw = gagarin.astimezone(timezone('Europe/Warsaw'))


print(f'{in_utc:%Y-%m-%d %H:%M:%S %Z%z}')
# 1961-04-12 08:59:00 UTC+0000

print(f'{in_waw:%Y-%m-%d %H:%M:%S %Z%z}')
# 1961-04-12 09:59:00 CET+0100
