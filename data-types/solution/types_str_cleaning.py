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


a = a.replace(' 1 apt 2', '').strip()
b = b.replace('ul ', '').replace(' 1/2', '').title().replace('Iii', 'III')
c = c.replace('trzeciego', 'III').replace(' 1/2', '').replace('ul. ', '')
d = d.replace('ul.', '').replace(' 1/2', '')
e = e.replace('ulica', '').replace(' 1/2', '')


expected = 'Jana III Sobieskiego'
print(f'{a == expected}\t a: "{a}"')
print(f'{b == expected}\t b: "{b}"')
print(f'{c == expected}\t c: "{c}"')
print(f'{d == expected}\t d: "{d}"')
print(f'{e == expected}\t e: "{e}"')
print(f'{f == expected}\t f: "{f}"')
print(f'{g == expected}\t g: "{g}"')
print(f'{h == expected}\t h: "{h}"')
print(f'{i == expected}\t i: "{i}"')
print(f'{j == expected}\t j: "{j}"')
print(f'{k == expected}\t k: "{k}"')
