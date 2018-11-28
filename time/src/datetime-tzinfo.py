from datetime import datetime, timezone

# timezone naive - nieświadome
datetime.now()
datetime.utcnow()
datetime(1957, 10, 4, 19, 28, 34)

# timezone aware - świadome
datetime.now(tz=timezone.utc)
datetime(1957, 10, 4, 19, 28, 34, tzinfo=timezone.utc)
