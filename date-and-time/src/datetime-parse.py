from datetime import datetime


sputnik = '4 October 1957 19:28:34 UTC'


out = datetime.strptime(sputnik, '%d %B %Y %H:%M:%S %Z')
# datetime.datetime(1957, 10, 4, 19, 28, 34)

print(out)
# 1957-10-04 19:28:34
