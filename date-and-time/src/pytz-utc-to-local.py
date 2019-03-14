from datetime import datetime
from pytz import timezone, utc


warsaw = timezone('Europe/Warsaw')
armstrong = datetime(1969, 7, 21, 14, 56, 15, tzinfo=utc)


armstrong.astimezone(warsaw)
# datetime.datetime(1969, 7, 21, 15, 56, 15,
#                   tzinfo=<DstTzInfo 'Europe/Warsaw' CET+1:00:00 STD>)
