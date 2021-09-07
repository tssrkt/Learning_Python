class Person:
    name = 'Vasya'
    surname = 'Pupkin'
    age = 25

    def say(self):
        print('Hello, World!')

man = Person()

# set new attribute
setattr(Person, 'x', 200)
setattr(Person, 'y', 200)
Person.z = 100

# delete attribute
del Person.x
delattr(Person, 'y')

# get attribute
getattr(Person, 'age')
print(Person.age)

a1 = Person()
a2 = Person()

# All attributes of class
Person.__dict__
a1.__dict__

a1.seat = 4
a1.name = 'Marusya'

# call attribute
a1.say()
getattr(Person, 'say')
a2.say()
a2.say

class Cat:
    breed = 'persian'
    name = 'Vasya'
    age = '5'

    def show_bread(self):
        print(f'My breed is {self.breed}')

    def hello(self):
        print(f'Hello world from kitty {self.name}')

bob = Cat()
bob.name = 'Bob'
bob.show_bread()
bob.hello()

###########################

class Dog:

    def __init__(self, name, breed='ovcharka', age=1, color='red'):
        print('Hello new object is ', self, name, breed, age, color)
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

tuzik = Dog('Tuzik', 'pudel', 5, 'white')
sharik = Dog('Sharik', 'chihuahua')

########################################

from math import sqrt

class Point:
    list_points = []

    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f'Point with coordinates ({self.x}, {self.y})')

    def dist(self, other_point):
        if not isinstance(other_point, Point):
            raise ValueError('Argument should belong to class Point!')

        return sqrt((self.x-other_point.x)**2+(self.y-other_point.y)**2)

p1 = Point(1)
p1.move_to(2, 3)
p1.go_home()
p1.move_to(4, 10)
p1.print_point()

p2 = Point(2, 9)
print(p1.dist(p2))

class Horse:
    __shared_attr = {
        'name' : 'Wind',
        'breed' : 'arabian',
        'color' : 'black'
    }

    def __init__(self):
        self.__dict__ = Horse.__shared_attr

h1 = Horse()
h2 = Horse()
h1.breed = 'freezian'
h1.name = 'Hoost'

print(h2.name)
print(h1.name)

#######################################

class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    # def print_data(self):
    #     print(self.name, self.balance, self.passport)

    def __print_data(self):
        print(self.__name, self.__balance, self.__passport)
        # __ is protected (инкапсуляция)

    def print_all(self):
        self.__print_data()

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Balance should be number!')
        self.__balance = value

    def delete_balance(self):
        print('delete balance')
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)
    # The same:
    my_bal = property(get_balance)
    # my_bal = my_bal.getter(get_balance)
    my_bal = my_bal.setter(set_balance)
    my_bal = my_bal.deleter(delete_balance)

acc1 = BankAccount('Bob', 10000, 4564465544)
# acc1.__print_data()
acc1.print_all()
print(dir(acc1))
print(acc1._BankAccount__balance)
acc1.balance = 777
print(acc1.balance)

# module accessify for protecting variables inside classes

class Account:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('get balance')
        return self.__balance

    # my_property_balance = my_balance

    @my_balance.setter
    def my_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Balance should be number')
        self.__balance = value

    @my_balance.deleter
    def delete_balance(self):
        print('delete balance')
        del self.__balance

    # my_balance = my_property_balance.setter(my_balance)

#############################

class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            print('Calculate area')
            self.__area = self.side**2
        return self.__area

a = Square(5)
# print('Area of square a is', a.area())

################################

class Example:
    # cal from class (not from exemplar)
    def hello():
        print('Hello world!')

    # call from exemplar (not form class)
    def instance_hello(self):
        print(f'Instance hello {self}')

    # calling from class & exemplar use @staticmethod:
    @staticmethod
    def static_hello():
        print('Static Hello!')

    # working with class not with exemplar:
    @classmethod
    def class_hello(cls):
        print(f'Class hello {cls}')
        # cls is about class

