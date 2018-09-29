a = 'UL. Jana III Sobieskiego 1/2'
b = 'ulica Jana III Sobieskiego 1/2'
c = 'os. Jana III Sobieskiego 1/2'
d = 'plac Jana III Sobieskiego 1/2'
e = 'aleja Jana III Sobieskiego 1/2'
f = 'alei Jana III Sobieskiego 1/2'
g = 'Jana III Sobieskiego 1 m. 2'
h = 'os. Jana III Sobieskiego 1 apt 2'

print(a[4:-4])
print(b[6:-4])
print(c[4:-4])
print(d[5:-4])
print(e[6:-4])
print(f[5:-4])
print(g[0:-7])
print(h[4:-8])

# alternatively
offset = len('Jana III Sobieskiego')
print(a[4:offset])
print(b[6:offset+6])
