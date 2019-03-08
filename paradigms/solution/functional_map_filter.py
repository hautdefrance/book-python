
zakres = range(1, 34)

podzielne_przez_3 = [x for x in zakres if x % 3 == 0]

podzielne_przez_3_i_nieparzyste = filter(lambda x: not x % 2 == 0, podzielne_przez_3)

podzielne_przez_3_i_nieparzyste_do_szescianu = map(lambda x: pow(x, 3), podzielne_przez_3_i_nieparzyste)

liczby = list(podzielne_przez_3_i_nieparzyste_do_szescianu)

srednia = sum(liczby) / len(liczby)

print(srednia)