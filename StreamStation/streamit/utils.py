
import string
import random


def generate_key(plaintext, chars=(string.ascii_letters + string.digits) * 2):
    shuffled = sorted(chars, key=lambda k: random.random())[:len(string.printable)]
    trans = dict(zip(string.printable, shuffled))
    return ''.join(trans[l] for l in plaintext)

