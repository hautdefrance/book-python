from datetime import datetime


czas = '1969-07-21T14:56:15.123Z'
out = datetime.strptime(czas, '%Y-%m-%dT%H:%M:%S.%fZ')

print(out)
