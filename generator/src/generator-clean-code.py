DATA = {'username': 'Иван Иванович', 'agency': 'Roscosmos'}


def asd(x):
    return x.replace('Иван', 'Ivan')


out = {
    value: asd(value)
    for key, value in DATA.items()
    if key == 'username'
}

print(out)
# {'Иван Иванович': 'Ivan Ivanович'}


out = ['CCCP' if key == 'Roscosmos' else 'USA' for key, value in DATA.items() if key == 'agency']
print(out)
# ['USA']

