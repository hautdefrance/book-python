from datetime import datetime


armstrong = '"April 12, 1961 06:07:00 AM local time"'
armstrong = datetime.strptime(armstrong, '"%B %d, %Y %I:%M:%S %p local time"')

# 04/12/61 06:07 AM
print(armstrong.strftime('%m/%d/%y %I:%M %p'))
