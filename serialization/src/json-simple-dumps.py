import json


DATA = {
    'first_name': 'Pan',
    'last_name': 'Twardowski'
}

output = json.dumps(DATA)
print(output)
# '{"first_name": "Pan", "last_name": "Twardowski"}'
