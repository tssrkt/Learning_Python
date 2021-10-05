from pprint import pprint as pp
daily = [[1,2,3], [4,5,6], [7,8,9]]
pp(daily)
transposed = list(zip(*daily))
pp(transposed)

print(callable(transposed))

# closure
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

square = raise_to(2)
pp(square.__closure__)
print('raise 5 to 2:', square(5))
a = raise_to(3)
print('raise 5 to 3:', a(5))

##########################

msg = 'global'

def enclosing():
    msg = 'enclosing'

    def local2():
        nonlocal msg
        msg = 'local 2 (enclosing)'

    def local():
        global msg
        msg = 'local'

    print('enclosing msg:', msg)
    local()
    print('enclosing msg:', msg)
    local2()
    print('enclosing msg:', msg)

print('global msg:', msg)
enclosing()
print('global msg:', msg)

###################################

import time
def make_timer():
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result
    return elapsed

print()
print('*'*50)
print('DECORATORS')

def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

@escape_unicode
def northern_city():
    return 'Tromso'

print(northern_city())

class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)

@CallCount
def hello(name):
    print(f'Hello, {name}')

hello('John')
hello('Emma')
print(hello.count)

######################################################

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f'Calling {f}')
            return f(*args, **kwargs)
        return wrap

tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

########################################################
print()
print([x/(x-y) for x in range(100) if x>50 for y in range(100) if x-y!=0])
print([(x, y) for x in range(5) for y in range(3)])
print([[y*3 for y in range(x)] for x in range(10)])
print()

sizes = ['small', 'medium', 'large']
colors = ['pink', 'purple', 'lavender']
animals = ['horse', 'dog', 'cat']

def combine(size, color, animal):
    return f'{size} {color} {animal}'

print(list(map(combine, sizes, colors, animals)))

positives = list(filter(lambda x: x>0, [0,1,2,3,-2,-3,1,-6]))
print(positives)

from functools import reduce
import operator
red = reduce(operator.mul, [1,23,4,5,6,7,7])
print(red)

import datetime
i = iter(datetime.datetime.now, None)  # forever iteration
print(next(i))
print(next(i))

# MRO - method resolution order


