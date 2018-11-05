FILE = 'hosts.txt'


hosts = {}

with open(FILE, encoding='utf-8') as file:

    for line in file:

        if line.startswith('#'):
            continue

        if line.isspace():
            continue

        ip, *hostnames = line.split()

        if ip in hosts:
            hosts[ip] += hostnames
        else:
            hosts[ip] = hostnames

print(hosts)
