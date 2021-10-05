def delete_zero(grp):
    """Удаляем ноли из списка"""
    import itertools as it
    res = list(it.filterfalse(lambda x: x == 0, grp))
    return res


def merge_intervals(a):
    """
        Merge overlapped intervals.
    """
    for x in range(len(a)):
        a[x] = [a[x][0], a[x][-1]]

    for x in range(len(a) - 1):
        for y in range(x + 1, len(a)):
            if a[x] != 0 and a[y] != 0:
                if a[x][-1] >= a[y][0] or a[x][-1] == a[y][0] + 1 or a[x][-1] == a[y][0] - 1:
                    if a[x][-1] >= a[y][-1]:
                        a[y] = 0
                        continue
                    a[x][-1] = a[y][-1]
                    a[y] = 0
                    continue
    a = delete_zero(a)

    for x in range(len(a)):
        a[x] = (a[x][0], a[x][-1])

    return a


# print(merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)])) # == [(1, 6), (8, 10), (12, 19)]
# print(merge_intervals([(1, 12), (2, 3), (4, 7)])) # == [(1, 12)]
# print(merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)])) # == [(1, 15), (17, 20)]


from typing import Iterable


def expand_intervals(a: Iterable) -> Iterable:
    res = []
    for x in range(len(a)):
        res.append(a[x][0])
        if a[x][0] + 1 < a[x][-1]:
            for y in range(a[x][0] + 1, a[x][-1]):
                res.append(y)
        res.append(a[x][-1])
    res = set(res)
    res = list(res)
    return res


# print(expand_intervals([[1,2],[4,4]])) # == [1,2,4]
# print(expand_intervals([(1, 3), (5, 7)])) # == [1, 2, 3, 5, 6, 7]
# print(expand_intervals([(1, 3)])) # == [1, 2, 3]


def get_cookie(c, n):
    lst = list(c.split(';'))
    for x in lst:
        if n in x:
            z = x.find('=')
            return x[z + 1:].replace(';', '')


# print(get_cookie("USER=name=Unknown; domain=bbc.com","USER")) # == name=Unknown
# print(get_cookie("ffo=false; domain=google.com; expires=Sunday, 20-May-2018 00:00:00 GMT","expires"))
# # == "Sunday, 20-May-2018 00:00:00 GMT"
# print(get_cookie('theme=light; sessionToken=abc123', 'theme')) # == 'light'
# print(get_cookie('_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo')) # == 'true'


def unix_match(fn: str, ptrn: str) -> bool:
    if set(ptrn) == {'*'} or set(ptrn) == {'*', '?'} and len(ptrn) <= len(fn):
        return True

    if fn.count('.') == 1 and ptrn.count('.') == 1:
        fn = fn.split('.')
        ptrn = ptrn.split('.')
    elif len(fn) == len(ptrn):
        for x in range(len(fn)):
            if ptrn[x] == '?' or ptrn[x] == fn[x]:
                continue
            else:
                return False
        return True
    elif '.*' in ptrn and '.' in fn:
        for x in range(len(fn)):
            if ptrn[x] == '?' or ptrn[x] == fn[x]:
                continue
            elif ptrn[x] == '*':
                return True
            else:
                return False
    if type(fn) == list and len(fn) == len(ptrn):
        if fn[-1] == ptrn[-1] or ptrn[-1] == '*' or set(ptrn[-1]) == {'?'} and len(ptrn[-1]) == len(fn[-1]):
            if ptrn[0] == '*':
                return True
            if '?' in ptrn[0] and len(fn[0]) == len(ptrn[0]):
                for x in range(len(fn[0])):
                    if ptrn[0][x] == '?' or ptrn[0][x] == fn[0][x]:
                        continue
                    else:
                        return False
                return True
            elif ptrn[0] == '*' or fn[0] == ptrn[0]:
                return True
    return False


# print(unix_match("file19.txt","*z*")) # == False
# print(unix_match("name....","name.*")) # == True
# print(unix_match("name....","name.???")) # == True
# print(unix_match("name.txt","name.???")) # == True
# print(unix_match("12apache1","*.*")) # == False
# print(unix_match("apache1.log","*.*")) # == True
# print(unix_match("txt","????*")) # == False
# print(unix_match("l.txt","???*")) # == True
# print(unix_match("log12.txt","**")) # == True
# print(unix_match('somefile.txt', '*')) # == True
# print(unix_match('other.exe', '*')) # == True
# print(unix_match('my.exe', '*.txt')) # == False
# print(unix_match('log1.txt', 'log?.txt')) # == True
# print(unix_match('log12.txt', 'log?.txt')) # == False
# print(unix_match('log12.txt', 'log??.txt')) # == True

def ptrn_check(ptrn, fn, x):
    a = ''
    positive = True
    for y in range(x + 1, len(ptrn)):
        if ptrn[y] == '!':
            positive = False
        elif ptrn[y] == '[':
            continue
        elif ptrn[y] == ']':
            break
        else:
            a += ptrn[y]
    if positive == True and fn[x] in a or positive == False and fn[x] not in a:
        return True
    return False


def unix_match(fn: str, ptrn: str) -> bool:
    if fn == ptrn:
        return True
    after = False
    new_ptrn = ''
    for x in range(len(fn)):
        if ptrn[x] == fn[x] and after == False:
            continue
        elif ptrn[x] == '[' and after == False:
            new_ptrn = ptrn[:ptrn.index('[')] + fn[x] + ptrn[ptrn.index(']') + 1:]
            after = True
            if ptrn_check(ptrn, fn, x):
                continue
            else:
                return False
        elif after == True:
            if '[' not in new_ptrn and ']' not in new_ptrn and new_ptrn == fn:
                return True
            elif '[' not in new_ptrn and ']' not in new_ptrn and new_ptrn != fn:
                return False
            elif '[' in new_ptrn and ']' in new_ptrn and new_ptrn[x] == fn[x]:
                continue
            elif new_ptrn[x] == '[':
                if ptrn_check(new_ptrn, fn, x):
                    new_ptrn = new_ptrn[:new_ptrn.index('[')] + fn[x] + new_ptrn[new_ptrn.index(']') + 1:]
                    continue
                else:
                    return False
        else:
            return False
    return True


# print(unix_match("check.txt","[[c]heck.txt")) # == True
# print(unix_match("name.txt","[!abc]name.txt")) # == False
# print(unix_match("name.exe","name.[!.][!.][!.]")) # == True
# print(unix_match('somefile.txt', 'somefile.txt')) # == True
# print(unix_match('1name.txt', '[!abc]name.txt')) # == True
# print(unix_match('log1.txt', 'log[1234567890].txt')) # == True

def flatten(lst):
    lst2 = []
    for x in lst:
        if type(x) == list:
            lst2.extend(x)
        else:
            lst2.append(x)
    return lst2


def get_key(d, value):
    for k, v in d.items():
        if value in v:
            return k


def is_family(tree: list[list[str]]) -> bool:
    if len(tree) == 1:
        return True
    d = {}
    for x in range(len(tree)):
        person = tree[x][0]
        son = tree[x][1]
        if person == son:
            return False
        if d == {}:
            d.setdefault(person, [son])
        else:
            if person in d.keys():
                d[person].append(son)
            elif person in flatten(d.values()):
                grandpa = get_key(d, person)
                if son == grandpa or son in flatten(d.values()):
                    return False
                else:
                    d.setdefault(person, [son])
            else:
                d.setdefault(person, [son])

    f = list(d.keys())
    s = flatten(d.values())
    for x in range(1, len(f)):
        if f[x] not in s:
            for y in d.get(f[x]):
                if y not in f:
                    return False
    # print(d)
    return True


