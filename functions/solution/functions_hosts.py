FILENAME = r'../assignment/etc-hosts.txt'
hosts = dict()


with open(FILENAME, encoding='utf-8') as file:
    for line in file:
        if line.isspace() or line.startswith('#'):
            continue

        ip, *hostnames = line.split()

        if hosts.get(ip) in hosts:
            hosts[ip].extend(hostnames)
        else:
            hosts[ip] = hostnames


print(hosts)
