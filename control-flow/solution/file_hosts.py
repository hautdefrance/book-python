from pprint import pprint


FILENAME = r'hosts.txt'
hosts = []


with open(FILENAME, encoding='utf-8') as file:
    for line in file:

        if line.startswith('#') or line.isspace():
            continue

        record = line.split()
        ip = record[0]
        hostnames = record[1:]
        protocol = 'ipv4' if '.' in ip else 'ipv6'

        hosts.append({
            'ip': ip,
            'hostnames': hostnames,
            'protocol': protocol,
        })


pprint(hosts)
