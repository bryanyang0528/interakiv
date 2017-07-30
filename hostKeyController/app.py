from socketIO_client import SocketIO, LoggingNamespace
from pykeyboard import PyKeyboard
from time import time
k = PyKeyboard()

ONE_FRAME_IN_MS = 16.67

def on_print_response(*args):
    print('response', args)


def on_press_key(*args):
    print('press_key', args)
    streetFighter(args['message'])


def streetFighter(key):
    if key == 'Q':
        tap_key('down')
        time.sleep(ONE_FRAME_IN_MS)
        tap_key('right')
        time.sleep(ONE_FRAME_IN_MS)
	tap_key('Q')

socketIO = SocketIO('localhost', 3000, LoggingNamespace)
socketIO.emit('add user', 'testfrompython')
socketIO.emit('new message', 'test')
socketIO.on("new message", on_print_response)
    #socketIO.wait(seconds=10) 
socketIO.on("press key", on_press_key)


socketIO.wait()
