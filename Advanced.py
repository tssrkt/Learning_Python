a = [1, 2, 3]
d = iter(a)
print(next(d))
print(next(d))

a = [i ** 2 for i in range(1, 6)]
print(a)

b = (i ** 2 for i in range(1, 6))
print(b)  # will show b because it's first time
print(b)  # will not show any b !!!
print(list(b))  # will show list


# Function-generator
# Функция генератор
def genf():
    for i in [45, 35, 23]:
        s = 7
        yield i  # return i, this freeze i
        print(s)
        s = s * 10 + 7


s = genf()
print(s)  # s is generator
print(next(s))  # first item of list

for i in genf():
    print(i)


# Usage of function-generator
# 1. Saving memory

def fact(n):
    pr = 1
    a = []
    for i in range(1, n + 1):
        pr = pr * i
        yield pr


q = fact(10)
print(q)

for i in fact(10):
    print(i, end=' ')

# Map function
a = [-1, 2, -3, 4, 5]
b = list(map(abs, a))
c = [abs(i) for i in a]
s = ['ababa', 'gala', 'maga', '123']
s_len = list(map(len, s))
s_up = list(map(str.upper, s))
d = list(map(lambda x: x[::-1], s))
e = [i[::-1] for i in s]
f = list(map(list, s))
g = list(map(sorted, f))

# Filter
a = [1, 2, 0, 0, 3, 2, 5, 6, 4, 0, 12, 34, 23]
f1 = [i for i in a if i > 9 and i < 100]
f2 = list(filter(bool, a))
f3 = list(filter(lambda x: len(a)>4, a))
b = list(filter(str.isdigit, s))

print()
print('*'*50)
print(f1)
print(f2)
print(f3)
print(b)
print('*'*50)

d = {
    'aba': 33,
    'bab': 36,
    'gal': 23,
    'mag': 12
}

f4 = list(filter(lambda x: d[x]>10, d))

# Zip
a = [5, 6, 7 , 8]
b = [100, 200, 300, 400]

rez = zip(a, b)
print(list(rez))

# sorting
a.sort() # Only for lists
a = sorted(s, reverse=False) # Return list
print(sorted(b, key=abs))

def fu(x):
    return x%10, x//10%10

print(sorted(b, key=fu))
print(sorted(s, key=str.lower))
# print(sorted(s, key=lambda x: (-int(x.split()[1]), x.split()[0].lower()), reverse=True)) # sort 'string 123' etc. If nums same - sort by alphabet

a = ['a', 'baba', 'gala', 'maga123', 'a3', 'b1', 'sfs2344']
# a = sorted(a, key=lambda x: -int(x.split()[0]))
a = sorted(a, key=lambda x: x.split()[0].lower(), reverse=True)
print(a)
s.sort(key=len) # sort by length of strings

# isinstance
a = [5,3,4,'hello',[3,4],'world',[5],10.5]
st = ''
lst = []
nums = 0
for i in a:
    if isinstance(i, str):
        st+=i
    elif isinstance(i, list):
        lst=lst+i
    elif isinstance(i, (int, float)):
        nums = nums + i

# all & any
s = ['hello', 'ababa', 'gala', 'maga', '']
print(all(s)) # all in list or tuple True or False
print(any(s)) # if any is not empty then True

# callable - вызываемый объект
x = 10
print(callable(x))

# module collection
from collections import Counter
nums = Counter(s)
print(nums)
for i in nums.elements():
    print(i)

nums.most_common()

r = Counter()
for i in [1,2,3,3,4,5,5,5,5]:
    r[i]+=1
print(r)

d = Counter([1,2,3,4,5,5,5])
print(r+d)
print(d+r)

# defaultdict
# defaultdict(int, {'s':3})
# m = defaultdict(list)
# k = defaultdict(set)

# namedtuple
# PointV2 = namedtuple('PointV2', 'x y')
# print(PointV2)
# p1 = PointV2(2,3)
# print(p1[0])
# p2 = PointV2(y=10, x=43)
# print(p2.y)

# Human = namedtuple('Person', 'name surname date country')
# z = Human(name='Jessica', surname='Doolitl', date='12.07.1943', country='England')
# print(isinstance(z, tuple))
# print(z.name)

################################
# ITERTOOLS
################################
print('ITERTOOLS')
import itertools

s = 'cat dog horse'
words = s.split()
res = list(itertools.permutations(words))
print('res:', res)

for x in itertools.permutations(words):
    print(' '.join(x))

###############################
# try except

# try:
#     y = int(input())
# except ValueError:
#     print('Insert number please!')
#     y = 0
# else:
#     print('You inserted number.')
# finally:
#     print('Will be executed 100%')

######################################
# Iterators
print('Iterator')

nums = [1,2,3]
i_nums = iter(nums)

while True:
    try:
        a = (next(i_nums))
        print(a)
    except StopIteration:
        break

class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

nums = MyRange(1, 10)

for num in nums:
    print(num)

print(next(nums))