# print(is_family([["Logan","William"],["Logan","Jack"],["Mike","Mike"]])) # == False
# print(is_family([["Logan","Mike"],
#                  ["Alexander","Jack"],
#                  ["Jack","Logan"]])) # == True
# print(is_family([
#   ['Logan', 'Mike'],
#   ['Logan', 'Jack'],
#   ['Mike', 'Logan']
# ])) # == False  # Можешь ли ты быть отцом своего отца?
# print(is_family([
#   ['Logan', 'William'],
#   ['Logan', 'Jack'],
#   ['Mike', 'Alexander']
# ])) # == False  # По всей видимости, Майк является посторонним в семье Логана
# print(is_family([
#   ['Logan', 'Mike']
# ])) # == True
# print(is_family([
#   ['Logan', 'Mike'],
#   ['Logan', 'Jack']
# ])) # == True
# print(is_family([
#   ['Logan', 'Mike'],
#   ['Logan', 'Jack'],
#   ['Mike', 'Alexander']
# ])) # == True
# print(is_family([
#   ['Logan', 'Mike'],
#   ['Logan', 'Jack'],
#   ['Mike', 'Jack']
# ])) # == False  # Можешь ли ты быть отцом своего брата?


def cut_sentence(s: str, n: int) -> str:
    '''
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    '''
    if n >= len(s):
        return s

    a = s.split()
    res = a[0]
    for x in range(1, len(a)):
        if len(res) > n:
            return '...'
        elif len(res + ' ' + a[x]) <= n:
            res += ' ' + a[x]
        else:
            res += '...'
            break
    return res


# print(cut_sentence("Hi my name is Alex",1)) # == "..."
# print(cut_sentence("Hi my name is Alex", 4)) # == "Hi..."
# print(cut_sentence("Hi my name is Alex", 8)) # == "Hi my..."
# print(cut_sentence("Hi my name is Alex", 18)) # == "Hi my name is Alex"
# print(cut_sentence("Hi my name is Alex", 20)) # == "Hi my name is Alex"


def best_stock(d: dict) -> str:
    price = max(list(d.values()))
    for k, v in d.items():
        if price == v:
            return k


# print(best_stock({
#     'CAC': 10.0,
#     'ATX': 390.2,
#     'WIG': 1.2
# })) # == 'ATX'
# print(best_stock({
#     'CAC': 91.1,
#     'ATX': 1.01,
#     'TASI': 120.9
# })) # == 'TASI')


def checkio(n: int) -> int:
    return bin(n).count('1')


# print(checkio(4)) # == 1
# print(checkio(15)) # == 4
# print(checkio(1)) # == 1
# print(checkio(1022)) # == 9


def to_decrypt(ct, n):
    import string as s
    alpha = s.ascii_lowercase
    res = ''
    for x in ct:
        if x.isalpha():
            z = alpha.index(x)
            try:
                res += alpha[z + n]
            except IndexError:
                z = n - (len(alpha) - (z))
                res += alpha[z]
        elif x.isspace():
            res += ' '
    return res


# print(to_decrypt("!d! [e] &f*", -3)) # == "a b c"
# print(to_decrypt("x^$# y&*( (z):-)", 3)) # == "a b c"
# print(to_decrypt("iycfbu!@# junj%&", -16)) # == "simple text"
# print(to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10)) # == "important text"
# print(to_decrypt("fgngr **&&frperg^__^", 13)) # == "state secret")


def to_encrypt(txt, n):
    import string as s
    alpha = s.ascii_lowercase
    res = ''
    for x in txt:
        if x.isalpha():
            z = alpha.index(x)
            try:
                res += alpha[z + n]
            except IndexError:
                z = n - (len(alpha) - (z))
                res += alpha[z]
        else:
            res += ' '
    return res


# print(to_encrypt("a b c", 3)) # == "d e f"
# print(to_encrypt("a b c", -3)) # == "x y z"
# print(to_encrypt("simple text", 16)) # == "iycfbu junj"
# print(to_encrypt("important text", 10)) # == "swzybdkxd dohd"
# print(to_encrypt("state secret", -13)) # == "fgngr frperg")


def count_neighbours(g, row, col):
    NBRS = {
        1: lambda x, y: [x - 1, y - 1],  # left upper square
        2: lambda x, y: [x - 1, y],
        3: lambda x, y: [x - 1, y + 1],
        4: lambda x, y: [x, y + 1],
        5: lambda x, y: [x + 1, y + 1],
        6: lambda x, y: [x + 1, y],
        7: lambda x, y: [x + 1, y - 1],
        8: lambda x, y: [x, y - 1]
    }

    res = 0
    for x in range(1, 9):
        a, b = NBRS[x](row, col)
        if len(g) > a >= 0 and len(g[0]) > b >= 0:
            res = res + 1 if g[a][b] == 1 else res
    return res


# print(count_neighbours([[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0]],5,4))
# print(count_neighbours([[1,1,1],[1,1,1],[1,1,1]],0,2)) # == 3
# print(count_neighbours(((1, 0, 0, 1, 0),
#                   (0, 1, 0, 0, 0),
#                   (0, 0, 1, 0, 1),
#                   (1, 0, 0, 0, 0),
#                   (0, 0, 1, 0, 0),), 1, 2)) # == 3
# print(count_neighbours(((1, 0, 0, 1, 0),
#                   (0, 1, 0, 0, 0),
#                   (0, 0, 1, 0, 1),
#                   (1, 0, 0, 0, 0),
#                   (0, 0, 1, 0, 0),), 0, 0)) # == 1)


def koma(s):
    if ',' not in s:
        if s.count('.') > 1:
            return s.replace('.', ',')
        else:
            z = s.split('.')[-1]
            z = ''.join(i for i in z if i.isdigit())
            if z.isdigit() and int(z) == 0:
                return s.replace('.', ',')
            return s
    if '.' not in s:
        if s.count(',') == 1:
            return s.replace(',', '.')
        if s.count(',') > 1:
            return s
    s = s.replace(',', '.')
    n = s.count('.') - 1
    return s.replace('.', ',', n)


def checkio(s: str) -> str:
    res = ''
    dt = False
    if '$' not in s:
        return s
    if s[-1] == '.':
        dt = True
        s = s[:-1]
    if s.count('$') > 1:
        s = s.split('$')
        if '' in s:
            del s[s.index('')]
        for x in s:
            if x[0].isalpha():
                res += koma(x)
            else:
                res += '$' + koma(x)
    else:
        res = koma(s)
    if dt == True:
        res += '.'
    return res


# print(checkio("Clayton Kershaw $31.000.000\nZack Greinke   $27.000.000\nAdrian Gonzalez $21.857.143\n"))
# print('RIGHT:', "Clayton Kershaw $31,000,000\nZack Greinke   $27,000,000\nAdrian Gonzalez $21,857,143\n")
# print(checkio("127.255.255.255")) # == "127.255.255.255"
# print(checkio("Our movie tickets cost $12,20.")) # == "Our movie tickets cost $12.20."
# print(checkio("$4.545,45 is less than $5,454.54.")) # == "$4,545.45 is less than $5,454.54."
# print(checkio("$8.000 - $8.000 = $0")) # == "$8,000 - $8,000 = $0"
# print(checkio("$4,13 + $1.005,24 = $1.009,37")) # == "$4.13 + $1,005.24 = $1,009.37"
# print(checkio("$4,13 + $5,24 = $9,37")) # == "$4.13 + $5.24 = $9.37"
# print(checkio("$222.100.455")) # == "$222,100,455"
# print(checkio('$5.34')) # == '$5.34'
# print(checkio('$5,34')) # == '$5.34'
# print(checkio('$222,100,455.34')) # == '$222,100,455.34'
# print(checkio('$222.100.455,34')) # == '$222,100,455.34'
# print(checkio('$222,100,455')) # == '$222,100,455')

all = {
    'color': ['blue', 'green', 'red', 'white', 'yellow'],
    'pet': ['cat', 'bird', 'dog', 'fish', 'horse'],
    'drink': ['beer', 'coffee', 'milk', 'tea', 'water'],
    'ciga': ['Rothmans', 'Dunhill', 'Pall Mall', 'Winfield', 'Marlboro'],
    'man': ['Brit', 'Dane', 'German', 'Norwegian', 'Swede']}

QUESTIONS = {"color": 'color', "nationality": 'man', "beverage": 'drink', "cigarettes": 'ciga', "pet": 'pet'}


# for all
def gt(item, slovar):
    for k, v in slovar.items():
        if item in v:
            return k


# for pancha
def gt2(item, slovar):
    for k, v in slovar.items():
        if item in list(v.values()):
            return k


