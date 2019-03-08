def liczby_parzyste(x):
    return x % 2 == 0


zbior_liczb = [1, 2, 3, 4]
parzyste = filter(liczby_parzyste, zbior_liczb)


parzyste = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])


print(list(parzyste))