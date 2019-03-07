import json


DATA = {
    'first_name': 'Jan',
    'last_name': 'Twardowski'
}

output = json.dumps(DATA)
print(output)
# '{"first_name": "Jan", "last_name": "Twardowski"}'