def lopata(rels, pancha):
    new_rels = []
    for a in rels:
        x = a.split('-')
        if gt2(x[0], pancha) != None and x[1].isalpha():
            pancha[gt2(x[0], pancha)][gt(x[1], all)] = x[1]
        elif gt2(x[1], pancha) != None and x[0].isalpha():
            pancha[gt2(x[1], pancha)][gt(x[0], all)] = x[0]
        else:
            new_rels.append(a)
    return pancha, new_rels


def bandura(pancha):
    for key in all.keys():
        spisok = []
        for k, v in pancha.items():
            spisok.append(v[key])
        spisok = list(filter(lambda x: x != '', spisok))
        if len(spisok) == 4:
            item = list(filter(lambda x: x not in spisok, all[key]))[0]
            for k, v in pancha.items():
                if v[key] == '':
                    v[key] = item
    return pancha


def answer(rels, q):
    pancha = {k: {'man': '', 'drink': '', 'pet': '', 'ciga': '', 'color': ''} for k in range(1, 6)}
    new_rels = []

    # Numbers of houses
    for a in rels:
        x = a.split('-')
        if x[0].isdigit():
            pancha[int(x[0])][gt(x[1], all)] = x[1]
        elif x[1].isdigit():
            pancha[int(x[1])][gt(x[0], all)] = x[0]
        else:
            new_rels.append(a)

    # Filling pancha
    while len(new_rels) > 0:
        pancha, new_rels = lopata(new_rels, pancha)
        pancha = bandura(pancha)

    # Answering on the question
    q = q.split('-')
    if q[1] == 'number':
        return str(gt2(q[0], pancha))
    return pancha[gt2(q[0], pancha)][QUESTIONS[q[1]]]

    # print(new_rels)
    # for k,v in pancha.items():
    #     print(k, v)


# print(answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
#                    'German-coffee', 'beer-white', 'cat-water',
#                    'horse-2', 'milk-3', '4-Rothmans',
#                    'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
#                    'bird-Brit', '4-green', 'Winfield-beer',
#                    'Dane-blue', '5-dog', 'blue-horse',
#                    'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
#                   'fish-color')) # == 'green'  # What is the color of the house where the Fish lives?
# print(answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
#                    'German-coffee', 'beer-white', 'cat-water',
#                    'horse-2', 'milk-3', '4-Rothmans',
#                    'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
#                    'bird-Brit', '4-green', 'Winfield-beer',
#                    'Dane-blue', '5-dog', 'blue-horse',
#                    'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
#                   'tea-number')) # == '2'  # What is the number of the house where tea is favorite beverage?
# print(answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
#                    'German-coffee', 'beer-white', 'cat-water',
#                    'horse-2', 'milk-3', '4-Rothmans',
#                    'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
#                    'bird-Brit', '4-green', 'Winfield-beer',
#                    'Dane-blue', '5-dog', 'blue-horse',
#                    'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
#                   'Norwegian-beverage')) # == 'water'  # What is the favorite beverage of the Norwegian man?


def longest_palindromic(a):
    if len(set(a)) == 1:
        return a
    res = [a[0]]
    palin = ''
    for x in range(1, len(a) - 1):
        for y in range(x + 1, len(a)):
            z = x - (y - x)
            if z >= 0 and a[y] == a[z]:
                palin = a[x] if palin == '' else palin
                palin = a[y] + palin + a[z]
                continue
            else:
                if palin != '':
                    res.append(palin)
                    palin = ''
                break
    res.sort(key=len, reverse=True)
    return res[0]


# print(longest_palindromic("123abcba")) # == "abcba"
# print(longest_palindromic("aaaaa")) # == "aaaaa"
# print(longest_palindromic('abc')) # == 'a'
# print(longest_palindromic('abacada')) # == 'aba'

# ALPHA (%41–%5A and %61–%7A), DIGIT (%30–%39)


def checkio(url):
    import string as s
    SIGNS = {'%2D': '-', '%2E': '.', '%5F': '_', '%7E': '~'}
    ALPHA = s.ascii_lowercase
    nums = ['4', '5', '6', '7']

    url = url.lower()
    if ':80/' in url or ':80' in url and url.rfind('0') == len(url) - 1:
        url = url.replace(':80', '')
    if '/./' in url and '../' not in url:
        url = url.replace('./', '')
    new_url = url
    if '%' in url:
        x = url.find('%')
        new_url = url[:x]
        while x < len(url):
            if url[x] == '%':
                a = url[x:x + 3].upper()
                if a in SIGNS:
                    new_url += SIGNS.get(a)
                    x += 3
                elif url[x + 1] == '3' and url[x + 2].isdigit():
                    new_url += url[x + 2]
                    x += 3
                elif url[x + 1] in nums:
                    if url[x + 1] == '4':
                        if url[x + 2].isdigit():
                            new_url += ALPHA[int(url[x + 2]) - 1]
                        x += 3
                    elif url[x + 1] == '5':
                        new_url += ALPHA[ALPHA.index(url[x + 2]) + 18]
                        x += 3
                    elif url[x + 1] == '6':
                        new_url += ALPHA[ALPHA.index(url[x + 2]) + 9]
                        x += 3
                    elif url[x + 1] == '7':
                        new_url += ALPHA[int(url[x + 2]) + 15]
                        x += 3
                else:
                    new_url += a.upper()
                    x += 3
            else:
                new_url += url[x]
                x += 1

    y = 0
    while '../' in new_url or '/..' in new_url:
        x = new_url.find('.', y)
        if x + 2 < len(new_url):
            if new_url[x + 1] == '.' and new_url[x + 2] == '/':
                n = new_url[:x - 1].rfind('/')
                repl = new_url[n + 1:x + 3]
                new_url = new_url.replace(repl, '', 1)
            else:
                y = x + 1
        else:
            if new_url[x + 1] == '.':
                n = new_url[:x - 1].rfind('/')
                repl = new_url[n + 1:]
                new_url = new_url.replace(repl, '', 1)
                if new_url[-1] == '/':
                    new_url = new_url[:-1]
            else:
                y = x + 1

    while './' in new_url:
        new_url = new_url.replace('./', '', 1)
    return new_url


# print(checkio("http://Www.Checkio.org:80/ta%73K%2d/1/../2/./%3f%3e")) # == "http://www.checkio.org/task-/2/%3F%3E"
# print(checkio("http://example.com/a/b/c/d/../../")) # == "http://example.com/a/b/"
# print(checkio("http://example.com:80/HOME/../././Guest/1/../2/..")) # == "http://example.com/guest"
# print(checkio("http://example.com/%31%30%2D%2f%2E%1f%5F%7E")) # == "http://example.com/10-%2F.%1F_~"
# print(checkio("http://Example.com:80/%48%6f%6d%45")) # == "http://example.com/home"
# print(checkio("HTTP://EXAMPLE.COM:80")) # == "http://example.com"
# print(checkio("Http://Www.Checkio.org")) # == "http://www.checkio.org"
# print(checkio("http://www.checkio.org/%cc%b1bac")) # == "http://www.checkio.org/%CC%B1bac"
# print(checkio("http://www.checkio.org/task%5F%31")) # == "http://www.checkio.org/task_1"
# print(checkio("http://www.checkio.org:80/home/")) # == "http://www.checkio.org/home/"
# print(checkio("http://www.checkio.org:8080/home/")) # == "http://www.checkio.org:8080/home/"
# print(checkio("http://www.checkio.org/task/./1/../2/././name")) # == "http://www.checkio.org/task/2/name"


def nearest_square(n):
    for x in range(n - 1, 0, -1):
        if not (x ** 0.5) % 1:
            low = x
            break

    for x in range(n + 1, 1000001):
        if not (x ** 0.5) % 1:
            up = x
            break

    res = low if (n - low) < (up - n) else up
    return res


########################################################################################

fibochka = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]


def checkio(opacity):
    sq = [x if x in fibochka else -1 for x in range(1, 10001)]
    yo = 10000 - opacity
    for x, y in enumerate(sq, start=0):
        if sum(sq[:x + 1]) == yo:
            return x + 1


# print(checkio(9999)) # == 1
# print(checkio(9994)) # == 3
# print(checkio(9995)) # == 4

def name_spell(name, spell):
    for letter in name:
        if letter in spell:
            spell = spell.replace(letter, '', 1)
        else:
            return False
    spell = '1' if spell == '' else spell
    return spell


