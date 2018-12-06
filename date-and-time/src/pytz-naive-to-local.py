from datetime import datetime
from pytz import utc, timezone


gagarin = datetime(1961, 4, 12, 14, 7)  # timezone naive


gagarin = timezone('Asia/Almaty').localize(gagarin, is_dst=None)
# datetime.datetime(1961, 4, 12, 14, 7,
#                   tzinfo=<DstTzInfo 'Asia/Almaty' +06+6:00:00 STD>)


print(f'{gagarin:%Y-%m-%d %H:%M:%S %z}')
# 1961-04-12 14:07:00 +0600
