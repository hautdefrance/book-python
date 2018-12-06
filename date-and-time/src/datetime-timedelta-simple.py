from datetime import datetime, timedelta, date


sputnik = date(1957, 10, 4)
gagarin = datetime(1961, 4, 12)
armstrong = datetime(1969, 7, 21, 14, 56, 15)


gagarin - timedelta(minutes=15)
gagarin + timedelta(minutes=10)

armstrong - timedelta(hours=21)
armstrong + timedelta(hours=5)

sputnik + timedelta(days=5)
sputnik - timedelta(days=3)

gagarin + timedelta(weeks=2)
gagarin - timedelta(weeks=3)

armstrong - timedelta(days=2, hours=21)
