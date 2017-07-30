import os
import time
import random
from pykeyboard import PyKeyboard


k = PyKeyboard()
front_cmd = """osascript -e 'tell application "System Events"' -e 'tell process "mame64"' -e 'set frontmost to true' -e 'end tell' -e 'end tell'"""


def press_key(key):
    k.press_key(key)
    time.sleep(0.2)
    k.release_key(key)
    if key == 'c' or 'k':
        time.sleep(0.5)
    else:
        time.sleep(0.1)


def press_keys(key1, key2):
    k.press_key(key1)
    k.press_key(key2)
    time.sleep(0.2)
    k.release_key(key1)
    k.release_key(key2)
    if key1 == 'k' or key2 == 'c':
        time.sleep(0.5)
    elif key1 == 'h' or key2 == 'z':
        k.press_key(key1)
        k.press_key(key2)
        time.sleep(0.2)
        k.release_key(key1)
        k.release_key(key2)
        time.sleep(0.1)
    else:
        time.sleep(0.1)


if __name__ == '__main__':

    os.system(front_cmd)

    p1_keys = ['y', 'u', 'i', 'o', 'h', 'j', 'k', 'l']
    p2_keys = ['q', 'w', 'e', 'r', 'z', 'x', 'c', 'v']

    press_key('p')
    time.sleep(0.5)

    # random keys for demo
    for _ in range(200):
        for k1, k2 in zip(random.sample(p1_keys, 8), random.sample(p2_keys, 8)):
            press_keys(k1, k2)
