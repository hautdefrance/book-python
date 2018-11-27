SKALA_OCEN = (2, 3, 3.5, 4, 4.5, 5)
DOPUSZCZALNE_OCENY = [float(x) for x in SKALA_OCEN]

dzienniczek_ucznia = []


while True:
    wprowadzona_ocena = input('Wprowadz ocenę: ')

    if not wprowadzona_ocena:
        break

    wprowadzona_ocena = float(wprowadzona_ocena)

    if wprowadzona_ocena in DOPUSZCZALNE_OCENY:
        dzienniczek_ucznia.append(wprowadzona_ocena)
    else:
        print('Grade is not allowed')


srednia = sum(dzienniczek_ucznia) / len(dzienniczek_ucznia)
srednia = round(srednia, 2)

print(srednia)
