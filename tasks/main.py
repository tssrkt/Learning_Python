# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Input & Print

"""
a, b = map(int, input("Insert two numbers: ").split())
print("Sum of your numbers is: ", a + b)
print(1, 2, 3, sep=' <> ', end=' Yahoo!!! ')
print('I have ', a, ' and ', b, ' !!!')
print('I have %s and %s'%(a, b), ' !!!')

# Files
f = open('my_test.txt', 'w')
f.write('ababagalamaga')
f.close()

print('Canonical: ')
if a<b:
    print('a is: ', a)
else:
    print('b is: ', b)

print('Unarniy: ')
print('a is: ', a) if a<b else print('b is: ', b)

for a in [1,2,3,4,5]:
    print('iteration: ', a)

for a in range(10):
    print('iteration in rage: ', a)

# from numpy import cos
def my_func(*args): # list
    print(args)

def my_func2(**argv): # dictionary, named variables
    print(argv)

import math
print(math.trunc(25.2345))
print(math.floor(25.765))
print(math.ceil(25.165))

# Strings and lists
gender = {
    'm':'Mister',
    'f':'Miss'
}

ppl = [
    ['Vasya', 'Puplkin', '15', 'm'],
    ['Petya', 'Motykin', '20', 'm'],
    ['Marusya', 'Lopatochkina', '30', 'f']
]

for name, surname, money, g in ppl:
    x = f'Hello, {gender[g]} {name} {surname}, you have {money} USD on your account'
    print(x)


def str_name(name='Petya', surname='Pupkin', money='24'):
    x = 'Hello, {n} {s}, you have {m} USD on your acoount'.format(n=name, s=surname, m=money)
    y = f'Dear {name} {surname.upper()}, keep your {lol(money)} USD on your account'
    print(x)
    print(y)

def lol(m):
    m = int(m) + 20
    return str(m)

str_name(name='Vasya')

# Chess
a = input()
b = input()

def the_color(a):
    ltr = '0abcdefgh'
    num = int(a[1])
    buk = a[0]
    buk_num = ltr.find(buk)
    color = ''
    z = 0

    if (num%2==0 and buk_num%2==0) or (num%2!=0 and buk_num%2!=0):
        color='black'
    else:
        color='white'
    return color


a_color = the_color(a)
b_color = the_color(b)

if a_color == b_color:
    print('YES')
else:
    print('NO')

# FN
n = int(input()) + 1
fn = 0

for x in range(n):
    if x%2==0:
        fn = fn + x
    else:
        fn = fn + x*(-1)
print(fn)

# Pie
print('Pie test')
n = int(input())

if n == 1:
    n = 0
elif n%2==0:
    n = int(n/2)

print(n)

# Cities
print('Cities')

a = input().upper()
b = input().upper()

if a[-1]==b[0] or (a[-1]=='Ь' and a[-2]==b[0]):
    print('Good')
else:
    print('Bad')

# While
a = int(input())
x = 1

while a>=(x**2):
    print(x**2)
    x+=1

print('While n & m')
n = input()
m = int(n)

while n[0]!='1' and m<=1000000000:
    m = int(n[0])*m
    n = str(m)

print(m)

# <>
import math
n = int(input())
x = 1

while n>=1:
    if n%2==0:
        if n/2!=1:
            n = n/2
            x+=1
        elif n==1:
            print('0')
            n=0
        else:
            print(x)
            n=0
    elif n==1:
        print('0')
        n=0
    else:
        print('НЕТ')
        n=0


m = int(input())
mt = list(map(int, input().split()))
f = int(input())
ft = list(map(int, input().split()))

def MyFunc(x, y, xt, yt):
    res = 0
    x-=1
    y-=1
    yn = y
    for a in xt:
        y = yn
        while y>=0:
            if a==yt[y]:
                res+=1
                yt[y]=-10
                y=-1
            elif a==yt[y]-1:
                res+=1
                yt[y]=-10
                y=-1
            elif a==yt[y]+1:
                res+=1
                yt[y]=-10
                y=-1
            else:
                y-=1

    return res

if m>f:
    res = MyFunc(f, m, ft, mt)
else:
    res = MyFunc(m, f, mt, ft)

print(res)


n, k = map(int, input().split())
mins = 0
res = 0
time = 240-k

for x in range(n):
    mins+=(x+1)*5
    res+=1
    if mins > time:
        res-=1
        break

print(res)

n, m = map(int, input().split())
listn = list(map(int, input().split()))
listm = list(map(int, input().split()))

sum = listn + listm
res = []
x = 0
mx = max(sum)

while x<mx:
    z = sum.index(min(sum))
    if x==sum[z]:
        res.append(sum[z])
        del sum[z]
    else:
        x=min(sum)
res+=sum
print(*res)

# put your python code here
a = int(input())
b = input()
res = a
x=1

while x<len(b):
    if int(b[x])!=int(b[x-1]):
        res-=2
        b=b[:(x-1)]+b[(x+1):]
        x=1
    else:
        x+=1

print(res)


# put your python code here
n = int(input())
lst = []
Mishka = 0
Chris = 0

for i in range(n):
    a, b = map(int, input().split())
    lst.append([a, b])

for i in range(n):
    print(i)
    a, b = lst[i][0], lst[i][1]
    if a>b:
        Mishka+=1
    elif a<b:
        Chris+=1

if Mishka>Chris:
    print('Mishka')
elif Mishka<Chris:
    print('Chris')
else:
    print('Friendship is magic!^^')


n = int(input())
lst = []

for i in range(n):
    lst.append(input())

for i in lst:
    x = i.lower()
    if x.find('рок')!=-1:
        print(lst.index(i)+1, x.find('рок')+1)

# Next one
sum = 0
for i in range(50, 101):
    sum+=i**3

print(sum)

# Next one
a = list(map(int, input().split()))
b = []

for i in a:
    if a[a.index(i)]>0:
        b.append(a[a.index(i)])

if not b:
    print('Empty')
else:
    print(min(b))


# Next
s = input()
a = []
s = s.lower()

for i in s:
    a.append(s.count(i))

print(a)
print(max(a))


s = input()
bks = ['[]', '{}', '()']
a = s

def brks_func(s, bks):
    for i in range(len(s)-1):
        if (s[i]==bks[0][0] and s[i+1]==bks[0][1]) or (s[i]==bks[1][0] and s[i+1]==bks[1][1]) or (s[i]==bks[2][0] and s[i+1]==bks[2][1]):
            s='s' + s[:i] + s[i+2:] + 's'
    return s

s = brks_func(s, bks)
s = brks_func(s, bks)

if s.count('s')==len(s) or a=='':
    print('YES')
else:
    print('NO')


n=int(input())
res=0
for i in range(n+1, n*2):
    z=2
    for x in range(2, int(i**0.5 + 1)):
        if z<3:
            if i%x==0:
                z+=1
        else:
            break
    if z==2:
        res+=1

print(res)


n = int(input())
nums = list(map(int, input().split()))
res = 0
x = 0

while x<n*10:
    for i in range(n-1):
        x+=1
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            res += 1

print(*nums)
print(res)


n = int(input())
nums = list(map(int, input().split()))
x = 0

while x<n*100:
    for i in range(n-1):
        if nums[i]>nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
    x+=1

print(*nums)


n = int(input())
a = []
sum = 0
x = 0

for i in range(n):
    a.append(list(map(int, input().split())))

for y in range(n):
    sum += a[y][x]
    x += 1

print(sum)


# put your python code here
n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n-1, -1, -1):
    x = n - 1
    while x >= 0:
        print(a[x][i], end=' ')
        x -= 1
    print()


n, m = map(int, input().split())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n - 1, -1, -1):
    x = 0
    while x < n:
        print(a[x][i], end=' ')
        x += 1
    print()


# put your python code here
n, m = map(int, input().split())
a = []
rows = []
cols = []

for i in range(n):
    a.append(list(map(int, input().split())))
    rows.append(0)

for i in range(m):
    cols.append(0)

for i in range(n):
    x = 0
    while x < m:
        rows[i] = rows[i] + a[i][x]
        x += 1
    print()

for i in range(m):
    x = 0
    while x < n:
        cols[i] += a[x][i]
        x += 1
    print()

print(*rows)
print(*cols)


a = []
res = 'Yes'

for i in range(4):
    a.append(input())

for i in range(3):
    for x in range(3):
        if a[i][x] == a[i][x + 1] == a[i + 1][x] == a[i + 1][x + 1]:
            res = 'No'
            break

print(res)


# put your python code here
n, m = map(int, input().split())
a1 = []
a2 = []
res = 0
tuk = False

for i in range(n):
    a1.append(input())

input()

for i in range(n):
    a2.append(input())

for i in range(n):
    for j in range(m):
        if a1[i][j] == a2[i][j]:
            res += 1

print(res)


n = int(input())
a = []
res = 0

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n - 1):
    if a[i][0] == a[i + 1][1]:
        if a[i + 1][0] == a[i][1]:
            res += 3
        else:
            res += 1
    elif a[i][1] == a[i + 1][0]:
        res += 1

print(res)


# put your python code here
n, m = map(int, input().split())
a = []
res = 0

for i in range(n):
    a.append(input())

def kuts(*args):
    for i in args:
        if i == '*':
            return 0
    return 1

for i in range(n):
    for j in range(m):
        if a[i][j] == '.':
            if i == 0:
                if j == 0:
                    res += kuts(a[0][1], a[1][0], a[1][1])
                elif j == m - 1:
                    res += kuts(a[0][j - 1], a[1][j - 1], a[1][j])
                else:
                    res += kuts(a[0][j - 1], a[0][j + 1], a[1][j - 1], a[1][j], a[1][j + 1])
            elif i == n - 1:
                if j == 0:
                    res += kuts(a[i][j + 1], a[i - 1][j + 1], a[i - 1][j])
                elif j == m - 1:
                    res += kuts(a[i][j - 1], a[i - 1][j - 1], a[i - 1][j])
                else:
                    res += kuts(a[i][j - 1], a[i][j + 1], a[i - 1][j - 1], a[i - 1][j], a[i - 1][j + 1])
            elif j == 0:
                res += kuts(a[i - 1][j], a[i - 1][j + 1], a[i + 1][j], a[i + 1][j + 1], a[i][j + 1])
            elif j == m - 1:
                res += kuts(a[i - 1][j], a[i - 1][j - 1], a[i + 1][j], a[i + 1][j - 1], a[i][j - 1])
            else:
                res += kuts(a[i - 1][j - 1], a[i - 1][j], a[i - 1][j + 1], a[i + 1][j - 1], a[i + 1][j],
                            a[i + 1][j + 1], a[i][j - 1], a[i][j + 1])

print(res)


# put your python code here
n, m = map(int, input().split())
x = 1
y = 0
a = [0]


def snake(x, m, y):
    a = []
    if x == 1:
        for j in range(0 + y, m + y):
            a.append(j)
    else:
        for j in range(y + (m - 1), m + (y - m) - 1, -1):
            a.append(j)
    return (a)


for i in range(n):
    a = snake(x, m, y)
    if a[0] == 0:
        b = ''
        for k in a:
            b += str(a[k]) + '  '
        print(b)
    else:
        print(*a)
    y += m
    if x == 1:
        x = 0
    else:
        x = 1


# Hellish swirl
# put your python code here
n = int(input())
a = []

for x in range(n):
    a.append(list())
    for y in range(n):
        a[x].append(0)

u = 0
l = 0
r = n - 1
d = n - 1

zuka = 1
rng = n

for x in range(n * 2 - 1):
    if x>=(n*2-1)-2:
        if n%2==0:
            a[(n//2)][(n//2)]=zuka
            zuka+=1
            a[(n//2)][(n//2)-1]=zuka
        else:
            a[(n+1)//2-1][(((n+1)//2)-1)-1]=zuka
            zuka+=1
            a[(n + 1) // 2 - 1][(n + 1) // 2 - 1] = zuka

    if zuka>(n**2):
        break

    if x % 4 == 0:
        for y in range(rng):  # upper
            a[u][l + y] = zuka
            zuka += 1
        rng -= 1
        u += 1
    if x % 4 == 1:
        for y in range(rng):  # right
            a[u + y][r] = zuka
            zuka += 1
        r -= 1
    if x % 4 == 2:
        for y in range(rng):  # down
            a[d][n - (r + y)] = zuka
            zuka += 1
        rng -= 1
        d -= 1
    if x % 4 == 3:
        for y in range(rng):  # left
            a[n - (d + y)][l] = zuka
            zuka += 1
        l += 1



for i in a:
    print(*i)
"""

# put your python code here
n, m = map(int, input().split())
res = 0

for i in range(n):
    s = input()
    res += s.count('S')

print(n * m - res)


# Ctrl + Alt + L - format
# Ctrl + F5 - run or debug

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""
4
1 4 6 2
5
5 1 5 7 9
"""
