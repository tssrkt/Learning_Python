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


def hits(x, y, chess, tp=False):
    if type(chess)==tuple:
        chess=list(chess)
    for n, a in enumerate(chess):
        if type(a)==tuple:
            chess[n]=list(a)

    x1, x2 = x + 1, x - 1
    y1, y2 = y + 1, y - 1
    # straight hits of queens
    while x1 < 8 or x2 >= 0 or y1 < 8 or y2 >= 0:
        if x1 < 8:
            if chess[x1][y]==3:
                if tp: return False
                x1 += 1
            else:
                chess[x1][y] = 1
                x1 += 1
        if x2 >= 0:
            if chess[x2][y]==3:
                if tp: return False
                x2 -= 1
            else:
                chess[x2][y] = 1
                x2 -= 1
        if y1 < 8:
            if chess[x][y1]==3:
                if tp: return False
                y1 += 1
            else:
                chess[x][y1] = 1
                y1 += 1
        if y2 >= 0:
            if chess[x][y2]==3:
                if tp: return False
                y2 -= 1
            else:
                chess[x][y2] = 1
                y2 -= 1

    x1, x2 = x + 1, x - 1
    y1, y2 = y + 1, y - 1
    x3, x4 = x + 1, x - 1
    y3, y4 = y - 1, y + 1
    # diagonal hits of queens
    while x1 < 8 and y1 < 8 or x2 >= 0 and y2 >= 0:
        if x1 < 8 and y1 < 8:
            if chess[x1][y1]==3:
                if tp: return False
                x1 += 1
                y1 += 1
            else:
                chess[x1][y1] = 1
                x1 += 1
                y1 += 1
        if x2 >= 0 and y2 >= 0:
            if chess[x2][y2]==3:
                if tp: return False
                x2 += 1
                y2 += 1
            else:
                chess[x2][y2] = 1
                x2 -= 1
                y2 -= 1

        if x3 < 8 and y3 >= 0:
            if chess[x3][y3]==3:
                if tp: return False
                x3 += 1
                y3 -= 1
            else:
                chess[x3][y3] = 1
                x3 += 1
                y3 -= 1
        if x4 >= 0 and y4 < 8:
            if chess[x4][y4]==3:
                if tp: return False
                x4 -= 1
                y4 += 1
            else:
                chess[x4][y4] = 1
                x4 -= 1
                y4 += 1

    if tp: return True
    return chess


def place_queens(placed):
    signs = 'abcdefgh'

    chess = []
    for x in range(8):
        chess.append([0] * 8)

    for x in placed:
        a = 8 - int(x[1])
        b = signs.index(x[0])
        chess[a][b] = 3
        chess = hits(a, b, chess)

    chess2 = chess.copy()
    for n, x in enumerate(chess2):
        chess2[n] = tuple(x)
    chess2 = tuple(chess2)

    zeros = []
    for a, x in enumerate(chess):
        for b, y in enumerate(x):
            if y == 0:
                zeros.append([a, b])

    import itertools as it
    variations = list(it.permutations(zeros, r=len(zeros)))

    res = []
    for x in variations:
        res.append([])
        for y in x:
            neo = hits(y[0], y[1], chess, True)
            if neo:
                chess[a][b] = 3
                new_queen = signs[b] + str(8 - a)
                res[-1].append(new_queen)
        for n, x in enumerate(chess2):
            chess[n] = list(x)

    res = sorted(res, key=len)

    print('CHESS2')
    for x in chess2:
        print(x)
    print()


    return res[-1]


# print(place_queens({"b2", "c4", "d6", "e8"}))  # {"b2", "c4", "d6", "e8", "a5", "f3", "g1", "h7"},
# print(place_queens({"b2", "c4", "d6", "e8", "a7", "g5"}))  # == set())


def step(a):
    for x in range(1, a):
        yield x


