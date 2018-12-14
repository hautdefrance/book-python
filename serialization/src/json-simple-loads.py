import json


DATA = '{"first_name": "José", "last_name": "Jiménez"}'

output = json.loads(DATA)
print(output)
# {
#     'first_name': 'Jos\u00e9',
#     'last_name': 'Jim\u00e9nez'
# }
