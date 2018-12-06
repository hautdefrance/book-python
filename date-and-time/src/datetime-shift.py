from datetime import datetime


gagarin = datetime(1961, 4, 12, 6, 7)
armstrong = datetime(1969, 7, 21, 14, 56, 15)


between_dates = armstrong - gagarin    # datetime.timedelta(3022, 31755)

between_dates                          # 3022 days, 8:49:15
between_dates.seconds                  # 31755
between_dates.days                     # 3022
between_dates.total_seconds()          # 261132555.0 (days * seconds per day + seconds)
