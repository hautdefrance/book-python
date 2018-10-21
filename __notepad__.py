SEPARATOR_ZDAN = '.'
SEPARATOR_SLOW = ' '

TEXT = 'We choose to go to the Moon. We choose to go to the Moon in this decade and do the other things. Not because they are easy, but because they are hard. Because that goal will serve to organize and measure the best of our energies and skills. Because that challenge is one that we are willing to accept. One we are unwilling to postpone. And one we intend to win'


podsumowanie_zdan = dict()
ile_zdan = 0
ile_slow = 0
ile_znakow = 0


for zdanie in TEXT.split(SEPARATOR_ZDAN):
    zdanie = zdanie.strip()
    slowa = zdanie.split(SEPARATOR_SLOW)
    ile_slow_w_zdaniu = len(slowa)

    podsumowanie_zdan[zdanie] = ile_slow_w_zdaniu
    ile_zdan += 1
    ile_slow += ile_slow_w_zdaniu
    ile_znakow += len(zdanie)


print(f'Ile zdań: {ile_zdan}')
print(f'Ile słów: {ile_slow}')
print(f'Ile znaków: {ile_znakow}')