def monsters(spell: str, MONSTERS) -> int:
    names = []
    for name in MONSTERS:
        inside = name_spell(name, spell)
        if inside:
            spell = inside
            names.append(name)
            while inside:
                inside = name_spell(name, spell)
                if inside:
                    spell = inside
                    names.append(name)
    return len(names)


import itertools as it


def halloween_monsters(spell: str):
    MONSTERS = ['jack', 'ghost', 'witch', 'mummy', 'zombie', 'vampire', 'skeleton', 'werewolf', 'frankenstein']
    variations = list(it.permutations(MONSTERS, r=len(MONSTERS)))
    res = []
    for variant in variations:
        res.append(monsters(spell, variant))
    return max(res)


# print(halloween_monsters("sqcnxsqhtrxmhoslaykktvocxmjkwmuzewulwuotncvgebbqvdbyjpzirzmscporjklfiefzuaiynpyljdqbdpwighggfdv"))
# print(halloween_monsters("kenoistcepajmlvre")) # == 2
# print(halloween_monsters("llzmfrhlthfqpnnkgvtzvgknsewejisuspfqzbbmmsfxdnxcvpikyytqqcraiomrbvxdjeyjxolorezwao")) # == 7
# print(halloween_monsters('finhtiistchwwaerecnnkt'))  # == 3  # witch, witch, frankenstein)
# print(halloween_monsters("miaimavrurymepepv")) # == 2
# print(halloween_monsters('tkjagchso'))  # == 2               # jack, ghost


def checkio(ptrn, image):
    rows = len(ptrn)
    cols = len(ptrn[0])
    for x in range(len(image) - len(ptrn) + 1):
        for y in range(len(image[0]) - len(ptrn[0]) + 1):
            pikcha = True
            for x1, row in enumerate(image[x:x + rows], start=0):
                if pikcha == False:
                    break
                for y1, col in enumerate(row[y:y + cols], start=0):
                    if col != ptrn[x1][y1]:
                        pikcha = False
                        break
            if pikcha == True:
                for x1, row in enumerate(image[x:x + rows], start=x):
                    for y1, col in enumerate(row[y:y + cols], start=y):
                        image[x1][y1] = image[x1][y1] + 2
    return image


# print(checkio([[0,0,0],[0,0,0],[0,0,0]],[[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1,0,0]]))
# print(checkio([[1, 0], [1, 1]],
#         [[0, 1, 0, 1, 0],
#          [0, 1, 1, 0, 0],
#          [1, 0, 1, 1, 0],
#          [1, 1, 0, 1, 1],
#          [0, 1, 1, 0, 0]])) # == [[0, 3, 2, 1, 0],
#                             #  [0, 3, 3, 0, 0],
#                             #  [3, 2, 1, 3, 2],
#                             #  [3, 3, 0, 3, 3],
#                             #  [0, 1, 1, 0, 0]]
# print(checkio([[1, 1], [1, 1]],
#         [[1, 1, 1],
#          [1, 1, 1],
#          [1, 1, 1]])) # == [[3, 3, 1],
#                       #    [3, 3, 1],
#                       #    [1, 1, 1]])


def encode(msg, sa, kw):
    msg = msg.lower().replace(' ', '')
    ptrn = 'ADFGVX'
    sa_matrix = {'A': '', 'D': '', 'F': '', 'G': '', 'V': '', 'X': ''}
    num = 0

    # Create matrix of secret alphabet
    for x in range(6):
        for y in range(6):
            sa_matrix[ptrn[x]] += sa[num]
            num += 1

    # Create table of upper letters
    shifr = ''
    for x in msg:
        for k, v in sa_matrix.items():
            if x in v:
                shifr += k + ptrn[v.index(x)]

    # Clean keyword from repeating letters
    kw2 = ''
    for x in kw:
        if x not in kw2:
            kw2 += x
    kw = kw2

    # Create new matrix by keyword
    kw_matrix = []
    kw_matrix.append(kw)
    while len(shifr) > 0:
        kw_matrix.append('')
        for x in range(len(kw)):
            if len(shifr) == 0:
                break
            kw_matrix[-1] += shifr[0]
            shifr = shifr.replace(shifr[0], '', 1)

    # Reorganize matrix by alphabet and keyword
    kw = ''.join(sorted(kw))
    neo_matrix = [''] * len(kw_matrix)
    for s in kw:
        for y in range(len(kw_matrix)):
            try:
                neo_matrix[y] += kw_matrix[y][kw_matrix[0].index(s)]
            except IndexError:
                neo_matrix[y] += ' '

    # Read the neo_matrix by columns
    res = ''
    del neo_matrix[0]
    neo_matrix = list(filter(lambda x: x != '', neo_matrix))

    for x in range(len(neo_matrix[0])):
        for row in neo_matrix:
            if row[x] != ' ':
                res += row[x]
    return res


def decode(msg, sa, kw):
    # Clean keyword from repeating letters
    kw2 = ''
    for x in kw:
        if x not in kw2:
            kw2 += x
    kw = kw2
    kw2 = ''.join(sorted(kw))

    if len(msg) % len(kw):
        rows = len(msg) // len(kw) + 1
        spaces = kw[(len(msg) % len(kw)):]
    else:
        rows = len(msg) // len(kw)
        spaces = ''

    # Create keyword matrix
    kw_matrix = [''] * rows
    for s in kw2:
        if s not in spaces:
            for y in range(rows):
                kw_matrix[y] += msg[0]
                msg = msg[1:]
        else:
            for y in range(rows - 1):
                kw_matrix[y] += msg[0]
                msg = msg[1:]
            kw_matrix[y + 1] += ' '

    # Create neo_matrix by keyword
    neo_matrix = []
    for x in kw:
        for y in range(rows):
            if y > len(neo_matrix) - 1:
                neo_matrix.append([])
            neo_matrix[y].append(kw_matrix[y][kw2.index(x)])

    # Create string of upper letters
    shifr = ''
    for x in range(rows):
        for s in neo_matrix[x]:
            if s != ' ':
                shifr += s

    # Create matrix of secret alphabet
    ptrn = 'ADFGVX'
    sa_matrix = {'A': '', 'D': '', 'F': '', 'G': '', 'V': '', 'X': ''}
    num = 0
    for x in range(6):
        for y in range(6):
            sa_matrix[ptrn[x]] += sa[num]
            num += 1

    # Decode using matrix of secret alphabet
    res = ''
    for x in range(0, len(shifr), 2):
        res += sa_matrix.get(shifr[x])[ptrn.index(shifr[x + 1])]
    return res


# print(encode("I am going", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g", "cipher"))
# print(decode("DXGAXAAXXVDDFGFX", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g", "weasel"))
# print(encode("I am going", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g", "weasel"))
# print(encode('I am going.', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','cipher'))  # == 'FXGAFVXXAXDDDXGA'
# print(decode('FXGAFVXXAXDDDXGA', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','cipher'))  # == 'iamgoing')
# print(encode("One 1, Two 2, Three 3, Four 4, Five 5, Six 6, Seven 7, Eight 8, Nine 9, Zero 0", "d9sr4qxvaz75yu2hkwpm8j63b1legot0ifnc", "monty")) # == 'VGFFAGVGXGXVDVXGXVDGXDVAVXFVDXDFVVVAXGVXXVXXGGXAFDFADDFXVVGVVXXFGXDXDAAVGVVGFAGXVAFGVGAGVFGGXGFFXDAD'


def steps_finder(x, y):
    # All steps of horse
    STEPS = {
        1: lambda x, y: [x - 2, y - 1],
        2: lambda x, y: [x - 2, y + 1],
        3: lambda x, y: [x - 1, y + 2],
        4: lambda x, y: [x + 1, y + 2],
        5: lambda x, y: [x + 2, y + 1],
        6: lambda x, y: [x + 2, y - 1],
        7: lambda x, y: [x + 1, y - 2],
        8: lambda x, y: [x - 1, y - 2]
    }

    res = []
    for num in range(1, 9):
        stp = STEPS[num](x, y)
        if 8 > stp[0] >= 0 and 8 > stp[1] >= 0:
            res.append(stp)
    return res


