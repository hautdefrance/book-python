from datetime import datetime


timestamp = 267809220000
# JavaScript has timestamp in miliseconds

MILISECONDS = 1e3
# To convert from miliseconds we have to divide by 1e3 = 1000

datetime.fromtimestamp(timestamp / MILISECONDS)
# datetime.datetime(1978, 6, 27, 17, 27)
