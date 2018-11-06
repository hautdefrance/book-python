from datetime import datetime
from pytz import utc


gagarin = datetime(1961, 4, 12, 14, 7)      # timezone naive


in_utc = utc.localize(gagarin, is_dst=None)
# datetime.datetime(1961, 4, 12, 14, 7, tzinfo=<UTC>)

print(f'{in_utc:%Y-%m-%d %H:%M:%S %z}')
# 1961-04-12 14:07:00 +0000