def chess_knight(start, moves):
    row = 'abcdefgh'
    x, y = (8 - int(list(start)[1])), row.index(list(start)[0])

    steps = []
    prev_move = []
    prev_move.append([x, y])
    while moves > 0:
        next_move = []
        for z in prev_move:
            next_move.extend(steps_finder(z[0], z[1]))
        prev_move = next_move
        steps.extend(prev_move)
        moves -= 1

    res = []
    for x in steps:
        res.append(row[x[1]] + str(8 - int(x[0])))

    res = list(set(res))
    res = sorted(res, key=lambda x: int(x[1]))
    return sorted(res)


# print(chess_knight('h8', 2)) # == ['d6', 'd8', 'e5', 'e7', 'f4', 'f7', 'f8', 'g5', 'g6', 'h4', 'h6', 'h8'])
# print(chess_knight('a1', 1)) # == ['b3', 'c2']


def sum_consecutives(a):
    res = []
    same = []
    for x, n in enumerate(a):
        if x < len(a) - 1 and n == a[x + 1]:
            same.append(n)
        else:
            if same == []:
                res.append(n)
            else:
                same.append(n)
                res.append(sum(same))
                same = []
    if same != []:
        res.append(sum(same))
    return res


# print(sum_consecutives([1,1,2,1])) # == [2,2,1]
# print(sum_consecutives([1, 1, 1, 1])) # == [4]
# print(sum_consecutives([1, 1, 2, 2])) # == [2, 4]


def simple_areas(*args):
    from math import pi
    # Circle
    if len(args) == 1:
        return round(pi * (args[0] / 2) ** 2, 2)
    # Rectangle
    elif len(args) == 2:
        return round(args[0] * args[1], 2)
    # Triangle
    else:
        p = (args[0] + args[1] + args[2]) / 2
        return round((p * (p - args[0]) * (p - args[1]) * (p - args[2])) ** 0.5, 2)


# print(simple_areas(3)) # == 7.07
# print(simple_areas(2, 2)) # == 4
# print(simple_areas(2, 3)) # == 6
# print(simple_areas(3, 5, 4)) # == 6
# print(simple_areas(1.5, 2.5, 2)) # == 1.5)


def check_command(ptrn, cmd):
    a = str(bin(ptrn))
    a = '0' * (len(cmd) - len(a[2:])) + a[2:]

    if len(cmd) < len(a):
        return False

    for n, s in enumerate(cmd):
        if a[n] == '0' and s.isalpha() or a[n] == '1' and s.isdigit():
            return False
    return True


# print(check_command(8,"a")) # == False
# print(check_command(42, "12a0b3e4")) # == True
# print(check_command(101, "ab23b4zz")) # == False


def weak_point(m):
    rows = [sum(x) for x in m]
    cols = []

    for x in range(len(m[0])):
        col = 0
        for y in m:
            col += y[x]
        cols.append(col)

    return [rows.index(min(rows)), cols.index(min(cols))]


#################################################################


def next_stages(x, y, obs, psh=True):
    pass


def first_stage(x, y, obs, psh=True):
    pass


def landing_site(obs):
    ALPHA = 'ABCDEFGHIJKL'
    hexa = []
    for x in range(9):
        hexa.append([])
        for y in range(12):
            hexa[-1].append(ALPHA[y] + str(x + 1))

    sites = []
    site = False
    for x, row in enumerate(hexa[1:-1], start=1):
        for y, s in enumerate(row[1:-1], start=1):
            if s not in obs:
                psh = (y + 1) % 2
                site = first_stage(x, y, obs, psh)
                if site:
                    sites.append(site)

    mx_site = (sorted(sites, key=len))[-1]
    # sites = list(filter(sites, lambda x: x if len(x)==len(mx_site)))

    for x in hexa:
        print(x)

    return sites


# print(landing_site({'E5', 'E7', 'F4', 'F6', 'G4', 'G6', 'H3', 'H5'})) # == {'C3', 'J7'}
# print(landing_site({'A4', 'C2', 'C6', 'C9', 'D4', 'D7', 'F1', 'F5',
#                      'F8', 'G4', 'H7', 'I2', 'I5', 'I9', 'K3', 'K8', 'L5'})) # == {'B7', 'E3', 'J6'}


def convert(code):
    bin_code = bin(code)[2:].zfill(6)[::-1]
    return [[int(bin_code[j + i * 3]) for i in range(2)] for j in range(3)]


LETTERS_NUMBERS = list(map(convert,
                           [1, 3, 9, 25, 17, 11, 27, 19, 10, 26,
                            5, 7, 13, 29, 21, 15, 31, 23, 14, 30,
                            37, 39, 62, 45, 61, 53, 47, 63, 55, 46, 26]))
CAPITAL_FORMAT = convert(32)
NUMBER_FORMAT = convert(60)
PUNCTUATION = {",": convert(2), "-": convert(18), "?": convert(38),
               "!": convert(22), ".": convert(50), "_": convert(36)}
WHITESPACE = convert(0)


def braille_page(text: str):
    from string import ascii_lowercase as al

    nums_caps = len([x for x in text if x.isdigit()]) + len([x for x in text if x.isupper()])
    ln = (len(text) + nums_caps)
    if ln <= 10:
        rows = 1
        cols = ln * 3 - 1
    else:
        num = 0
        if ln % 10:
            num = 1
        rows = ln // 10 + num
        cols = 29

    m = []
    for x in range(rows):
        for y in range(3):
            m.append([0] * cols)
        if x < rows - 1:
            m.append([0] * cols)

    step = [0, 0]
    for x in text:
        a = []
        if x.isalpha():
            if x.isupper():
                a.append(CAPITAL_FORMAT)
            a.append(LETTERS_NUMBERS[al.index(x.lower())])
        elif x.isdigit():
            a.append(NUMBER_FORMAT)
            a.append(LETTERS_NUMBERS[int(x) - 1])
        elif x.isspace():
            a.append(WHITESPACE)
        else:
            a.append(PUNCTUATION.get(x))

        for n, y in enumerate(a):
            for z in range(3):
                m[step[0] + z][step[1]] = y[z][0]
                m[step[0] + z][step[1] + 1] = y[z][1]
            if step[1] < (cols - 3):
                step[1] += 3
            else:
                step[0] += 4
                step[1] = 0
    return m


# print(braille_page(u"0123456789"))
# print(braille_page(u"42"))
# print(braille_page("hello 1st World!"))


FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(num):
    num = str(num)

    res = ''
    if len(num) == 3:
        res += FIRST_TEN[int(num[0]) - 1] + ' ' + HUNDRED + ' '
        num = num[1:]
        if num == '00':
            return res.strip()

    if len(num) == 2:
        if num[0] != '0' and int(num) < 20:
            res += SECOND_TEN[int(num) - 10]
        else:
            n2 = str(OTHER_TENS[int(num[0]) - 2]) + ' ' if num[0] != '0' else ''
            n3 = str(FIRST_TEN[int(num[1]) - 1]) if num[1] != '0' else ''
            res += n2 + n3

    if len(num) == 1:
        res += FIRST_TEN[int(num) - 1]
    return res.strip()


# print(checkio(4))  # =='four'
# print(checkio(143))  # =='one hundred forty three'
# print(checkio(12))  # =='twelve'
# print(checkio(101))  # =='one hundred one'
# print(checkio(212))  # =='two hundred twelve'
# print(checkio(40))  # =='forty'

class Friends:
    cons = []

    @classmethod
    def add(cls, bond):
        if bond not in cls.cons:
            cls.cons.append(bond)

    @classmethod
    def connected(cls, name):
        names = set()
        for bond in cls.cons:
            if name in bond:
                for x in bond:
                    if x != name:
                        names.add(x)
        return names

    @classmethod
    def clear(cls):
        cls.cons = []


def check_connection(nw, f1, f2):
    f = Friends()
    for x in nw:
        a, b = x.split('-')
        if a == f1 and b == f2 or a == f2 and b == f1:
            Friends.clear()
            return True
        f.add({a, b})

    nxt1, nxt2 = [], []
    nxt1.extend(f.connected(f1))
    nxt2.extend(f.connected(f2))
    res = list(filter(lambda x: x in nxt1, nxt2))
    if len(res) > 0:
        Friends.clear()
        return True

    z = 0
    fs1, fs2 = [], []
    cons = f.cons
    while z < len(cons):
        nxt1 = set(nxt1)
        nxt2 = set(nxt2)
        fs1.extend([x for x in nxt1 if fs1.count(x) == 0])
        fs2.extend([x for x in nxt2 if fs2.count(x) == 0])
        nxt1 = []
        nxt2 = []
        for x in fs1:
            nxt1.extend(f.connected(x))
        for x in fs2:
            nxt2.extend(f.connected(x))
        res = list(filter(lambda x: x in nxt1, nxt2))
        if len(res) > 0:
            Friends.clear()
            return True
        z += 1
    Friends.clear()
    return False


