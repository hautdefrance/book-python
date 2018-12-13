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

    line = line.strip().split()
    ip = line[0]
    hosts = line[1:]

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
