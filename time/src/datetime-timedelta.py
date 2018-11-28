from datetime import datetime, timedelta, date


sputnik = date(1957, 10, 4)
gagarin = datetime(1961, 4, 12)
armstrong = datetime(1969, 7, 21, 14, 56, 15)


datetime.now() - timedelta(hours=3)
armstrong = datetime(1969, 7, 21, 14, 56, 15)
date(1961, 4, 12) - timedelta(days=3)

month_before = date(1961, 4, 12) - MONTH
# datetime.date(1961, 3, 13)
