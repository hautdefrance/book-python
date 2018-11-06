from datetime import datetime

gagarin = datetime(1961, 4, 12, 6, 7)
armstrong = datetime(1969, 7, 21, 14, 56, 15)

duration = armstrong - gagarin            # datetime.timedelta(3022, 31755)

duration                                  # 3022 days, 8:49:15
duration.seconds                          # 31755
duration.days                             # 3022
duration.total_seconds()                  # 261132555.0 (days * seconds per day + seconds)
