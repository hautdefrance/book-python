import re

TEXT = '<strong>Ehlo World</strong>'

re.findall(r'<.*>', TEXT)
# ['<strong>Ehlo World</strong>']

re.findall(r'<.*?>', TEXT)
# ['<strong>', '</strong>']
