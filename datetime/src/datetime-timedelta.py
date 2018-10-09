from datetime import datetime, timedelta, date

# Average days a month in solar calendar
MONTH = timedelta(days=30.436875)


datetime.now() - timedelta(hours=3)
date(1961, 4, 12) - timedelta(days=3)

month_before = date(1961, 4, 12) - MONTH
# datetime.date(1961, 3, 13)
