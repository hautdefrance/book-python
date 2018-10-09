from datetime import datetime, timedelta, timezone


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
MONTH = 30.436875               # Average days a month in solar calendar
YEAR = 365.2425                 # Solar calendar


input1 = 'April 12, 1961 2:07 local time'  # ALMT Timezone
input2 = '"07/21/69 2:56:15 AM UTC"'


gagarin = datetime.strptime(input1, '%B %d, %Y %H:%M local time')
# datetime.datetime(1961, 4, 12, 2, 7)

armstrong = datetime.strptime(input2, '"%x %X %p %Z"')
# datetime.datetime(1969, 7, 21, 2, 56, 15)

armstrong = datetime.strptime(input2, '"%m/%d/%y %I:%M:%S %p %Z"')
# datetime.datetime(1969, 7, 21, 2, 56, 15)

diff = armstrong - gagarin
# datetime.timedelta(days=3022, seconds=2955)


years, days = divmod(diff.days, YEAR)
months, days = divmod(days, MONTH)
hours, minutes = divmod(diff.seconds, HOUR)
minutes, seconds = divmod(minutes, MINUTE)

difference = {
    'years': int(years),
    'months': int(months),
    'days': int(days),
    'hours': int(hours),
    'minutes': int(minutes),
    'seconds': int(seconds),
}
# {'years': 8, 'months': 3, 'days': 8, 'hours': 0, 'minutes': 49, 'seconds': 15}

delta = timedelta(seconds=diff.total_seconds())
# datetime.timedelta(days=3022, seconds=2955)

now = datetime.now(tz=timezone.utc)

past = now - delta
# 2010-05-20

birthday = datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
my_age = past - birthday
# datetime.timedelta(days=14749, seconds=42059, microseconds=810113)


years, days = divmod(my_age.days, YEAR)
months, days = divmod(days, MONTH)
hours, minutes = divmod(my_age.seconds, HOUR)
minutes, seconds = divmod(minutes, MINUTE)

difference = {
    'years': int(years),
    'months': int(months),
    'days': int(days),
    'hours': int(hours),
    'minutes': int(minutes),
    'seconds': int(seconds),
}

print(difference)
# {'years': 40, 'months': 4, 'days': 17, 'hours': 11, 'minutes': 40, 'seconds': 59}
