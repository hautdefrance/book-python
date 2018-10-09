from datetime import datetime
from pytz import utc, timezone


warsaw = timezone('Europe/Warsaw')
gagarin = datetime(1961, 4, 12, 14, 7)


in_utc = utc.localize(gagarin, is_dst=None)
# datetime.datetime(1961, 4, 12, 14, 7, tzinfo=<UTC>)

in_waw = warsaw.localize(gagarin, is_dst=None)
# datetime.datetime(1961, 4, 12, 14, 7, tzinfo=<DstTzInfo 'Europe/Warsaw' CET+1:00:00 STD>)
