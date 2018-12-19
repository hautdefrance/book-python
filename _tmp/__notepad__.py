DATA = [
     {'last_name': 'Jiménez'},
     {'first_name': 'Mark', 'last_name': 'Watney'},
     {'first_name': 'Иван'},
     {'first_name': 'Pan', 'last_name': 'Twardowski', 'born': 1961},
     {'first_name': 'Melissa', 'last_name': 'Lewis', 'first_step': 1969},
 ]

def asd(value):
    pass

[
                asd(value)
            for d in DATA
        for key, value in d.items()
    if key == 'username'
]
