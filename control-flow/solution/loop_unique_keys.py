DATABASE = [
    {'last_name': 'Jiménez'},
    {'first_name': 'Matt', 'last_name': 'Kowalski'},
    {'first_name': 'Иван', 'age': 42},
    {'first_name': 'Melissa', 'last_name': 'Lewis', 'first_step': 1969},
    {'first_name': 'José', 'first_flight': 1961, 'agency': 'NASA'},
]

unique_keys = set()

for row in DATABASE:
    unique_keys.update(row.keys())

print(unique_keys)
