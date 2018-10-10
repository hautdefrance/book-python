import re

PATTERN = r'\s[a-z]{3}\s'
TEXT = 'Baked Beans And Spam'


re.split(PATTERN, TEXT, flags=re.IGNORECASE)
# ['Baked Beans', 'Spam']
