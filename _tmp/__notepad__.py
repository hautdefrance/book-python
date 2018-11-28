i = 'ULICA. JANA III SOBI'


def clean(text: str) -> str:
    return text.replace('ULICA. ', '').title().replace('Iii', 'III')


a = '  Jana III Sobieskiego 1 apt 2'
a = clean(a)
print(a)

b = 'ul Jana III SobIESkiego 1/2'
b = clean(b)
print(b)

c = '\tul. Jana trzeciego Sobieskiego 1/2'
c = clean(c)
print(c)

d = 'ul.Jana III Sob\n\nieskiego 1/2'
d = clean(d)
print(d)

e = 'ulicaJana III Sobieskiego 1/2'
e = clean(e)
print(e)

f = 'UL. JA\tNA 3 SOBIES\tKIEGO 1/2'
f = clean(f)
print(f)

g = 'UL. III SOBiesKIEGO 1/2'
g = clean(g)
print(g)

h = 'ULICA JANA III SOBIESKIEGO 1 /2  '
h = clean(h)
print(h)

i = 'ULICA. JANA III SOBI'
i = clean(i)
print(i)

j = ' Jana 3 Sobieskiego 1/2 '
j = clean(j)
print(j)

k = 'Jana III Sobieskiego 1 m. 2'
k = clean(k)
print(k)
