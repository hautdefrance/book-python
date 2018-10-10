import re


PATTERN = r'#[0-9]+'  # used for redmine and track issue id
TEXT = "Refs #23919, #31337 -- Removed obsolete comments about u'' prefixes."


re.search(PATTERN, TEXT).group()
# '#23919'
