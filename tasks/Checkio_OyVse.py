def rs(price, a):
    res = 0
    for x in a:
        if price == 0:
            break
        while price >= x:
            res += 1
            price -= x
    if price == 0:
        return res
    return None


def checkio(price, a):
    """
        return the minimum number of coins that add up to the price
    """
    a = sorted(a, reverse=True)
    res = []
    while len(a) > 0:
        z = rs(price, a)
        if z != None:
            res.append(z)
        del a[0]

    if res == []:
        return None
    return min(res)


# print(checkio(123456,[1,6,7,456,678])) # == 187
# print(checkio(8, [1, 3, 5])) # == 2
# print(checkio(12, [1, 4, 5])) # == 3

def lines(m):
    # horizintal
    for x in m:
        if len(set(x)) == 1:
            return True

    # vertical
    for x in range(len(m)):
        a = []
        for y in range(len(m)):
            a.append(m[y][x])
        if len(set(a)) == 1:
            return True


def di(m, m_start, m_end, step, ahead=True, up=False):
    if not up:
        m_end_1 = m_end - 2
        m_end_2 = m_end
    else:
        m_end_1 = m_end + 3
        m_end_2 = m_end - 2


    for y in range(m_start, m_end_1, step):
        for x in range(m_start, m_end_2, step):
            if ahead and not up and m[y][x] == m[y + 1][x - 1] == m[y + 2][x - 2] == m[y + 3][x - 3]:
                return True
            elif not ahead and not up and m[y][x] == m[y + 1][x + 1] == m[y + 2][x + 2] == m[y + 3][x + 3]:
                return True
            elif ahead and up and m[y][x] == m[y - 1][x + 1] == m[y - 2][x + 2] == m[y - 3][x + 3]:
                return True
    return False

def diago(m):
    if len(m[0]) < 4:
        return False

    if di(m, 3, len(m), 1, True, False): return True
    if di(m, 0, len(m), 1, False, False): return True
    if di(m, len(m), 3, -1, True, True): return True

    return False


def checkio(matrix: List[List[int]]) -> bool:
    if lines(matrix) or diago(matrix):
        return True
    return False


# print(checkio([
#     [7, 1, 1, 8, 1, 1],
#     [1, 1, 7, 3, 1, 5],
#     [2, 3, 1, 2, 5, 1],
#     [1, 1, 1, 5, 1, 4],
#     [4, 6, 5, 1, 3, 1],
#     [1, 1, 9, 1, 2, 1]
# ]))

# Пока не знаю как решить задачку с диагоналями


def checkio(s, s3=None):
    a = [s.count('(') - s.count(')'), s.count('[') - s.count(']'), s.count('{') - s.count('}')]
    b = ['(', '[', '{']
    c = [')', ']', '}']
    d = c + b

    for x in range(len(a)):
        if a[x] != 0:
            return False

    if s3 != None:
        res = checkio(s3)
        if res==True:
            s3==None

    ou = [x for x in d if x in s]
    if len(ou)==0 and s3==None:
        return True

    res = False
    for x in range(len(s)):
        if s[x] in b:
            z = b.index(s[x])
            if c[z] in s:
                n = s.rfind(c[z])
                s2 = s[x + 1:n]
                if n!=len(s)-1:
                    s3 = s[n:]
                else:
                    s3 = None
                res = checkio(s2, s3)
                if res==True:
                    break
            else:
                break

    return res


# print(checkio("[1+202]*3*({4+3)}"))
# print(checkio("((5+3)*2+1)"))
# print(checkio("(3+{1-1)}"))











def sm(a, b, x, costs):
    res = []
    for y in x:
        if y != a and isinstance(y, str):
            for z in costs:
                if y in z and b in z:
                    res.append(costs[costs.index(z)][-1] + costs[costs.index(x)][-1])
    next = ''
    sm = 0
    for x in costs:
        if next in x:
            if b in x:
                sm += x[-1]
                res.append(sm)
                break

            for y in x:
                if y != next and isinstance(y, str):
                    sm += x[-1]
                    next = y
                    break

        if next == '' and a in x and b not in x:
            for y in x:
                if y != a and isinstance(y, str):
                    sm += x[-1]
                    next = y
                    break
    return res


