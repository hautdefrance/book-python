FILE = r'hosts.txt'

hostnames = []

try:
    with open(FILE, encoding='utf-8') as file:
        content = file.readlines()

except FileNotFoundError:
    print('File does not exist')

except PermissionError:
    print('Permission denied')


for line in content:
    if line.startswith('#') or line.isspace():
        continue

    ip = line.split()[0]
    hosts = line.split()[1:]

    for record in hostnames:
        if record['ip'] == ip:
            record['hostnames'].update(hosts)
            break
    else:
        hostnames.append({
            'hostnames': set(hosts),
            'protocol': 'IPv4' if '.' in ip else 'IPv6',
            'ip': ip,
        })

print(hostnames)
