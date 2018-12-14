import re


DATA = [
    'jose.jimenez@nasa.gov',
    'Jose.Jimenez@nasa.gov',
    '+jose.jimenez@nasa.gov',
    'jose.jimenez+@nasa.gov',
    'jose.jimenez+newsletter@nasa.gov',
    'jose.jimenez@.gov',
    '@nasa.gov',
    'jose.jimenez@nasa.g',
]

PATTERN = re.compile(r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$')


for email in DATA:
    PATTERN.match(email)

