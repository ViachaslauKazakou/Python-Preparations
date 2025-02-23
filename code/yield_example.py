DICTIONARY = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cat',
    'd': 'dog',
    'e': 'elephant',
    'f': 'fox',
    'g': 'gorilla',
    'h': 'hippo',
    'i': 'iguana',
    'j': 'jaguar',
    'k': 'koala',
    'l': 'llama',
    'm': 'monkey',
    'n': 'newt',
    'o': 'octopus',
    'p': 'parrot',
    'q': 'quail',
    'r': 'rabbit',
    's': 'squirrel',
    't': 'tiger',
    'u': 'unicorn',
    'v': 'viper',
    'w': 'walrus',
    'x': 'xenomorph',
    'y': 'yak',
    'z': 'zebra'
}


def alphabet():
    a = yield
    while True:
        try:
            a = yield DICTIONARY[a]
        except KeyError:
            a = yield 'default'

def alphabet1():
    a = yield
    while True:
        a = yield DICTIONARY.get(a, 'default')

def alphabet2():
    a = yield
    while True:
        try:
            a = yield DICTIONARY.get(a, 'default')
        except KeyError:
            a = yield 'default'
            

if __name__ == '__main__':

    coro = alphabet()
    next(coro)
    print(coro.send('a'))
    print(coro.send('b'))
    print(coro.throw(KeyError))
    print(coro.send('c'))
    