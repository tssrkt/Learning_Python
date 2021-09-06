# pypi.org - find any module
# from math import factorial
# from math import * - bad manner
# import .anyfile - file above this directory
# importing my modules:
# import Triangle_Pascal
import my_modules.my_module
import math as m

print('Hello, world!')
print(m.factorial(10))
print(my_modules.my_module.x)

###################################

from typing import TypeVar, Generic
from logging import Logger

T = TypeVar('T')

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)

from typing import Iterable

def zero_all_vars(vars: Iterable[LoggedVar[int]]) -> None:
    for var in vars:
        var.set(0)

###############################################
print('*'*50)
print('Useful modules')
print()

# copy lists and objects
import copy

class Auto():
    pass

auto1 = Auto()
auto1.wheels = 4
auto2 = copy.copy(auto1)
auto2.wheels = 8

print(auto1.wheels)
print(auto2.wheels)

# is word system
import keyword

print(keyword.iskeyword('if')) # True (if belong to python)
print(keyword.iskeyword(('catdog'))) # False

# random numbers
import random

num = random.randint(1, 100)
print(num) # random number from 1 to 100

# while True:
#     print('Insert number from 1 to 100:')
#     num1 = int(input())
#     if num1 == num:
#         print('Good of you!')
#         break
#     elif num1 == 0:
#         print('Exit!')
#         break
#     else:
#         print('Did not guess!')

# working with system
import sys

if False:
    sys.exit()

print('stdin')
in1 = sys.stdin.readline()
print(in1)
sys.stdout.write(in1)

# version of python
print(sys.version)

# working with time
import time

# time now in seconds from 1 January 1970
print(time.time())

# human friendly format of time
print(time.asctime())

# structure (year, month, day and etc.)
print(time.localtime())

t1 = time.localtime()
print('Year:', t1[0])

for x in range(1, 5):
    print(x)
    # wait a second
    time.sleep(1)

# saving difficult objects in file and work with it
import pickle

game = {'life': 5, 'armor': 7, 'level': 100}
file1 = open('test.txt', 'wb')
pickle.dump(game, file1)
file1.close()

load_file = open('test.txt', 'rb')
loaded = pickle.load(load_file)
load_file.close()

print(loaded)

# working with money (decimal is better than float)
from decimal import Decimal
deci = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
print(deci)
print(deci==0.3)

print()
print('*' * 50)
print('dataclasses')

# more simple working with classes
from dataclasses import dataclass, field

@dataclass(order=True) # order if many objects in one print
class MyClass:
    # init & repr:
    x: int
    y: int = field(compare=False)
    z: int = field(repr=False, default=6) # will not showed in repr

    def __post_init__(self):
        self.generated_attr = self.x + self.y + self.z

m1 = MyClass(1, 2, 3)
print(m1)
print(m1.generated_attr)

m2 = MyClass(4, 5)
print(m1, m2) # ordered

@dataclass(frozen=True) # no changing attributes
class M2:
    x: int
    y: int

m4 = M2(1,2)




