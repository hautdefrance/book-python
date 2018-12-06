from datetime import datetime


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
MONTH = 30.436875 * DAY    # Average days a month in solar calendar
YEAR = 365.2425 * DAY      # Solar calendar


gagarin = datetime(1961, 4, 12, 6, 7)
armstrong = datetime(1969, 7, 21, 14, 56, 15)

duration = armstrong - gagarin
# datetime.timedelta(3022, 31755)

years, seconds = divmod(duration.total_seconds(), YEAR)
months, seconds = divmod(seconds, MONTH)
days, seconds = divmod(seconds, DAY)
hours, seconds = divmod(duration.seconds, HOUR)
minutes, seconds = divmod(seconds, MINUTE)

difference = {
    'years': int(years),
    'months': int(months),
    'days': int(days),
    'hours': int(hours),
    'minutes': int(minutes),
    'seconds': int(seconds),
}

print(difference)
# {'years': 8, 'months': 3, 'days': 9, 'hours': 8, 'minutes': 49, 'seconds': 15}
