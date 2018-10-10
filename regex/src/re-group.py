import re

PATTERN = r'(?P<first_name>\w+) (?P<last_name>\w+)'
TEXT = 'José Jiménez'

matches = re.match(PATTERN, TEXT)


matches.group('first_name')
# 'José'

matches.group('last_name')
# 'Jiménez'

matches.group(1)
# 'José'

matches.group(2)
# 'Jiménez'

matches.groups()
# ('José', 'Jiménez')

matches.groupdict()
# {'first_name': 'José', 'last_name': 'Jiménez'}
