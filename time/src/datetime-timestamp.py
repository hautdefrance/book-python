from datetime import datetime

now = datetime.now()
now.timestamp()




# JavaScript has timestamp in miliseconds you have to divide by 1e3 = 1000
timestamp = 1331856000000
MILISECODS = 1e3

datetime.fromtimestamp(timestamp / MILISECODS)
# datetime.datetime(1978, 6, 27, 17, 27)


timestamp = 1331856000000
datetime.fromtimestamp(timestamp)

