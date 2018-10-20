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


def clean(text):
    text = text.lower()
    text = text.replace('\n', '')
    text = text.replace('\t', '')
    text = text.replace('ulica', '')
    text = text.replace('.', '')
    text = text.replace('ul', '')
    text = text.replace('trzeciego', 'III')
    text = text.replace('1/2', '')
    text = text.replace('1 /2', '')
    text = text.replace('1 m 2', '')
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
g = f'Jana {clean(g)}'
h = clean(h)
i = clean(i).replace('Sobi', 'Sobieskiego')
j = clean(j)
k = clean(k)

from pprint import pprint
pprint(locals())