def cheapest_flight(costs: List, a: str, b: str) -> int:
    prices = []
    A, B = 0, 0
    for x in costs:
        if a in x and b in x:
            prices.append(x[-1])
        elif a in x and b not in x:
            res = sm(a, b, x, costs)
            prices.extend(res)
        elif b in x and a not in x:
            res = sm(b, a, x, costs)
            prices.extend(res)

    if prices == []:
        return 0

    return min(prices)


# print(cheapest_flight([["A","C",40],["A","B",20],["A","D",20],["B","C",50],["D","C",70]],"D","C"))
# print(cheapest_flight([["A","C",100],["A","B",20],["D","F",900]],"A","F"))
# print(cheapest_flight([["A","C",40],["A","B",20],["A","D",20],["B","C",50],["D","C",70]],"D","C"))
# print(cheapest_flight([["A","B",10],["A","C",15],["B","D",15],["C","D",10]],"A","D"))
# print(cheapest_flight([["A","B",10],["A","C",20],["B","D",15],["C","D",5],["D","E",5],["E","F",10],["C","F",25]],"A","F"))

def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """

    if abs(number) < base and decimals == 0:
        return '{}'.format(number)

    d = [100, 1000, 10 ** 6, 10 ** 9, 10 ** 12, 10 ** 15, 10 ** 18, 10 ** 21, 10 ** 24]
    for x in range(len(d)):
        if abs(number) < base:
            bs = number
            bs2 = 1
            break
        if abs(number) < d[x]:
            if base not in d:
                bs = number // base // base
                bs2 = d[x - 2]
                break
            bs = abs(number) // d[x - 1]
            bs2 = d[x - 1]
            break

    if number < 0:
        bs = '-' + str(bs)

    dec = str(round(number / bs2, decimals)) if decimals != 0 else str(bs)
    dec2 = '0' * (decimals - 1) if number % bs2 == 0 and decimals != 0 else ''
    if powers != ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']:
        pw = powers[1]
    else:
        pw = powers[d.index(bs2)] if bs2 in d else ''
    return dec + dec2 + pw + suffix


# print(friendly_number(255000000000, powers=["","k","M"]))
# print(friendly_number(-150, base=100, powers=["","d","D"]))
# print(friendly_number(1024000000, base=1024, suffix="iB"))
# print(friendly_number(10240))
# print(friendly_number(102, decimals=2))
# print(friendly_number(12000000, decimals=3))
# print(friendly_number(12341234, decimals=1))

def checkio(data):
    n = list(map(int, data.replace('(', '').replace(')', '').split(',')))
    # a = n[] - n[]
    # (2-a)**2 + (2-b)**2 = R**2
    # (6-a)**2 + (2-b)**2 = R**2
    # (2-a)**2 + (6-b)**2 = R**2
    #
    # (2 - a) ** 2 + (2 - b) ** 2 = (6-a)**2 + (2-b)**2
    # 4 - 2a - a**2 + 4 - 2b - b**2 = 12 - 6a - a**2 + 4 - 2b - b**2
    # 8a= 8

    return "(x-{})^2+(y-{})^2={}^2".format(a, b, c)


# print(checkio("(2,2),(6,2),(2,6)")) # == "(x-4)^2+(y-4)^2=2.83^2"
# print(checkio("(3,7),(6,9),(9,7)")) # == "(x-6)^2+(y-5.75)^2=3.25^2"

def checkio(n, nxt=None):
    a, b = 0, 0
    lst = []

    if nxt == None:
        nxt = ''

    for x in range(2, 10):
        if n % x == 0:
            y = n // x
            nxt += str(x)
            if y < 10:
                nxt += str(y)
                lst.append(int(nxt))
                nxt = ''
            else:
                nxt = str(checkio(y, nxt))
                lst.append(int(nxt))
                nxt = ''

    if lst == []:
        return 0
    return min(lst)


# print(checkio(560)) # == 2578
# print(checkio(20)) # == 45
# print(checkio(125)) # == 555
# print(checkio(21)) # == 37
# print(checkio(17)) # == 0
# print(checkio(33)) # == 0)
# print('END')


# Задачка вроде норм, но решать ее долго, поэтому пока оставила
def find_path(m, f, paths, step, me, past):
    w = []
    x = 5
    # while x<4:
    #     try:
    #         if m[f[0][f[1]]] == m[f[0] - 1][f[1]] and past!=m[f[0] - 1][f[1]]:
    #     except IndexError:
    #         break
    # return paths

def can_pass(m, f, s):
    me = m[f[0]][f[1]]
    paths = {1:{}}
    past = False
    x = 0
    while me!=s:
        paths = paths + find_path(m, f, paths, x, me, past)
        if len(paths.get(x))==0:
            del paths[x]
            if len(paths)==0:
                return False
            else:
                x = paths.keys()[0]
                continue
        elif len(paths.get(x))==1:
            past = me
            me = paths.get(x)[0]
            paths = paths + find_path(m, f, paths, x, me, past)
        else:
            past = me
            me = a
            paths = paths + find_path(m, f, paths, x, me, past)




    return True or False

# print(can_pass(((0, 0, 0, 0, 0, 0),
#           (0, 2, 2, 2, 3, 2),
#           (0, 2, 0, 0, 0, 2),
#           (0, 2, 0, 2, 0, 2),
#           (0, 2, 2, 2, 0, 2),
#           (0, 0, 0, 0, 0, 2),
#           (2, 2, 2, 2, 2, 2),),
#          (3, 2), (0, 5))) # == True, 'First example'
# print(can_pass(((0, 0, 0, 0, 0, 0),
#           (0, 2, 2, 2, 3, 2),
#           (0, 2, 0, 0, 0, 2),
#           (0, 2, 0, 2, 0, 2),
#           (0, 2, 2, 2, 0, 2),
#           (0, 0, 0, 0, 0, 2),
#           (2, 2, 2, 2, 2, 2),),
#          (3, 3), (6, 0))) # == False,

def bigger_together(a: List[int]) -> int:
    """
        Returns difference between the largest and smallest values
        that can be obtained by concatenating the integers together.
    """
    a.sort()
    res = []
    for x in range(len(a)):
        if a[x] > 9:
            x1 = map(int, list(str(a[x])))
            z = 0
            for y in res:
                if x1[z] == y:

        else:
            res.append(a[x])

    return res


# print(bigger_together([1, 2, 3, 4]))  # == 3087 # 4321 - 1234
# print(bigger_together([1, 2, 3, 4, 11, 12]))  # == 32099877 # 43212111 - 11112234
# print(bigger_together([0, 1]))  # == 9 # 10 - 01
# print(bigger_together([100]))  # == 0 # 100 - 100


def chase(a1, t2, ad):
    res = ad
    m_t2 = t2*ad
    m_a1 = 0
    while True:
        m_t2 += t2
        m_a1 += a1
        res += 1
        if m_t2==m_a1:
            return round(res, 8)
        elif m_t2>m_a1:
            continue
        else:
            return round((res-1) + t2/a1, 8)

# print(chase(6, 3, 2)) # == 4
# print(chase(10, 1, 10)) # == 11.11111111


# Все правильно работает, но на больших числах стопорится, пока не знаю как это пофиксить
def greatest_common_divisor(*args:int) -> int:
    divs = []
    args = list(args)
    args.sort()
    args = tuple(args)

    for x in args:
        n = args.index(x)
        if n==0:
            divs.append([])
            for y in range(x, 1, -1):
                if x%y==0:
                    divs[-1].append(y)
                    if args[n+1]%y==0:
                        return y
            # divs.append([y for y in range(1, x+1) if x%y==0])
        else:
            divs.append([])
            for y in range(1, x+1):
                if x%y==0 and y in divs[0]:
                    divs[-1].append(y)
                elif x%y==0 and y not in divs[0] and y>max(divs[0]):
                    break
    print(divs)
    if len(divs)==2:
        res = [z for z in divs[0] if z in divs[1]]
        return max(res)

    res = sorted(divs, key=len)[0]
    if len(res)==1:
        return 1

    for x in divs:
        res = [z for z in x if z in res]
    return max(res)

# print(greatest_common_divisor(4294967296,1610612736))
# print(greatest_common_divisor(180,300,450)) # == 30
# print(greatest_common_divisor(6,10,15)) # == 1
# print(greatest_common_divisor(42949, 67296, 2)) # == 1
# print(greatest_common_divisor(6, 4)) # == 2
# print(greatest_common_divisor(2, 4, 8)) # == 2
# print(greatest_common_divisor(2, 3, 5, 7, 11)) # == 1
# print(greatest_common_divisor(3, 9, 3, 9)) # == 3)
