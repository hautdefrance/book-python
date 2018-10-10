import re


PATTERN = r'^#[0-9]+'

TEXT = """
#27533 Fixed inspectdb crash;
#31337 Remove commented out code
"""


re.findall(PATTERN, TEXT)
# []

re.findall(PATTERN, TEXT, flags=re.MULTILINE)
# ['#27533', '#31337']
