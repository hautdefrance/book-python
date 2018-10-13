import json
import base64
import http.client

client = http.client.HTTPSConnection('api.github.com')

auth = b'username:token'
hash = base64.b64encode(auth).decode('ascii')

client.request('GET', '/repos/django/django/commits', headers={
    'Authorization': 'Basic {}'.format(hash),
    'User-Agent': 'Python HTTP',
})

res = client.getresponse()
body = res.read().decode()
data = json.loads(body)

print(data)
