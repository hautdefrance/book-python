expected = 'Jana III Sobieskiego'

a = '  Jana III Sobieskiego 1 apt 2'
b = 'ul Jana III SobIESkiego 1/2'
c = '\tul. Jana trzeciego Sobieskiego 1/2'
d = 'ul.Jana III Sob\n\nieskiego 1/2'
e = 'ulicaJana III Sobieskiego 1/2'
f = 'UL. JA\tNA 3 SOBIES\tKIEGO 1/2'
g = 'UL. III SOBiesKIEGO 1/2'
h = 'ULICA JANA III SOBIESKIEGO 1 /2  '
i = 'ULICA. JANA III SOBI'
j = ' Jana 3 Sobieskiego 1/2 '
k = 'Jana III Sobieskiego 1 m. 2'



print(f'a: {a == expected}')
print(f'b: {b == expected}')
print(f'c: {c == expected}')
print(f'd: {d == expected}')
print(f'e: {e == expected}')
print(f'f: {f == expected}')
print(f'g: {g == expected}')
print(f'h: {h == expected}')
print(f'i: {i == expected}')
print(f'j: {j == expected}')
print(f'k: {k == expected}')
