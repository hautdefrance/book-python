import threading


def hello():
    print('Timer Thread')


t = threading.Timer(5.0, hello)
t.start()

print('Main Thread')
