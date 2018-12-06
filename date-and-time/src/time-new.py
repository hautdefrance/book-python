from datetime import time


midnight = time()
# datetime.time(0, 0)


now = time(12, 33, 44)
# datetime.time(12, 33, 44)


now.hour            # 12
now.minute          # 33
now.second          # 44
now.microsecond     # 0