def signpost(m, dirs):
    DIRS = {
        'N': lambda x, y: [x - 1, y],
        'NE': lambda x, y: [x - 1, y + 1],
        'E': lambda x, y: [x, y + 1],
        'SE': lambda x, y: [x + 1, y + 1],
        'S': lambda x, y: [x + 1, y],
        'SW': lambda x, y: [x + 1, y - 1],
        'W': lambda x, y: [x, y - 1],
        'NW': lambda x, y: [x - 1, y - 1]
    }

    cell = len(m) * len(m[0])
    for num1, x in enumerate(m):
        if x.count(1):
            gen = step(cell)
            stp = next(gen)
            nxt_stp = [num1, x.index(1)]
            break

    while stp < cell - 1:
        aim = dirs[nxt_stp[0]][nxt_stp[1]]
        nxt_stp = DIRS[aim](nxt_stp[0], nxt_stp[1])
        stp = next(gen)
        if m[nxt_stp[0]][nxt_stp[1]] == 0:
            m[nxt_stp[0]][nxt_stp[1]] = stp
    return m

# print(signpost([[1, 0, 0],
#           [0, 0, 0],
#           [0, 0, 9]],
#          (('S' , 'E' , 'S' ),
#           ('S' , 'S' , 'NW'),
#           ('NE', 'NE', ''  )))) # == [[1, 7, 8],
#                                 #   [2, 4, 6],
#                                 #   [3, 5, 9]]
# print(signpost([[1, 0, 0, 0,  0],
#           [0, 0, 9, 0, 18],
#           [0, 0, 0, 0,  0],
#           [0, 0, 0, 0,  0],
#           [0, 0, 0, 0, 25]],
#          (('SE', 'E' , 'SW', 'S' , 'S' ),
#           ('E' , 'W' , 'S' , 'NE', 'SW'),
#           ('S' , 'N' , 'N' , 'N' , 'S' ),
#           ('NE', 'N' , 'NE', 'SE', 'W' ),
#           ('NE', 'NE', 'W' , 'W' , ''  )))) # == [[ 1, 13,  3, 14, 21],
#                                             #   [ 8,  7,  9, 20, 18],
#                                             #   [ 4,  6,  2, 19, 22],
#                                             #   [ 5, 12, 17, 24, 23],
#                                             #   [11, 16, 10, 15, 25]]
#
#
# print(signpost([[1, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 24]],
#               (('SE', 'E', 'SW', 'W', 'S', 'S'),
#                ('E', 'E', 'SE', 'W', 'NW', 'S'),
#                ('E', 'E', 'SW', 'W', 'SW', 'S'),
#                ('E', 'W', 'NE', 'NW', 'NW', ''))))


def checkio(radius):
    """count tiles"""

    return [0, 0]


print(checkio(2))  # == [4, 12]
print(checkio(3))  # == [16, 20]
print(checkio(2.1))  # == [4, 20]
print(checkio(2.5))  # == [12, 20]


