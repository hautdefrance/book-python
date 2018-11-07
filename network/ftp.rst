***
FTP
***

Connect to FTP
==============
.. code-block:: python

    from ftplib import FTP


    HOSTNAME = 'ftp.pureftpd.org'
    USERNAME = 'anonymous'
    PASSWORD = ''


    with FTP(host=HOSTNAME, user=USERNAME, passwd=PASSWORD, timeout=30) as ftp:
        ftp.dir()

    # drwxr-xr-x   18 1000       1008             1024 Jul 21  2016 .
    # drwxr-xr-x   18 1000       1008             1024 Jul 21  2016 ..
    # lrwxr-xr-x    1 1000       20                 20 Jun 20  2011 6jack -> pure-ftpd/misc/6jack
    # lrwxr-xr-x    1 1000       1008               12 Jan 24  2012 OpenBSD -> misc/OpenBSD
    # drwxr-xr-x    2 1000       1008              512 Feb 10  2015 antilink
    # lrwxr-xr-x    1 0          1008               24 Feb  1  2006 blogbench -> pure-ftpd/misc/blogbench
    # lrwxr-xr-x    1 0          1008               21 Feb  1  2006 bsdcam -> pure-ftpd/misc/bsdcam
    # ...

Connect to FTPS
===============
.. code-block:: python

    from ftplib import FTP_TLS

    HOSTNAME = 'ftp.pureftpd.org'
    USERNAME = 'anonymous'
    PASSWORD = ''


    with FTP_TLS(host=HOSTNAME, user=USERNAME, passwd=PASSWORD, timeout=30) as ftps:
        ftps.dir()

    # drwxr-xr-x   18 1000       1008             1024 Jul 21  2016 .
    # drwxr-xr-x   18 1000       1008             1024 Jul 21  2016 ..
    # lrwxr-xr-x    1 1000       20                 20 Jun 20  2011 6jack -> pure-ftpd/misc/6jack
    # lrwxr-xr-x    1 1000       1008               12 Jan 24  2012 OpenBSD -> misc/OpenBSD
    # drwxr-xr-x    2 1000       1008              512 Feb 10  2015 antilink
    # lrwxr-xr-x    1 0          1008               24 Feb  1  2006 blogbench -> pure-ftpd/misc/blogbench
    # lrwxr-xr-x    1 0          1008               21 Feb  1  2006 bsdcam -> pure-ftpd/misc/bsdcam
    # ...

Download file
=============
.. code-block:: python

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


Methods
=======
.. csv-table:: FTP Methods
    :header-rows: 1
    :widths: 10, 10, 80

    "Method", "Arguments", "Description"
    "``FTP.connect()``", "``host=''``, ``port=0``, ``timeout=None``, ``source_address=None``", "Connect to the given host and port. The default port number is 21, as specified by the FTP protocol specification"
    "``FTP.login()``", "``user='anonymous'``, ``passwd=''``, ``acct=''``", "Log in as the given user"
    "``FTP.abort()``", "", "Abort a file transfer that is in progress"
    "``FTP.sendcmd()``", "``cmd``", "Send a simple command string to the server and return the response string"
    "``FTP.retrbinary()``", "``cmd``, ``callback``, ``blocksize=8192``, ``rest=None``", "Retrieve a file in binary transfer mode"
    "``FTP.retrlines()``", "``cmd``, ``callback=None``", "Retrieve a file or directory listing in ASCII transfer mode"
    "``FTP.set_pasv()``", "``val``", "Enable 'passive' mode if val is true, otherwise disable passive mode"
    "``FTP.storbinary()``", "``cmd``, ``fp``, ``blocksize=8192``, ``callback=None``, ``rest=None``", "Store a file in binary transfer mode"
    "``FTP.storlines()``", "``cmd``, ``fp``, ``callback=None``", "Store a file in ASCII transfer mode"
    "``FTP.dir()``", "``argument[, ...]``", "Produce a directory listing as returned by the LIST command, printing it to standard output"
    "``FTP.rename()``", "``old_name``, ``new_name``", "Rename file"
    "``FTP.delete()``", "``filename``", "Remove the file"
    "``FTP.cwd()``", "``pathname``", "Set the current directory on the server"
    "``FTP.mkd()``", "``pathname``", "Create a new directory on the server"
    "``FTP.pwd()``", "", "Return the pathname of the current directory on the server"
    "``FTP.rmd()``", "``dirname``", "Remove the directory named dirname on the server"
    "``FTP.size()``", "``filename``", "Request the size of the file named filename on the server"
