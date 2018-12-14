DATA = [
    {'last_name': 'Jiménez'},
    {'first_name': 'Matt', 'last_name': 'Kowalski'},
    {'first_name': 'Иван', 'age': 42},
    {'first_name': 'Melissa', 'last_name': 'Lewis', 'first_step': 1969},
    {'first_name': 'José', 'first_flight': 1961, 'agency': 'NASA'},
]

unique_keys = set()

for row in DATA:
    unique_keys.update(row.keys())



unique_keys = set()

for row in DATA:
    for key in row.keys():
        unique_keys.add(key)



all_keys = list()

for row in DATA:
    for key in row.keys():
        all_keys.append(key)

unique_keys = set(all_keys)



unique_keys = list()

for row in DATA:
    for key in row.keys():
        if key not in unique_keys:
            unique_keys.append(key)

