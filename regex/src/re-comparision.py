import re


PATTERN = r'#[0-9]+'
TEXT = "Refs #23919, #31337 Removed obsolete comments"


re.findall(PATTERN, TEXT)
# ['#23919', '#31337']

re.search(PATTERN, TEXT).group()
# '#23919'

re.match(PATTERN, TEXT)
# None
