# Variables first Python search:
# Local - локальные
# Enclosing (from parent functions)
# Global - глобальные
# Built-in - встроенные

def genfun(n, power):
    for x in range(1, n):
        yield x**power

for y in genfun(10, 2):
    print(y, end=' ')

gn = genfun(10, 2)
print('next: ')
print(next(gn))
print(next(gn))
print('genfun:', list(gn))


a = [1, 2, 3]
d = a

# Copy of list a:
b = a.copy()
c = a[:]

b.append(4)
c.append(5)
d.append('This is not a copy')

print(a, b, c, d)

s = 'Hello world'
for x in s:
    if x == 'a':
        break
    print(x)
else:
    print('There is no letter "a" in this variable.')

x = 50
while x < 5:
    if x % 6 == 0:
        break
    x += 1
else:
    print('There is no number from 1 to 5 which we can divide on 6 without digits after point.')

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print(a)

d = dict(a=1, b=2, c=3)
print(d)

d = dict.fromkeys(['a', 'b', 'c', 'd', 'e', 'f'], [1, 2, 3, 4, 5])
print(d)

d = {a: a ** 2 for a in range(7)}
print(d)

a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4]
a = set(a)
s = set('aaaaaaaaaabbbbbbbbbccccc')
print(a, s)

c = frozenset('qwertysssss')
print(a.isdisjoint(s))
print(a == s)
a.intersection_update(s)  # intersection of set a with set s
a.difference_update(s)
a.symmetric_difference_update(s)


########################################

def howdy():
    """Description of howdy"""
    print('Howdy')


print(howdy.__doc__)  # will print description of function

#########################################

from functools import reduce

ppl = ({'age': 12, 'name': 'Emmy', 'hobby': 'math'},
        {'age': 13, 'name': 'Tom', 'hobby': 'coding'},
        {'age': 15, 'name': 'Bob', 'hobby': 'astronomy'},
        {'age': 17, 'name': 'Samantha', 'hobby': 'math'},
        {'age': 19, 'name': 'Amanda', 'hobby': 'coding'},
        {'age': 13, 'name': 'Mikle', 'hobby': 'chemistry'}
        )

total_age = reduce(lambda acc, val: acc + val['age'], ppl, 0)
print('total_age:', total_age)

def reducer(acc, val):
    acc[val['hobby']].append(val['name'])
    return acc

people_by_field = reduce(reducer, ppl, {'math': [], 'coding': [], 'astronomy': [], 'chemistry': []})
print('people_by_field:', people_by_field)
