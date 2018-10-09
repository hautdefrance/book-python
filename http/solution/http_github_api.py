#!/usr/bin/env python3

import json
import base64
import re
import http.client


client = http.client.HTTPSConnection('api.github.com')

auth = b'username:token'
hash = base64.b64encode(auth).decode('ascii')
headers={
        'Autorization': 'Basic {}'.format(hash),
        'User-Agent': 'Python http.client',
}

def GET(url):
    client.request('GET', url, headers=headers)
    resp = client.getresponse()
    body = resp.read().decode()
    return json.loads(body)

repositories = GET('/orgs/django/repos')

repo = [repo for repo in repositories if repo['full_name'] == 'django/django'][0]

url = repo['commits_url'].replace('{/sha}', '').replace('https://api.github.com', '')

commits = GET(url)

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

