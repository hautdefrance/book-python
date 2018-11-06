#!/usr/bin/env python3

import re
import http.client
import json
from http import HTTPStatus
from base64 import b64encode
from datetime import datetime
import logging


USERNAME = 'my_username'
TOKEN = 'my_token'


auth = bytes(f'{USERNAME}:{TOKEN}', 'utf-8')
auth = b64encode(auth).decode('ascii')

headers = {
    'Authorization': f'Basic {auth}',
    'User-Agent': 'Python http.client',
    'Accept': 'application/json'
}

conn = http.client.HTTPSConnection(host="api.github.com", port=443)


def GET(url):
    logging.warning(f'URL: {url}')
    conn.request('GET', url, headers=headers)
    response = conn.getresponse()

    if response.status == HTTPStatus.OK:
        body = response.read().decode()
        return json.loads(body)
    else:
        raise ConnectionError(response.reason)


repo = [repo for repo in GET('/orgs/django/repos') if repo['full_name'] == 'django/django'][0]
url = repo['commits_url'].replace('{/sha}', '').replace('https://api.github.com', '')

commits = GET(url)
date = commits[0]['commit']['author']['date']
name = commits[0]['commit']['author']['name']
date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z')
print(f'Ostatni commit: {date} by {name}')

messages = [commit['commit']['message'] for commit in commits]

issues = set()

for msg in messages:
    tickets = re.findall(r'#([0-9]+)', msg, flags=re.MULTILINE)
    issues.update(tickets)

print(issues)

conn.close()