###################################################################################################


def grid():
    for x in range(1, 17):
        yield x


def clean_slepok(x, slepok):
    while sum(slepok[x]) == 0:
        del slepok[x]

    col = 0
    while col == 0:
        for n, y in enumerate(slepok):
            col += slepok[n][x]
        if col == 0:
            for n, y in enumerate(slepok):
                del slepok[n][x]
    return slepok


def rotate(slepok):
    res = []
    for x in range(len(slepok[0])):
        res.append([])
        for y in reversed(range(len(slepok))):
            res[-1].append(slepok[y][x])
    return res


def patterns(slepok):
    PATTERNS = {
        'I': [[1], [1], [1], [1]],
        'J': [[0, 1], [0, 1], [1, 1]],
        'L': [[1, 0], [1, 0], [1, 1]],
        'O': [[1, 1], [1, 1]],
        'S': [[0, 1, 1], [1, 1, 0]],
        'T': [[1, 1, 1], [0, 1, 0]],
        'Z': [[1, 1, 0], [0, 1, 1]]
    }
    signs = 'IJLOSTZ'
    for y in range(4):
        for x in signs:
            if PATTERNS[x] == slepok:
                return x
        slepok = rotate(slepok)
    return None


def identify_block(nums):
    m = []
    gen = grid()
    for x in range(4):
        m.append([])
        for y in range(4):
            m[-1].append(next(gen))

    slepok = []
    for x in range(4):
        slepok.append([])
        for y in range(4):
            slepok[-1].append(0)

    for x in nums:
        for n, y in enumerate(m):
            if x in y:
                slepok[n][y.index(x)] = 1

    slepok = clean_slepok(0, slepok)
    slepok = clean_slepok(-1, slepok)

    if len(slepok) == 1 and sum(slepok[0]) == 4:
        return 'I'

    res = patterns(slepok)
    return res


# print(identify_block({1, 2, 3, 4})) # == 'I'
# print(identify_block({1, 2, 3, 6})) # == 'T'
# print(identify_block({1, 5, 6, 10})) # == 'S'
# print(identify_block({10, 13, 14, 15})) # == 'T', 'T'
# print(identify_block({1, 5, 9, 6})) # == 'T', 'T'
# print(identify_block({2, 3, 7, 11})) # == 'L', 'L'
# print(identify_block({4, 8, 12, 16})) # == 'I', 'I'
# print(identify_block({3, 1, 5, 8})) # == None, 'None'


def checkio(s):
    b = ['(', '[', '{', ')', ']', '}']

    x = 0
    while x < len(s):
        if s[x] in b:
            x += 1
            continue
        s = s.replace(s[x], '')

    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')

    if s == '':
        return True
    return False


# print(checkio("((5+3)*2+1)"))  # == True
# print(checkio("{[(3+1)+2]+}"))  # == True
# print(checkio("(3+{1-1)}"))  # == False
# print(checkio("[1+1]+(2*2)-{3/3}"))  # == True
# print(checkio("(({[(((1)-2)+3)-3]/3}-3)"))  # == False
# print(checkio("2+3"))  # == True)


def double_substring(s):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    res = []
    for a in range(len(s) - 1):
        for b in range(a + 1, len(s)):
            if s.count(s[a:b]) > 1:
                res.append(len(s[a:b]))
    if res == []:
        return 0
    return max(res)


# print(double_substring('aaaa'))  # == 2
# print(double_substring('abc'))  # == 0
# print(double_substring('aghtfghkofgh'))  # == 3 # fgh


def non_empty_lines(text: str) -> int:
    return len(list((text.replace(' ', '')).split()))


# print(non_empty_lines('one simple line')) # == 1
# print(non_empty_lines('')) # == 0
# print(non_empty_lines('\nonly one line\n            ')) # == 1
# print(non_empty_lines('''
# Lorem ipsum dolor sit amet,
#
# consectetur adipiscing elit
# Nam odio nisi, aliquam
#             ''')) # == 3


def checkio(n, m):
    n, m = bin(n)[2:], bin(m)[2:]
    dif = len(n) - len(m)
    if dif < 0:
        n = '0' * abs(dif) + n
    else:
        m = '0' * dif + m
    res = 0
    for a, x in enumerate(n):
        if x != m[a]:
            res += 1
    return res


# print(checkio(117, 17)) # == 3
# print(checkio(1, 2)) # == 2
# print(checkio(16, 15)) # == 5)

def square_board(side: int, token: int, steps: int):
    board = []
    for x in range(side):
        board.append([0] * side)

    nums = iter([x for x in range((side - 1) * 4)])
    for x in reversed(range(side)):
        board[-1][x] = next(nums)
    for x in reversed(range(side - 1)):
        board[x][0] = next(nums)
    for x in range(1, side):
        board[0][x] = next(nums)
    for x in range(1, side - 1):
        board[x][-1] = next(nums)

    nums = (side - 1) * 4
    fin = token + steps
    fin = nums + fin if fin < 0 else fin
    while fin >= nums:
        fin -= nums

    res = []
    for x in range(side):
        for y in range(side):
            if fin == board[x][y]:
                res = [x, y]
    return res


# print(square_board(4, 1, 4))  # == (1, 0)
# print(square_board(6, 2, -3))  # == (4, 5)


def subnetworks(net, crushes):
    for x in net:
        for y in crushes:
            if y in x:
                x.remove(y)

    net = list(filter(lambda x: x != [], net))
    if len(net) == 1: return 1

    x = 0
    while x < len(net):
        lol = True
        if len(net[x]) == 1:
            for y in net:
                if net[x] != y and net[x][0] in y:
                    del net[x]
                    lol = False
            if lol:
                x += 1
        else:
            x += 1
    return len(net)


# print(subnetworks([["A", "B"],
#                    ["A", "C"],
#                    ["A", "D"],
#                    ["D", "F"],
#                    ["B", "C"]
#                    ], ["A"]))  # = 2
# print(subnetworks([
#         ['A', 'B'],
#         ['B', 'C'],
#         ['C', 'D']
#     ], ['B']))  # == 2
# print(subnetworks([
#         ['A', 'B'],
#         ['A', 'C'],
#         ['A', 'D'],
#         ['D', 'F']
#     ], ['A']))  # == 3
# print(subnetworks([
#         ['A', 'B'],
#         ['B', 'C'],
#         ['C', 'D']
#     ], ['C', 'D']))  # == 1


# Наконец задачка по системах счисления! Ура!)))))

def checkio(str_number: str, radix: int) -> int:
    if radix == 10:
        try:
            str_number = int(str_number)
            return str_number
        except:
            return -1

    if radix < 10 and any([x for x in str_number if x.isalpha()]):
        return -1

    res = 0
    str_number = str_number[::-1]
    from string import ascii_uppercase as au
    for n, x in enumerate(str_number):
        if x.isalpha():
            if (10 + au.index(x)) >= radix: return -1
            res += (10 + au.index(x)) * radix ** n
        else:
            if int(x) == radix: return -1
            res += int(x) * radix ** n
    return res


# print(checkio('705', 8))
# print(checkio("255",7))  # == 138
# print(checkio("AF", 16))  # == 175
# print(checkio("101", 2))  # == 5
# print(checkio("101", 5))  # == 26
# print(checkio("Z", 36))  # == 35
# print(checkio("AB", 10))  # == -1
# print(checkio("AB", 5))  # == -1
# print(checkio("23", 10))  # == 23
# print(checkio("10110101110011", 2))
# print(checkio("12FD", 16))  # == 4861
# print(checkio("1100", 2))  # == 12
# print(checkio("ASD",15))  # == -1
# print(checkio("909",9))  # == -1


