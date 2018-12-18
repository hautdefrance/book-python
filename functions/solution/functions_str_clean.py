expected = 'Jana III Sobieskiego'

a = '  Jana III Sobieskiego '
b = 'ul Jana III SobIESkiego'
c = '\tul. Jana trzeciego Sobieskiego'
d = 'ulicaJana III Sobieskiego'
e = 'UL. JA\tNA 3 SOBIES\tKIEGO'
f = 'UL. jana III SOBiesKIEGO'
g = 'ULICA JANA III SOBIESKIEGO  '
h = 'ULICA. JANA III SOBIeskieGO'
i = ' Jana 3 Sobieskiego  '
j = 'Jana III\tSobieskiego '
k = 'ul.Jana III Sob\n\nieskiego\n'


def clean(text):
    text = text.upper()
    text = text.replace('\n', '')
    text = text.replace('\t', '')
    text = text.replace('ULICA', '')
    text = text.replace('.', '')
    text = text.replace('UL', '')
    text = text.replace('TRZECIEGO', 'III')
    text = text.replace('3', 'III')
    text = text.strip()
    text = text.title().replace('Iii', 'III')
    return text


a = clean(a)
b = clean(b)
c = clean(c)
d = clean(d)
e = clean(e)
f = clean(f)
g = clean(g)
h = clean(h)
i = clean(i)
j = clean(j).replace('IIIs', 'III S')
k = clean(k)

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