################################################

from string import digits

class User:

    def __init__(self, login, password):
        self.login = login
        self.__password = password

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @property
    def password(self):
        print('getter')
        return self.__password

    @password.setter
    def password(self, value):
        print('setter')
        if not isinstance(value, str):
            raise TypeError('Password should be string!')
        if len(value)<4:
            raise ValueError('Too shord password! Minimum is 4 signs')
        if len(value)>12:
            raise ValueError('Too long password! Maximum is 12 signs')
        if not User.is_iclude_number(value):
            raise ValueError('Password should contain at least one digit')
        self.__password = value

u1 = User('Vasya', 'sdf123')

#########################################################

class Lion:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'The object Lion - {self.name}'

    def __str__(self):
        return f'Lion - {self.name}'

q = Lion('Simba')

####################################

class Acc:
    def __init__(self, name, balance):
        print('new_obj init')
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('add')
        if isinstance(other, Acc):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return Acc(self.name, self.balance+other)
        raise NotImplemented

    # for to do 12+r (number first)
    def __radd__(self, other):
        print('radd')
        return self+other

    def __mul__(self, other):
        print('mul')
        if isinstance(other, Acc):
            return self.balance * other.balance
        if isinstance(other, (int, float)):
            return self.balance * other
        if isinstance(other, str):
            return self.name + other
        raise NotImplemented

    def __repr__(self):
        return f'Client {self.name} with balance {self.balance}'

r = Acc('Misha', 78)
r += 12

k = Acc('Katya', 58)
k = k+r

###########################################

class HelloWorld:
    def __init__(self, num_iters):
        self.num_iters = num_iters
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.num_iters:
            self.counter += 1
            return 'Hello World!'
        raise StopIteration

gr = HelloWorld(3)
for x in gr:
    print(x)

names = ['Bob', 'Mikle', 'Samantha', 'Jhon', 'Amanda', 'Vasya']
for x, name in enumerate(names, start=1):
    print(x, name)

for x, name in enumerate(names, start=1):
    team = 'Red' if x%2 else 'Blue'
    print(x, team, name)

def my_enum(sequence, start=0):
    for x in sequence:
        yield start, item
        start += 1

class StringByLetter:
    def __init__(self, string):
        self.string = string
        self.str_len = len(string)
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < self.str_len:
            letter = self.string[self.position]
            self.position += 1
            return letter.upper()
        raise StopIteration

for letter in StringByLetter('hello world'):
    print(letter, end=' ')
print()

def string_by_letter(string):
    for letter in string:
        yield letter.upper()

for letter in string_by_letter('hello world'):
    print(letter, end=' ')
print()

from collections.abc import Iterator
gen = string_by_letter('hello world')
isinstance(gen, Iterator)

def invalid_oper():
    raise Exception('Only operations: +, -, * and /')

def do_math(x, y, oper='+'):
    opers = {
        '+': lambda x,y: x+y,
        '-': lambda x,y: x-y,
        '*': lambda x,y: x*y,
        '/': lambda x,y: x/y,
    }
    op_func = opers.get(oper)
    return op_func(x, y)

dm = do_math(2, 3, '*')
print('do math:', dm)
print('*'*50)

#######################################################

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

user = User('simple_user', 'user')
admin = User('root', 'admin')
current_user = user

def do_admin_work():
    if current_user.role != 'admin':
        raise Exception('Access denied')
    return 'Do something administoe'

do_admin_work()

def do_admin_work2():
    return 'Do admin 2'

def check_access(func):
    if current_user.role != 'admin':
        raise Exception('Access denied')
    return func()

check_access(do_admin_work2)

def check_access2(func):
    def wrapper():
        if current_user.role != 'admin':
            raise Exception('Access denied')
        return func()
    return wrapper

do_admin_work2.__name__
do_admin_work2 = check_access2(do_admin_work)

@check_access2
def do_admin_work3():
    return 'Do admin 3'


