from datetime import datetime


armstrong = datetime(1969, 7, 21, 14, 56, 15)

armstrong.date()        # datetime.date(1969, 7, 21)
armstrong.time()        # datetime.time(14, 56, 15)
armstrong.weekday()     # 0  # in US week starts with Sunday
