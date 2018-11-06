import re

# used for redmine and track issue id
PATTERN = r'#[0-9]+'
TEXT = "Refs #23919, #31337 Removed obsolete comments"


re.findall(PATTERN, TEXT)
# ['#23919', '#31337']
