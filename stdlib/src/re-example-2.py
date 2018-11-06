import re


TEXT = 'He was carefully disguised but captured quickly by police.'
ADVERBS = r'\w+ly'

re.findall(ADVERBS, TEXT)
# ['carefully', 'quickly']