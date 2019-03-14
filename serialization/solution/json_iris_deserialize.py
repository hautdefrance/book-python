import json
from pprint import pprint

FILE = r'../tmp/iris.json'
out = list()


with open(FILE) as file:
    DATA = json.load(file)


header = DATA[0].keys()
out.append(tuple(header))

for row in DATA:
    measurements = row.values()
    out.append(tuple(measurements))

pprint(out)
