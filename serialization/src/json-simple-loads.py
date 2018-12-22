import json


DATA = '{"first_name": "Pan", "last_name": "Twardowski"}'

output = json.loads(DATA)
print(output)
# {
#     'first_name': 'Pan',
#     'last_name': 'Twardowski'
# }
