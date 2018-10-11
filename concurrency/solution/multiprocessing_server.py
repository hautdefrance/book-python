#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from multiprocessing.connection import Listener
import logging

from __init__ import Prostokat
import pickle

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime).19s]  %(levelname)-9s %(name)10s: %(message)s',
    #filename='/_tmp/processes.log'
)

log = logging.getLogger('listener')

log.debug('Creating listener')
listener = Listener(
    address=('localhost', 1337),
    authkey=b'Welcome:)',
)


log.debug('Accept connections')
connection = listener.accept()


while True:
    data = connection.recv()

    if data == 'close':
        log.critical('Received "close"')
        connection.close()
        break

    else:
        log.info(data)
        if isinstance(data, Prostokat):
            obwod = data.obwod()
            log.info('Dosalem {} o obwodzie: {}'.format(data, obwod))
        elif isinstance(data, bytes):
            obj = pickle.loads(data, encoding='bytes')
            print(obj, 'o obwodzie', obj.obwod())
        else:
            print(type(data), data)


log.warning('Close listener')
listener.close()
