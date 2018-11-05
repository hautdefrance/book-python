import os
import logging


def if_file_exists(function):

    def check(filename):
        if os.path.exists(filename):
            function(filename)
        else:
            logging.error('File "%(filename)s" does not exists, will not execute!', locals())

    return check


@if_file_exists
def print_file(filename):
    with open(filename) as file:
        content = file.read()
        print(content)


if __name__ == '__main__':
    print_file('/etc/passwd')
    print_file('/tmp/passwd')
