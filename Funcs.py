# Рекурсии
def fac(n): # factorial with recurcy
    if n<=1:
        return 1
    return n*fac(n-1)

f = fac(5)
print('Factorial of 5 is:', f)

def fac2(n): # factorial without recurcy
    count = 1
    res = 1
    while count<=n:
        res*=count
        count+=1
    return res

# Fibonacci
def fib(n):
    if n<2:
        return n
    else:
        return(fib(n-1)+fib(n-2))

fiba = fib(13)
print('Fibonacci 13:', fiba)


starts_with = lambda s: True if s[0] == 'W' else False
square_x = lambda x: x ** 2

# lambda & any & all
nums = list(1, range(21))
even = lambda x: x%2==0
print(even(3)) # False (not even)
res = [even(n) for n in nums]
if any(res):
    print('At least one number is even!')
else:
    print('No number is even!')

if all(res):
    print('All numbers are even!')


print(starts_with('Work'))
print(square_x(5))

a = [23, 45, 23, 56, 25, 65]
a.sort(key=lambda x: x%10)
print(a)

def linear(k,b):
    return lambda x: x*k+b

grafi = linear(2,5)
print(grafi(3))

graf2 = linear(-4,1)
print(graf2(3))

import datetime
now = datetime.datetime.now()
get_year = lambda x: x.year
get_month = lambda x: x.month
get_day = lambda x: x.day



blue = 'first level blue'
def colors(a, b):
    red = 'red'
    blue = 'blue'

    def c_blue(blue):
        nonlocal red
        print(blue)
        blue='changed blue'

    def red(a, b):
        global red
        print(red)
        red = 'changed red'

# Замыкания
def main_func(name='Ivan'):
    def inner_func():
        print('hello my friend', name) # it use variable above
    return inner_func

b = main_func('Panteleymon')
v = main_func('Vasya')
x = main_func()
b()
v()
x()

def adder(v):
    def inner(a):
        return v+a
    return inner

a2 = adder(2)
print(a2(5))

def counter():
    count = 0
    def inner():
        nonlocal count # for variable above
        count += 1
        return count
    return inner

def average_numbers():
    numbers = []
    summa = 0
    count = 0
    def inner(number):
        nonlocal summa
        nonlocal count
        summa = summa + number
        numbers.append(number)
        return sum(numbers)/len(numbers)
    return inner

r1 = average_numbers()
print(r1(5))

def timer():
    start = datetime.datetime.now() # imported before
    def inner():
        return datetime.datetime.now() - start
    return inner

some_time = timer()
print(some_time())

def add(a,b):
    return a+b

# def counter(Func):
#     count = 0
#     def inner(*args, **kwargs):
#         nonlocal count
#         count+=1
#         print(f'Function {func.__name__} runs {count} times')
#         return func(*args, **kwargs)
#     return inner
#
# q = counter(add)
# q(10,20)

def mult(a,b,c):
    return a+b+c

# m = counter(mult)
# print(m(12,3,3))

##############################
# Decorators
##############################

def decator(func):
    def inner(name, surname):
        print('start decorator...')
        func(name, surname)
        print('finish decorator...')
    return inner

def say(name, surname):
    print('Hello, world!', name, surname)

def buy():
    print('Buy, world!')

say = decator(say)
print(say('Vasya', 'Pupkin'))
say('Vasya', 'Pupkin')

buy = decator(buy)
print(buy())
buy()

###

from functools import wraps

def header(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('<head>')
        func(*args, **kwargs)
        print(sum(args))
        print('</head>')

    inner.__name__=func.__name__
    inner.__doc__=func.__doc__
    return inner

@header
def func2():
    print('My function')

func2(3,4,5)

def func(x):
    def add(a):
        return x+a
    return add

test = func(100)
print(test(200)) # it will call add(200)