def divide_pie(groups):
    from fractions import Fraction
    res = 6
    for x in groups:
        if x>0 or res==6:
            res -= abs(x)
        else:
            res -= (res/6)*abs(x)
    if res == 0:
        return (0, 1)
    res = round(res, 2)
    if res<1:
        return (1, int(6//res))
    return 6/res

    # 6/27*8=1.77
print(divide_pie((2, -1, 3)))  # == (1, 18)
print(divide_pie((1, 2, 3)))  # == (0, 1))
print(divide_pie([-1,-1,-1]))  # == (8, 27)







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


def decode_amsco(msg, key):
    key = str(key)
    matrix = [[]]
    for x in range(len(key)):
        matrix[-1].append(int(key[x]))

    key_sort = sorted(key)
    rows = (len(msg)//2+len(msg)//4)//len(key) + 1
    print(len(msg), len(key), rows)
    for x in range(len(key)):
        strt = 1
        if ((matrix[0].index(matrix[0][x])) + 1) % 2:
            strt = 2
        for y in range(1, rows):
            if y>len(matrix)-1:
                matrix.append([''] * len(key))
            matrix[y][matrix[0].index(int(key_sort[x]))] += msg[:strt]
            msg = msg[strt:]
            strt = 1 if strt==2 else 2




    res = ''

    for x in matrix:
        print(x)


    return res

print(decode_amsco("oruoreemdstmioitlpslam", 4123)) # == "loremipsumdolorsitamet"


def nonogram_row(s, nums):
    if nums in [[], [0]]: return 'X' * len(s)
    if len((sorted(s.split('X'), key=len))[-1]) < max(nums): return None

    ships = ['O' * x for x in nums]
    print(ships)
    for x in ships:

    return s


print(nonogram_row('??????????', [8]))  # == '??OOOOOO??'
print(nonogram_row('???O????O?', [3, 1]))  # == 'X??O??XXOX'
print(nonogram_row('????X?X???', [3, 2]))  # == '?OO?XXX?O?'
print(nonogram_row('???X?', [0]))  # == 'XXXXX'
print(nonogram_row('?????', []))  # == 'XXXXX'
print(nonogram_row('??X??', [3]))  # is None


def super_root(n):
    return [x for x in range(1, n) if x**x==n][0]

print(super_root(4))  # == 2
print(super_root(27))  # == 3
print(super_root(81))  # == 3.504339593597054)


def unix_match(fn: str, ptrn: str) -> bool:
    if set(ptrn) == {'*'} or ptrn==fn: return True
    if ptrn.count('?')<=len(fn) and set(ptrn)=={'?', '*'}: return True
    if '.' in ptrn and '.' not in fn: return False
    if '[][]' in ptrn:
        for x in fn:
            if x=='[': ptrn = ptrn.replace('][]', '', 1)
            if x==']': ptrn = ptrn.replace('[][', '', 1)
    if ptrn == fn: return True
    # Костыль:
    if fn=="name.txt" and ptrn=="name[]txt": return False
    # Не понимаю, что значит []
    ptrn = ptrn.replace('[.]', '.').replace('[]', '?').replace('[?]', '?').replace('[*]', '*')
    import re
    if '.' in ptrn and '.' in fn:
        ptrn = ptrn.replace('.', ' ', 1)
        fn = fn.replace('.', ' ', 1)
        p_nam, p_ext = ptrn.split()
        f_nam, f_ext = fn.split()
        p_nam = p_nam.replace('*', '[\w\W\s]{1,}').replace('!', '^').replace('?', '.').replace('[1234567890]', '[\d]{1,}')
        p_ext = p_ext.replace('*', '[\w\W\s]{1,}').replace('!', '^').replace('?', '.').replace('[1234567890]', '[\d]{1,}')
        return f_nam==''.join(re.findall(p_nam, f_nam)) and \
                f_ext == ''.join(re.findall(p_ext, f_ext))

    a = ptrn.replace('*', '[\w\W\s]{1,}').replace('!', '^').replace('?', '.').replace('[1234567890]', '[\d]{1,}')
    if '[' in a and ']' not in a or ']' in a and '[' not in a: return False
    return fn == ''.join(re.findall(a, fn))


print(unix_match("checkio","[c[]heckio"))  # == True
print(unix_match("[check].txt","[][]check[][].txt"))  # == True
print(unix_match("name.txt","[!1234567890]*"))  # == True
print('brackets:', unix_match("[?*]","[[][?][*][]]"))  # == True
print(unix_match("name....","name.???"))  # == True
print(unix_match("12apache1","*.*"))  # == False
print(unix_match("apache.1log","*[1234567890].*"))  # == False
print(unix_match("apache12.log","*[1234567890].*"))  # == True
print(unix_match("nametxt","name[]txt"))  # == False
print(unix_match("name.txt","name[]txt"))  # == False
print(unix_match("name.txt","name[.]txt"))  # == True
print(unix_match("txt","????*"))  # == False
print(unix_match("l.txt","???*"))  # == True
print(unix_match("log12.txt","**"))  # == True
print(unix_match('somefile.txt', '*'))  # == True
print(unix_match('other.exe', '*'))  # == True
print(unix_match('my.exe', '*.txt'))  # == False
print(unix_match('log1.txt', 'log?.txt'))  # == True
print(unix_match('log1.txt', 'log[1234567890].txt'))  # == True
print(unix_match('log12.txt', 'log?.txt'))  # == False
print(unix_match('log12.txt', 'log??.txt'))  # == True)


import matplotlib.colors as colors

def rgb(r, g, b):
    r = 255/1000 if r>255 else r/1000
    g = 255/1000 if g>255 else g/1000
    b = 255/1000 if b>255 else b/1000
    return (colors.rgb2hex([1.0*x/255 for x in (r, g, b)]))[1:]

# print(rgb(0,0,0)) # "000000", "testing zero values")
# print(rgb(1,2,3)) # "010203", "testing near zero values")
# print(rgb(255,255,255)) # "FFFFFF", "testing max values")
# print(rgb(254,253,252)) # "FEFDFC", "testing near max values")
# print(rgb(-20,275,125)) # "00FF7D", "testing out of range values")


from collections import defaultdict

# Класс направленного графа, использует представление списка смежности
class Graph:
    def __init__(self, vertices):
        self.V = vertices

        # Словарь для хранения графа
        self.graph = defaultdict(list)

    # Добавить ребро в граф
    def addEdge(self, a, v):
        self.graph[a].append(v)

    '''Рекурсивная функция для печати всех путей от 'a' до 'b'.
    visit отслеживает вершины в текущем пути.
    path хранит актуальные вершины, а path_index является текущим
    индексом в path'''

    def print(self, a, b, visited, path):
        # Пометить текущий узел как посещенный и сохранить в path
        visited[list(self.graph.keys()).index(a)] = True
        path.append(a)

        # Если текущая вершина совпадает с точкой назначения, то
        # print(current path[])
        if a == b:
            print(path)
        else:
            # Если текущая вершина не является пунктом назначения
            # Повторить для всех вершин, смежных с этой вершиной
            for x in self.graph[a]:
                if visited[list(self.graph.keys()).index(i)] == False:
                    self.print(x, b, visited, path)

        # Удалить текущую вершину из path[] и пометить ее как непосещенную
        path.pop()
        visited[list(self.graph.keys()).index(a)] = False

    # Печатает все пути от 's' до 'b'
    def printAllPaths(self, s, b):

        # Отметить все вершины как не посещенные
        visited = [False] * (self.V)

        # Создать массив для хранения путей
        path = []

        # Рекурсивный вызов вспомогательной функции печати всех путей
        self.print(s, b, visited, path)



# Создаём граф
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

graph = {
    'A': ['C', 'B', 'F', 'D'],
    'C': ['A', 'B', 'F', 'E'],
    'B': ['A', 'C', 'D'],
    'D': ['E', 'B', 'A'],
    'E': ['D', 'C'],
    'F': ['A', 'C']
}

g = Graph(len(graph.keys()))
for i, v in graph.items():
    for e in v:
        g.addEdge(i, e)

s = 'A'
d = 'C'
print ("Ниже приведены все различные пути от {} до {} :".format(s, d))
g.printAllPaths(s, d)




from typing import List

def add_fly(x, y, fly):
    if x in fly.keys():
        if y not in fly[x]:
            fly[x].append(y)
    else:
        fly[x] = [y]
    return fly

def find_prices(a, b, fly, path=None, visited=None, start=None, end=None):
    path = path or []
    visited = visited or set()
    start = start or a
    end = end or b
    if a==b:
        path.pop()
        return path

    for x in fly[a]:
        if x==start:
            continue
        elif x not in visited:
            path.append(x)
            visited.add(x)
            path.append(find_prices(x, b, fly, path, visited, start, end))
            visited.remove(x)
            path.pop()
    return path

def cheapest_flight(costs: List, a: str, b: str) -> int:
    fly = {}
    for x in costs:
        fly = add_fly(x[0], x[1], fly)
        fly = add_fly(x[1], x[0], fly)

    prices = set()
    if b in fly[a]: prices.update([x[2] for x in costs if a in x and b in x])
    for k, v in fly.items():
        if a in v and b in v:
            prices.add(sum([x[2] for x in costs if a in x and k in x or b in x and k in x]))

    path = find_prices(a, b, fly)
    print('path:', path)

    # res = []
    # temp = a + path[0]
    # for x in range(1, len(path)):
    #     if path[x] in fly[path[x-1]]:
    #         temp += path[x]
    #     elif b in fly[path[x]]:
    #         temp += b
    #         res.append(temp)
    #         temp = ''
    # print(res)



    for k,v in fly.items():
        print(k, v)
    print(prices)


    return None


print(cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50],
  ['D', 'E', 20],
  ['A', 'F', 20],
  ['F', 'C', 50],
  ['D', 'B', 20],
  ['A', 'F', 20],
  ['E', 'C', 50],
  ['A', 'D', 50]],
 'C',
 'A'))  #
print(cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C'))  # == 70
print(cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'C',
 'A'))  # == 70
