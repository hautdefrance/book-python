#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from multiprocessing.connection import Client
import logging
import pickle

from __init__ import Prostokat


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime).19s] %(levelname)-9s %(name)10s: %(message)s',
    #filename='/_tmp/processes.log'
)

log = logging.getLogger('client')


log.debug('Opening connection')
client = Client(
    address=('localhost', 1337),
    authkey=b'Welcome:)'
)


log.debug('Sending data')
prostokat = Prostokat(5, 10)

pickled = pickle.dumps(prostokat, protocol=pickle.HIGHEST_PROTOCOL)

data = ['ehlo', 10, 10.6, None, True, {'asd': 10}, [{1, 2, 3}], prostokat, pickled]

for element in data:
    client.send(element)


log.debug('Closing connection')
client.send('close')
client.close()



## TODO: Stworzenie Listenera
# stworzenie listenera
# akceptacja polaczen przychodzacych
# petla
#     przyjecie wiadomosci
#     if wiadomosc == close: zamkniecie polaczenia, wyjscie z petli
#     else: wyswietl tresc
# zamkiecie listenera