def weekly_calendar(year: int, month: int, day: int, firstweekday: int):
    import datetime as dt
    wd = dt.datetime(year, month, day).weekday()
    if wd > firstweekday:
        fd = dt.datetime(year, month, day) - dt.timedelta(days=(wd - firstweekday))
    elif wd == firstweekday:
        fd = dt.datetime(year, month, day)
    else:
        fd = dt.datetime(year, month, day) - dt.timedelta(days=(wd + (7 - firstweekday)))

    res = []
    for x in range(7):
        d = fd + dt.timedelta(days=x)
        res.append(d.day)
    return res


# print(list(weekly_calendar(2020, 1, 1, 0)))  # == [30, 31, 1, 2, 3, 4, 5]
# print(list(weekly_calendar(2020, 9, 20, 6)))  # == [20, 21, 22, 23, 24, 25, 26]
# print(list(weekly_calendar(2020, 9, 30, 0)))  # == [28, 29, 30, 1, 2, 3, 4])
# print(weekly_calendar(7239,10,26,5))  # == [22,23,24,25,26,27,28]

from typing import Dict, Tuple

Date = Tuple[int, int, int]


def next_birthday(today: Date, birthdates: Dict[str, Date]) -> Tuple[int, Dict[str, int]]:
    import datetime as dt
    today = dt.datetime(today[0], today[1], today[2])
    bd = {k: dt.datetime(v[0], v[1], v[2]) for k, v in birthdates.items()}
    bd = {k: v for k, v in sorted(bd.items(), key=lambda para: para[1])}
    bd_keys = list(bd.keys())
    bd_values = list(bd.values())

    y = 0
    ages = {}
    bds = {}
    while y < len(bd_keys):
        today2 = None
        # check if birthday is 29 February
        if bd_values[y].month == 2 and bd_values[y].day == 29:
            year = today.year
            if today.month > 2:
                if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                    today2 = today
                    today = dt.datetime(today.year + 1, today.month, today.day)
                year = today.year + 1
            # check if year is without 29 February
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                pass
            else:
                bd_values[y] = dt.datetime(bd_values[y].year, 3, 1)

        for x in range(365):
            nxt_day = today + dt.timedelta(days=x)
            if nxt_day.month == bd_values[y].month and nxt_day.day == bd_values[y].day:
                to_bd = nxt_day - today2 if today2 else nxt_day - today
                age = nxt_day.year - bd_values[y].year
                ages[bd_keys[y]] = age  # how old he/she will be
                bds[bd_keys[y]] = to_bd  # how long to birthday
                y += 1
                break

    bds_values = list(bds.values())
    best = min(bds_values)

    rs = {}
    for k, v in bds.items():
        if v == best:
            rs[k] = ages[k]

    res = (best.days, rs)
    return res


# print(next_birthday([2024, 3, 1], {"Baby": [2020, 2, 29]}))  # [365,{"Baby":5}]
# print(next_birthday([2014, 3, 29], {"Emilie": [1990, 7, 31], "Jean-Baptiste": [1985, 6, 3], "Cameron": [1995, 11, 12],
#                                     "Mia": [1999, 4, 5], "Elena": [1980, 1, 8], "Alexei": [1993, 10, 28],
#                                     "Youssef": [1992, 4, 5], "Soraya": [1996, 12, 27], "Jiao": [1988, 2, 29],
#                                     "Kang": [2012, 8, 15], "Pedro": [1959, 5, 2], "Manuela": [1961, 3, 18],
#                                     "Inaya": [1968, 9, 22], "Moussa": [1976, 2, 29]}))
# # == [7,{"Mia":15, "Youssef":22}]
#
# birthdates = {
#     'Emma': (2000, 12, 25),
#     'Brian': (1967, 5, 31),
#     'Léna': (1970, 10, 3),
#     'Philippe': (1991, 6, 15),
#     'Yasmine': (1996, 2, 29),
# }
# print(next_birthday((2020, 9, 8), birthdates))  # == (25, {'Léna': 50})
# print(next_birthday((2021, 10, 4), birthdates))  # == (82, {'Emma': 21})
# print(next_birthday((2022, 3, 1), birthdates))  # == (0, {'Yasmine': 26})


def nbrs(g, row, col):
    NBRS = {
        1: lambda x, y: [x - 1, y - 1],  # left upper square
        2: lambda x, y: [x - 1, y],
        3: lambda x, y: [x - 1, y + 1],
        4: lambda x, y: [x, y + 1],
        5: lambda x, y: [x + 1, y + 1],
        6: lambda x, y: [x + 1, y],
        7: lambda x, y: [x + 1, y - 1],
        8: lambda x, y: [x, y - 1]
    }

    res = 0
    for x in range(1, 9):
        a, b = NBRS[x](row, col)
        if len(g) > a >= 0 and len(g[0]) > b >= 0:
            res = res + 1 if g[a][b] == 1 else res
    return res


def life_counter(m, n):
    matrix = [list(x) for x in m]
    steps = 1
    while steps<=n:
        if sum(matrix[-1])>0:
            matrix.append([0] * len(matrix[0]))
        elif sum(matrix[-1])==0 and sum(matrix[-2])==0:
            del matrix[-1]
        if sum(matrix[0])>0:
            matrix.insert(0, [0] * len(matrix[0]))
        elif sum(matrix[0])==0 and sum(matrix[1])==0:
            del matrix[0]

        left = [matrix[x][0] for x in range(len(matrix))]
        left2 = [matrix[x][1] for x in range(len(matrix))]
        if sum(left)>0:
            for a, row in enumerate(matrix):
                row = [0] + row
                matrix[a] = row
        elif sum(left)==0 and sum(left2)==0:
            for a, row in enumerate(matrix):
                matrix[a] = row[1:]

        right = [matrix[x][-1] for x in range(len(matrix))]
        right2 = [matrix[x][-2] for x in range(len(matrix))]
        if sum(right) > 0:
            for a, row in enumerate(matrix):
                row.append(0)
                matrix[a] = row
        elif sum(right)==0 and sum(right2)==0:
            for a, row in enumerate(matrix):
                matrix[a] = row[:-1]

        born = [[0] * len(matrix[0]) for _ in matrix]
        die = [[1] * len(matrix[0]) for _ in matrix]

        for a, row in enumerate(matrix):
            for b, x in enumerate(row):
                alive = nbrs(matrix, a, b)
                if x == 0 and alive == 3:
                    born[a][b] = 1
                elif x == 1 and alive not in [2, 3]:
                    die[a][b] = 0

        for a, row in enumerate(matrix):
            for b, x in enumerate(row):
                if born[a][b] == 1: matrix[a][b] = 1
                if die[a][b] == 0: matrix[a][b] = 0
        steps += 1
    return sum([sum(x) for x in matrix])


