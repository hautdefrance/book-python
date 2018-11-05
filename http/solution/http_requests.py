#!/usr/bin/env python3

import re
import requests

auth = ('username', 'token')

resp = requests.get('https://api.github.com/orgs/django/repos', auth=auth)
repositories = resp.json()

repo = [repo for repo in repositories if repo['full_name'] == 'django/django'][0]
url = repo['commits_url'].replace('{/sha}', '')

resp = requests.get(url, auth=auth)
commits = resp.json()

data = commits[0]['commit']['author']['date']
name = commits[0]['commit']['author']['name']

print('Ostatni commit:', data, name)

messages = [commit['commit']['message'] for commit in commits]

issues = []

for msg in messages:
    issue = re.findall(r'#([0-9]+)', msg, flags=re.MULTILINE)

    if issue:
        issues.extend(issue)

unique = set(issues)

print(unique)

