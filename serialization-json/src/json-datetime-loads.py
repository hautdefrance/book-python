import json


DATA = """
{
    "email": "jose.jimenez@nasa.gov",
    "date": "1961-04-12",
    "datetime": "1969-07-21T14:56:15.000Z"
}
"""

output = json.loads(DATA)

print(output)
# {
#     'email': 'jose.jimenez@nasa.gov',
#     'date': '1961-04-12',
#     'datetime': '1969-07-21T14:56:15.000Z',
# }
