"""
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

print([x[y] for x in vector for y in range(3)])

a = [[i*j for i in range(1, 10)] for j in range(1, 10)]
print('*'*10)
for i in a:
    print(i)
print('*'*10)


# put your python code here
n = int(input())
a = []

for i in range(n):
    a.append(input())

d = {}
res = [0]*n

for i in range(n):
    num = a.count(a[i])
    d.setdefault(a[i], num-1)

for i in range(n-1, -1, -1):
    if d.get(a[i])>=1:
        res[i] = a[i] + str(d.get(a[i]))
        m = d.get(a[i])-1
        d[a[i]] = m
    else:
        res[i] = 'OK'

for i in range(n):
    print(res[i])


d = {}
a = ''
b = []

while a!='конец':
    a=input()
    if a!='конец':
        b = a.split(': ')
        d.setdefault(int(b[1]), b[0])
        b = []
    else:
        break

w = sorted(d.keys(), reverse=True)

for i in w:
    print(d.get(i))


# put your python code here
d = {}
a = ''
b = []

while a!='конец':
    a=input()
    if a!='конец':
        b.append(a.split(', '))
    else:
        break

c = {}

for i in b:
    d.setdefault(i[0], 0)
    c.setdefault(i[0], 0)

for x in d.keys():
    for i in b:
        if x==i[0]:
            d[x] = d.get(i[0]) + int(i[1])
            c[x] = c.get(i[0]) + 1

res = {}

for i in c.keys():
    res.setdefault(i, d.get(i)/c.get(i))

for key, value in sorted(res.items(), key=lambda para: (-para[1], para[0])):
    print(key, value)


# put your python code here
n = int(input())
d = {}
c = []
zap = []

for i in range(n):
    c.append(list(map(str, input().split())))

m = int(input())

for y in range(m):
    zap.append(input())

# Body
for i in c:
    d.setdefault(i[1], list())

for z in d.keys():
    for y in c:
        if z==y[1]:
            q = d.get(z)
            q.append(y[0])
            d[z] = q

# Res
res = []

for y in zap:
    if d.get(y):
        res.append(d.get(y))
    else:
        res.append(['Неизвестный номер'])

for i in res:
    print(*i)


# put your python code here
s = str(input())
d = {}

for x in s:
    if x.isalpha():
        x = x.lower()
        d[x] = d.get(x, 0) + 1

print(d)


data = {'my_friends': {'count': 10,
                       'items': [{'first_name': 'Kurt', 'id': 621547005, 'last_name': 'Cobain', 'bdate': '31.8.2005'},
                                 {'first_name': 'Виолетта', 'id': 484200150, 'last_name': 'Кастилио'},
                                 {'first_name': 'Иринка', 'id': 21886133, 'last_name': 'Бушуева', 'bdate': '28.8.1942'},
                                 {'first_name': 'Данил', 'id': 282456573, 'last_name': 'Греков', 'bdate': '4.7.2002'},
                                 {'first_name': 'Валентин', 'id': 184902932, 'last_name': 'Долматов', 'bdate': '25.5'},
                                 {'first_name': 'Евгений', 'id': 620469646, 'last_name': 'Шапорин',
                                  'bdate': '6.12.1982'},
                                 {'first_name': 'Ангелина', 'id': 622328862, 'last_name': 'Краснова',
                                  'bdate': '4.11.1995'},
                                 {'first_name': 'Иван', 'id': 576015198, 'last_name': 'Вирин', 'bdate': '2.2.1915'},
                                 {'first_name': 'Паша', 'id': 386922406, 'last_name': 'Воронов', 'bdate': '27.9'},
                                 {'first_name': 'Ольга', 'id': 622170942, 'last_name': 'Савченкова',
                                  'bdate': '20.12'}]}}



# put your python code here
s1 = input()
s2 = input()
res = 'YES'

if len(s1)==len(s2):
    for x in s1:
        if s1.count(x) == s2.count(x):
            res = 'YES'
        else:
            res = 'NO'
            break
else:
    res = 'NO'

print(res)



morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}

s = list(map(str, input().split()))

for i in s:
    i = i.lower()
    word = ''
    for x in i:
        word += morze.get(x) + ' '
    print(word)


# put your python code here
s = input()
res = ''

for i in range(len(s) - 1, -1, -1):
    x = s[i]
    if s[:(i + 1)].count(x) > 1:
        if res=='':
            res = s[:i] + s[(i + 1):]
        else:
            res = res[:i] + res[(i + 1):]

print(res)


# put your python code here
dili = []
bili = []
vili = []
s = ''

while s != 'конец':
    a = []
    s = input()
    if s == 'конец':
        break
    else:
        a = list(map(str, s.split()))
        if a[0] == 'Дили:':
            dili.append(a[1])
        elif a[0] == 'Били:':
            bili.append(a[1])
        else:
            vili.append(a[1])


def unicus(a=[]):
    res = []
    for i in range(len(a) - 1, -1, -1):
        x = a[i]
        if res.count(a[i]) == 0:
            res.append(a[i])
    return len(res)


def rng(a, b):
    c = {}
    u = ''
    for i in range(len(a)):
        num = unicus(b[i])
        str_res = f'Количество уникальных комментаторов у {a[i]} - {num}'
        c[num] = str_res
    for i in sorted(c, reverse=True):
        print(c.get(i))


names = ['Дили', 'Били', 'Вили']
comms = [dili, bili, vili]
rng(names, comms)


# put your python code here
s = input()
res = []
answ = 'IGNORE HIM!'

for i in s:
    if res.count(i) == 0:
        res.append(i)

if len(res) % 2 == 0:
    answ = 'CHAT WITH HER!'
print(answ)


# put your python code here
a = list(map(int, input().split()))
b = []

for i in a:
    if b.count(i)==0:
        b.append(i)

print(4 - len(b))


# put your python code here
a = list(map(str, input().split()))
b = []
res = 0

if len(a)==1:
    for i in a:
        if len(i)==3:
            res = 1
else:
    for i in a:
        y = 0
        for x in i:
            if x=='{':
                y = i[1]
                break
            elif x==',' or x=='}':
                y = i[-2]
                break
        if b.count(y) == 0:
            b.append(y)
    res = len(b)

print(res)


# put your python code here
n = int(input())
s = input()
s = s.lower()
res = ''

import string

st = string.ascii_lowercase

for x in st:
    if s.count(x) > 0:
        res = 'YES'
    else:
        res = 'NO'
        break

print(res)


# put your python code here
v = int(input())
t = int(input())
x = v * t

while x >= 109 or x < 0:
    if x > 0:
        x -= 109
    elif x < 0 and abs(x) < 109:
        x = 109 + x
    else:
        x = abs(x) - 109

print(x)


def longest_word_in_file(file_name):
    from string import punctuation

    f = open(file_name, encoding='utf-8')
    txt = f.read()
    f.close()

    punks = punctuation
    for x in punks:
        txt = txt.replace(x, '')

    d = {}
    txt = list(txt.split())
    for x in txt:
        d.setdefault(x, len(x))

    v = list(d.values())
    mx = max(v)
    res = [k for k, v in d.items() if v == mx]
    return res[-1]

###############################

def nums(file_name):
    f = open(file_name, encoding='utf-8')
    txt = f.read()
    f.close()

    tri = 0
    sm = 0
    txt = list(txt.split())
    for x in txt:
        if len(x)==3:
            tri+=1
        elif len(x)==2:
            sm+=int(x)
    print('Count of 3-digit numbers:', tri)
    print('Sum of 2-digit numbers:', sm)

# nums('numbers.txt')
###############################

# JSON
import json
with open('manager_sales.json', 'r') as f:
    data = json.load(f)

res = {}
for i in data:
    man = i['manager']['first_name'] + ' ' + i['manager']['last_name']
    money = 0
    for x in i['cars']:
        money += x['price']
    res.setdefault(man, money)

lst = res.values()
mx = max(lst)
best = {k:v for k,v in res.items() if v==mx}
print(best)


###############################
import json
with open('group_people.json', 'r') as f:
    data = json.load(f)

res = {}
for i in data:
    for x in i['people']:
        if x['gender']=='Female' and x['year']>1977:
            if res.get(i['id_group'])!=None:
                y = res.get(i['id_group'])+1
                res[i['id_group']] = y
            else:
                res.setdefault(i['id_group'], 1)
lst = res.values()
mx = max(lst)
max_id = [k for k,v in res.items() if v==mx]
max_id = max_id[0]
print(max_id, mx)


###############################
import json
from string import punctuation

with open('Alphabet.json', 'r') as f:
    data = json.load(f)

f = open('Abracadabra.txt', 'r', encoding='utf-8')
txt = f.read()
f.close()

pks = punctuation
res = ''
for i in txt:
    if i in pks or i==' ' or i=='\n':
        res += i
    elif i.islower():
        i = i.upper()
        res += data.get(i).lower()
    elif i.isupper():
        res += data.get(i)

print(res)


###############################

days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
res = list(filter(lambda x: len(x)==4 or x[0]=='S', days))
res = sorted(res)

for i in res:
    print(i)


###############################
models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
          {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
          {'make': 'Apple', 'model': 10, 'color': 'Silver'},
          {'make': 'Oppo', 'model': 9, 'color': 'Red'},
          {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
          {'make': 'Honor', 'model': 3, 'color': 'Black'}]

models = sorted(models, key=lambda x: x['color'].lower())
a = {'Производитель': 0, 'модель': 0, 'цвет': 0}
res = []
for x in range(7):
    res.append({'Производитель':models[x]['make'],
                'модель':models[x]['model'],
                'цвет':models[x]['color']})


for x in res:
    for k,v in x.items():
        if k=='цвет':
            z = ''
        else:
            z = ', '
        print(str(k) + ': ' + str(v), end=z)
    print()
"""

###############################





