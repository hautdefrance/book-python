************
SSH Protocol
************


``paramiko``
============
.. code-block:: python

    import paramiko

    client = paramiko.SSHClient()

    client.connect('example.com', username='tester')
    # Traceback (most recent call last):
    #   ...
    # paramiko.ssh_exception.SSHException: Server 'example.com' not found in known_hosts

.. code-block:: python

    import paramiko

    client = paramiko.SSHClient()

    client.load_system_host_keys()
    client.load_host_keys('/home/brandon/.ssh/known_hosts')
    client.connect('example.com', username='test')

Password Auth
-------------
.. code-block:: python

    client.connect('example.com', username='brandon', password=mypass)
    client.connect('my.example.com')

Public/Private Key Auth
-----------------------
.. code-block:: python

    client.connect('my.example.com', key_filename='/home/brandon/.ssh/id_sysadmin')

Running commands
----------------
.. code-block:: python

    import paramiko, sys, getpass

    hostname = sys.argv[1]
    username = sys.argv[2]
    password = getpass.getpass()


    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname, username=username, password=password)
        for command in 'echo "Hello, world!"', 'uname', 'uptime':
            stdin, stdout, stderr = client.exec_command(command)
            stdin.close()
            print(repr(stdout.read()))
            stdout.close()
            stderr.close()
    client.close


``fabric``
==========
* http://www.fabfile.org/
* https://pypi.python.org/pypi/Fabric3

Local
-----
.. code-block:: python

    from fabric.api import local

    def prepare_deploy():
        local("./manage.py test my_app")
        local("git add -p && git commit")
        local("git push")

.. code-block:: console

    $ fab prepare_deploy
    [localhost] run: ./manage.py test my_app
    Creating test database...
    Creating tables
    Creating indexes
    ..........................................
    ----------------------------------------------------------------------
    Ran 42 tests in 9.138s

    OK
    Destroying test database...

    [localhost] run: git add -p && git commit

    <interactive Git add / git commit edit message session>

    [localhost] run: git push

    <git push session, possibly merging conflicts interactively>

    Done.

Organization
------------
.. code-block:: python

    from fabric.api import local

    def test():
        local("./manage.py test my_app")

    def commit():
        local("git add -p && git commit")

    def push():
        local("git push")

    def prepare_deploy():
        test()
        commit()
        push()

Failure handling
----------------
.. code-block:: python

    from fabric.api import local, settings, abort
    from fabric.contrib.console import confirm

    def test():
        with settings(warn_only=True):
            result = local('./manage.py test my_app', capture=True)

        if result.failed and not confirm("Tests failed. Continue anyway?"):
            abort("Aborting at user request.")

Executing on remote host
------------------------
.. code-block:: python

    from fabric.api import *
    from fabric.contrib.console import confirm

    env.hosts = ['my_server']

    def test():
        with settings(warn_only=True):
            result = local('./manage.py test my_app', capture=True)

        if result.failed and not confirm("Tests failed. Continue anyway?"):
            abort("Aborting at user request.")

    def commit():
        local("git add -p && git commit")

    def push():
        local("git push")

    def prepare_deploy():
        test()
        commit()
        push()

    def deploy():
        code_dir = '/srv/django/myproject'

        with settings(warn_only=True):
            if run("test -d %s" % code_dir).failed:
                run("git clone user@vcshost:/path/to/repo/.git %s" % code_dir)

        with cd(code_dir):
            run("git pull")
            run("touch app.wsgi")

.. code-block:: python

    from fabric.api import *

    def deploy():
        sudo("~/install_script.py")
        sudo("mkdir /var/www/new_docroot", user="www-data")
        sudo("ls /home/jdoe", user=1001)
        result = sudo("ls /tmp/")

        with settings(sudo_user='mysql'):
            sudo("whoami")
            # 'mysql'

Host
----
.. code-block:: python

    from fabric.api import hosts

    @hosts(['127.0.0.1', 'localhost'])
    def whoami():
        sudo('whoami')


``pssh``
========
* Running commands in parallel across many hosts
* https://linux.die.net/man/1/pssh

.. figure:: img/ssh-pssh-1.jpg
    :align: center
    :scale: 75%

.. figure:: img/ssh-pssh-2.jpg
    :align: center
    :scale: 50%

.. figure:: img/ssh-pssh-3.png
    :align: center
    :scale: 75%
