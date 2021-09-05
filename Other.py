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

while x < 5:
    if x % 6 == 0:
        break
    x += 1
else:
    print('There is no number from 1 to 5 which we can divide on 6 without digits after point.')

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print(a)

d = dict(a=1,b=2,c=3)
print(d)

d = dict.fromkeys(['a', 'b', 'c', 'd', 'e', 'f'], [1, 2, 3, 4, 5])
print(d)

d = {a:a**2 for a in range(7)}
print(d)

a = [1,1,1,2,2,2,3,3,3,4,4]
a = set(a)
s = set('aaaaaaaaaabbbbbbbbbccccc')
print(a, s)

c = frozenset('qwertysssss')
print(a.isdisjoint(s))
print(a==s)
a.intersection_update(s) # intersection of set a with set s
a.difference_update(s)
a.symmetric_difference_update(s)

