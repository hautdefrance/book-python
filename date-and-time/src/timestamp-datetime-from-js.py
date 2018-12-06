from datetime import datetime


# JavaScript has timestamp in miliseconds you have to divide by 1e3 = 1000
timestamp = 267809220000
MILISECONDS = 1e3

datetime.fromtimestamp(timestamp / MILISECONDS)
# datetime.datetime(1978, 6, 27, 17, 27)