# print(life_counter(((0, 1, 0, 0, 0, 0, 0),
#                     (0, 0, 1, 0, 0, 0, 0),
#                     (1, 1, 1, 0, 0, 0, 0),
#                     (0, 0, 0, 0, 0, 1, 1),
#                     (0, 0, 0, 0, 0, 1, 1),
#                     (0, 0, 0, 0, 0, 0, 0),
#                     (1, 1, 1, 0, 0, 0, 0)), 4))  # == 15
#
# print(life_counter(((0, 1, 0, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0), (1, 1, 1, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 1, 1), (0, 0, 0, 0, 0, 1, 1), (0, 0, 0, 0, 0, 0, 0),
#            (1, 1, 1, 0, 0, 0, 0)), 15))  # 14 (0, 7, -3, 6)
# print(life_counter(((0, 1, 0), (0, 0, 1), (1, 1, 1)), 50))  # 5 (0, 15, 0, 14)
# print(life_counter(((1, 1, 0, 1, 1), (1, 1, 0, 1, 1), (0, 0, 0, 0, 0), (1, 1, 0, 1, 1),
#            (1, 1, 0, 1, 1)), 100))  # == 16 (0, 4, 0, 4),
# print(life_counter(((0, 0, 0, 0, 0, 0, 1, 0), (1, 1, 0, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 1, 1, 1)),  129))
# # 2 (-4, 18, -6, 11),
# print(life_counter(((0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1),
#            (1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1),
#            (1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1),
#            (0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0),
#            (1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1),
#            (1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1),
#            (1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0)), 100))  # 56 (-1, 13, -1, 13),
# print(life_counter(((0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
#            (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
#            (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1),
#            (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
#            (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
#            (0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0),
#            (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),
#            (0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0)), 42))  # 36 (-12, 10, -1, 16),
# print(life_counter(((0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1), (0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1),
#            (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
#            (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1), (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
#            (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1), (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1)), 100))  # 33 (-9, 15, -5, 22),
# print(life_counter(((0, 1, 0), (0, 0, 1), (1, 1, 1)), 999))  # 5 None,
# print(life_counter(((0, 1, 0, 0, 0, 0, 1, 0), (1, 0, 0, 0, 0, 0, 0, 1), (1, 1, 1, 0, 0, 1, 1, 1)),
#     999))  # 10 None,
# print(life_counter(((0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1), (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
#            (0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1), (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
#            (1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1), (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
#            (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1), (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1)), 100))  # 52 (-18, 20, -5, 20),
# print(life_counter(((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
#            (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
#            (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)), 10))  # 22 (0, 17, 0, 16),
# print(life_counter(((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
#            (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
#            (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
#            (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
#            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)), 20))  # 0 (0, 17, 0, 16),
# print(life_counter(((0, 0, 0, 0, 0, 0, 0, 0), (1, 1, 1, 0, 0, 1, 1, 1), (0, 0, 0, 0, 0, 1, 0, 0),
#            (0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 0), (1, 1, 1, 0, 0, 0, 0, 0),
#            (0, 0, 0, 0, 0, 1, 1, 1), (0, 0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0),
#            (1, 1, 1, 0, 0, 0, 0, 0)), 100))  # 3 (-1, 10, -2, 7),
# print(life_counter([[0, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
#            [0, 0, 1, 0, 0, 0, 0, 0, 1, 1], [1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
#            [1, 0, 1, 0, 0, 1, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1, 0, 1, 1, 1],
#            [1, 0, 1, 0, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
#            [0, 0, 1, 0, 1, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 1, 1, 1, 1]], 50))  # 74 (-6, 13, -5, 24),
# print(life_counter([[1, 1, 1, 1, 0, 1, 1, 0, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
#            [0, 1, 0, 1, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 0, 1, 0, 0, 1],
#            [0, 1, 1, 1, 0, 1, 1, 1, 0, 0], [1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
#            [1, 0, 1, 0, 0, 0, 0, 0, 1, 1], [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
#            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 1, 0, 1, 1]], 50))  # 79 (-5, 17, -14, 16),
# print(life_counter([[0, 0, 1, 1, 1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0, 1, 1, 1, 0],
#            [0, 1, 1, 1, 1, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
#            [1, 1, 0, 1, 0, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
#            [1, 0, 0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
#            [1, 0, 0, 1, 0, 0, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1, 0, 1, 0]], 50))  # 81 (-9, 15, -4, 24),
# print(life_counter([[1, 0, 0, 0, 1, 0, 0, 0, 1, 0], [1, 1, 0, 0, 1, 0, 1, 0, 1, 0],
#            [1, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
#            [0, 1, 1, 1, 1, 1, 0, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
#            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 0, 1, 1],
#            [0, 1, 1, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 0, 0, 1, 1, 1, 1, 0]], 50))  # 18 (-3, 16, -5, 13),


def is_stressful(subj):
    """
        recognize stressful subject
    """
    if len([x for x in subj if x.isupper() or not x.isalpha()])==len(subj) or subj[-3:]=='!!!' or \
            len([x for x in ['help', 'asap', 'urgent'] if x in subj.lower() or \
                x in ''.join([x for x in subj if x.isalpha()]).lower()]):
        return True

    res = ''
    for x in subj:
        if res.count(x)<1:
            res += x

    if len([x for x in ['help', 'asap', 'urgent'] if x in res.lower()]):
        return True
    return False

# print(is_stressful("HI HOW ARE YOU?"))  # == True
# print(is_stressful("UUUURGGGEEEEENT here"))  # == True
# print(is_stressful("Hi"))  # == False
# print(is_stressful("I neeed HELP"))  # == True
# print(is_stressful("HELP"))  # == True
# print(is_stressful("Attention!!!"))  # == True
# print(is_stressful("HHHEEEEEEEEELLP"))  # == True
# print(is_stressful("H-E-L-P"))  # == True
# print(is_stressful("H! E! L! P!"))  # == True


dic = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
       100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

def roman(n):
    res = ''
    for k in sorted(dic.keys(), reverse=True):
        while n>=k:
            res += dic[k]
            n -= k
    return res

def reverse_roman(s):
    for x in range(1, 4000):
        if roman(x) == s:
            return x

# print(reverse_roman('VI'))  # == 6
# print(reverse_roman('LXXVI'))  # == 76
# print(reverse_roman('CDXCIX'))  # == 499
# print(reverse_roman('MMMDCCCLXXXVIII'))  # == 3888


def count_consecutive_summers(num):
    res, n, sm = 1, 1, 0
    while n < num:
        for x in range(n, num+1):
            sm += x
            if sm == num:
                res += 1
                n += 1
                sm = 0
                break
            elif sm > num:
                n += 1
                sm = 0
                break
    return res

# print(count_consecutive_summers(42))  # == 4
# print(count_consecutive_summers(99))  # == 6


def add_fractions(*args):
    from fractions import Fraction
    if len(list(args))==1: fracts = args[0]
    else: fracts = list(args)

    res = 0
    for x in fracts:
        res += Fraction(x[0], x[1])

    if type(res)==int or res==1: return 1
    if res.denominator==1: return res.numerator

    frst = 0
    numer = res.numerator
    while numer>res.denominator:
        numer -= res.denominator
        frst += 1

    if frst and numer:
        res = f'{frst} and {numer}/{res.denominator}'
    return str(res)

# print(add_fractions([1,3],[1,3]))  # == 2/3
# print(add_fractions([2,1],[3,1],[4,2],[5,1]))  # == 12
# print(add_fractions([2,3],[2,3]))  # == "1 and 1/3"
# print(add_fractions(((2, 3), (2, 3))))  # == "1 and 1/3"
# print(add_fractions(((1, 3), (1, 3))))  # == "2/3"
# print(add_fractions(((1, 3), (1, 3), (1, 3))))  # == 1)

from typing import List

nums = [[[1,1,0],
    [1,0,1],
    [1,0,1],
    [1,0,1],
    [0,1,1]],[[0,1,0],
             [1,1,0],
             [0,1,0],
             [0,1,0],
             [0,1,0]], [[1,1,1],
                        [0,0,1],
                        [0,1,1],
                        [1,0,0],
                        [1,1,1]], [[1,1,1],
                                   [0,0,1],
                                   [0,1,0],
                                   [0,0,1],
                                   [1,1,1]], [[1,0,1],
                                              [1,0,1],
                                              [1,1,1],
                                              [0,0,1],
                                              [0,0,1]], [[1,1,1],
                                                         [1,0,0],
                                                         [1,1,0],
                                                         [0,0,1],
                                                         [1,1,0]], [[0,1,1],
                                                                    [1,0,0],
                                                                    [1,1,1],
                                                                    [1,0,1],
                                                                    [0,1,1]], [[1,1,1],
                                                                               [0,0,1],
                                                                               [0,1,0],
                                                                               [1,0,0],
                                                                               [1,0,0]], [[1,1,1],
                                                                                          [1,0,1],
                                                                                          [1,1,1],
                                                                                          [1,0,1],
                                                                                          [1,1,1]], [[0,1,1],
                                                                                                     [1,0,1],
                                                                                                     [1,1,1],
                                                                                                     [0,0,1],
                                                                                                     [1,1,0]]]

def checkio(image: List[List[int]]) -> int:
    res = ''
    while image!=[]:
        num = []
        for n, row in enumerate(image):
            num.append(row[1:4])
            image[n] = row[4:]

        for n, matrix in enumerate(nums):
            if num[0] == []: break
            noise = 0
            for a, row in enumerate(matrix):
                if row != num[a]:
                    for b, x in enumerate(row):
                        if x != num[a][b]:
                            noise += 1
                if noise>1: break
            if noise<=1:
                res += str(n)
                break
        if image[0]==[]: break
    return int(res)

print(checkio([ [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]))  # == 394
print(checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
         [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
         [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]))  # == 394)




