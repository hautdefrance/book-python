from ftplib import FTP


HOSTNAME = 'ftp.us.debian.org'
USERNAME = 'anonymous'
PASSWORD = ''


with FTP(host=HOSTNAME, user=USERNAME, passwd=PASSWORD, timeout=30) as ftp:
    ftp.cwd('debian')       # change into "debian" directory

    ftp.dir()   # list directory contents
    # drwxr-xr-x    9 ftp      ftp          4096 Nov 06 21:00 debian
    # drwxr-xr-x    9 ftp      ftp          4096 Nov 06 13:57 debian-archive
    # drwxr-sr-x    5 ftp      ftp          4096 Mar 13  2016 debian-backports
    # drwxr-xr-x    2 ftp      ftp          4096 Jun 22  2015 stats

    with open('README', mode='wb') as file:
        ftp.retrbinary('RETR README', file.write)
        # '226 Transfer complete.'

    ftp.quit()
