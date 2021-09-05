
d = {
    # key : value,
    'lopata' : 12,
    'vedro' : 13,
    1 : 'one',
    2 : 'two',
    3: 'three'

}

d[4] = 'four'
d[3] = 'THREE'

print('d:', d)
print(d.get(1))
print(d.setdefault(5, 'five'))
print(d.setdefault(2, 'TWO'))
print(d.pop(3)) # deleted 3
print('d:', d)
print(d.keys())

for value in d.values():
    print(value)

print(d.items())

print('*'*20)
a = [['abc', 2], ['bcd', 3]]

r = dict(abc=2, bcd=3)
print(r)

t = dict(a)

q = dict.fromkeys(['abc', 'cdb', 'bcd'], 100)
print('q:', q)

# # #
print('***'*50)

from string import ascii_lowercase
a = ascii_lowercase

alphabet = {}

print(a)

for i in range(26):
    alphabet.setdefault(a[i], i+1)
    print(a[i], i+1)

print(alphabet)

print('<>'*50)

d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}

print(d1 | d2)

heroes = {
    'Spider-Man': 80,
    'Batman': 65,
    'Superman': 75
}

for i in sorted(heroes.items(), key=lambda para: (para[1], para[0])):
    print(i)

s = 'ababagalamaga'
d = {}
for i in s:
    if i.isalpha():
        d[i] = d.get(i, 0) + 1

for i in sorted(d):
    print(i, d[i])

# GENERATORS
# list generator
a = [i**2 for i in range(1, 11)]
print('a:', a)

# Dictionary generator (key:value)
a1 = {i:i**2 for i in range(1, 11)}
print('a1:', a1)

a2 = {word:len(word) for word in ['hello', 'hi', 'world', 'lopata', 'crabik']}
print('a2:', a2)

data = {
    'Superman': 15,
    'Batman': 25,
    'Aquaman': 30
}

new_data = {key.title().upper(): int(value)*2 for key, value in data.items()}
print('data:', data)
print('new data:', new_data)

# Other
myd=dict(Spiderman=123,Superman=456,Batman=789)
print(myd)

from collections import OrderedDict
d1 = OrderedDict(a=1,b=2,c=3)
print(d1)
