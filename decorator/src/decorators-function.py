import signal
from time import sleep


def timeout(function, seconds=2, error_message='Timeout'):

    def wrapper(*args, **kwargs):

        def handler(signum, frame):
            raise TimeoutError

        signal.signal(signal.SIGALRM, handler)
        signal.alarm(seconds)

        try:
            function(*args, **kwargs)
        except TimeoutError:
            print(error_message)
        finally:
            signal.alarm(0)

    return wrapper


@timeout
def connect(username, password, host='127.0.0.1', port='80'):
    print('Connecting...')
    sleep(5)
    print('Connected')


connect('admin', 'admin')
