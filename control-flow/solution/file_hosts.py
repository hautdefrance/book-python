FILE = r'../src/etc-hosts.txt'
hostnames = []


try:
    with open(FILE, encoding='utf-8') as file:
        content = file.readlines()

except FileNotFoundError:
    print('File does not exist')

except PermissionError:
    print('Permission denied')


for line in content:
    if line.startswith('#'):
        continue
    if line.isspace():
        continue

    ip, *hosts = line.strip().split()

    for record in hostnames:
        if record['ip'] == ip:
            record['hostnames'] += hosts
            break
    else:
        hostnames.append({
            'hostnames': set(hosts),
            'protocol': 'IPv4' if '.' in ip else 'IPv6',
            'ip': ip,
        })

print(hostnames)

"""
found = False

for x in hosts:
    if x['ip'] == ip:
        found = True
        x['hostnames'] += hostnames

if not found:
    hosts.append({
        'ip': ip,
        'hostnames': hostnames,
        'protocol': 'IPv4' if '.' in ip else 'IPv6'
    })
"""
