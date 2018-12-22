from pprint import pprint
import requests


USERNAME = 'astromatt'
TOKEN = '9ee6df9bac964d7cad5b7d915e5f024748ddd720'
AUTH = (USERNAME, TOKEN)


url = 'https://api.github.com/orgs/django/repos'
r = requests.get(url, auth=AUTH)

pprint(r.json())
