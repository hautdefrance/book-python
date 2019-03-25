INPUT = {
    4: ['Masters', 'Doctorate', 'Prof-school'],
    6: ['HS-grad'],
    3: ['Bachelor']
}

wynik = {}

for key, value in INPUT.items():
    for education in value:
        wynik[education] = str(key)

## Alternatywnie:
#
# wynik = {education: str(key)
#     for key, value in EDUCATION_GROUPS.items()
#         for education in value
# }

print(wynik)

# OUTPUT = {
#     'Masters': '4',
#     'Doctorate': '4',
#     'Prof-school': '4',
#     'HS-grad': '6',
#     'Bachelor': '3',
# }
