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

