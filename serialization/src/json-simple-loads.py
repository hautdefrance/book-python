import json


DATA = '{"first_name": "Jan", "last_name": "Twardowski"}'

output = json.loads(DATA)
print(output)
# {
#     'first_name': 'Jan',
#     'last_name': 'Twardowski'
# }
