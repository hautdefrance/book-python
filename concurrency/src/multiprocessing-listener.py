from multiprocessing.connection import Listener
import logging
import pickle

address = ('localhost', 6000)  # family is deduced to be 'AF_INET'

logging.warning('Listening on %s:%s' % address)
listener = Listener(address, authkey=b'secret password')
conn = listener.accept()

logging.warning('connection accepted from %s %s' % listener.last_accepted)

while True:
    msg = conn.recv()
    logging.warning('Received: %s' % msg)

    if msg == 'close':
        conn.close()
        break
    else:
        # do something with msg
        prostokat = pickle.loads(msg[0])
        logging.warning('Prostokat %s' % prostokat)
        print('Pole: %s' % prostokat.pole())

listener.close()
