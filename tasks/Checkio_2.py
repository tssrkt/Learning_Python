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

    for x in range(len(a)-1):
        for y in range(x+1, len(a)):
            if a[x]!=0 and a[y]!=0:
                if a[x][-1]>=a[y][0] or a[x][-1]==a[y][0]+1 or a[x][-1]==a[y][0]-1:
                    if a[x][-1]>=a[y][-1]:
                        a[y]=0
                        continue
                    a[x][-1]=a[y][-1]
                    a[y]=0
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
        if a[x][0]+1<a[x][-1]:
            for y in range(a[x][0]+1, a[x][-1]):
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
            return x[z+1:].replace(';', '')

# print(get_cookie("USER=name=Unknown; domain=bbc.com","USER")) # == name=Unknown
# print(get_cookie("ffo=false; domain=google.com; expires=Sunday, 20-May-2018 00:00:00 GMT","expires"))
# # == "Sunday, 20-May-2018 00:00:00 GMT"
# print(get_cookie('theme=light; sessionToken=abc123', 'theme')) # == 'light'
# print(get_cookie('_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo')) # == 'true'


def unix_match(fn: str, ptrn: str) -> bool:
    if set(ptrn)=={'*'} or set(ptrn)=={'*', '?'} and len(ptrn)<=len(fn):
        return True

    if fn.count('.')==1 and ptrn.count('.')==1:
        fn = fn.split('.')
        ptrn = ptrn.split('.')
    elif len(fn)==len(ptrn):
        for x in range(len(fn)):
            if ptrn[x] == '?' or ptrn[x] == fn[x]:
                continue
            else:
                return False
        return True
    elif '.*' in ptrn and '.' in fn:
        for x in range(len(fn)):
            if ptrn[x]=='?' or ptrn[x]==fn[x]:
                continue
            elif ptrn[x]=='*':
                return True
            else:
                return False
    if type(fn)==list and len(fn)==len(ptrn):
        if fn[-1]==ptrn[-1] or ptrn[-1]=='*' or set(ptrn[-1])=={'?'} and len(ptrn[-1])==len(fn[-1]):
            if ptrn[0]=='*':
                return True
            if '?' in ptrn[0] and len(fn[0])==len(ptrn[0]):
                for x in range(len(fn[0])):
                    if ptrn[0][x]=='?' or ptrn[0][x]==fn[0][x]:
                        continue
                    else:
                        return False
                return True
            elif ptrn[0]=='*' or fn[0]==ptrn[0]:
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
    if fn==ptrn:
        return True
    after = False
    new_ptrn = ''
    for x in range(len(fn)):
        if ptrn[x]==fn[x] and after==False:
            continue
        elif ptrn[x]=='[' and after==False:
            new_ptrn = ptrn[:ptrn.index('[')] + fn[x] + ptrn[ptrn.index(']') + 1:]
            after = True
            if ptrn_check(ptrn, fn, x):
                continue
            else:
                return False
        elif after==True:
            if '[' not in new_ptrn and ']' not in new_ptrn and new_ptrn==fn:
                return True
            elif '[' not in new_ptrn and ']' not in new_ptrn and new_ptrn!=fn:
                return False
            elif '[' in new_ptrn and ']' in new_ptrn and new_ptrn[x]==fn[x]:
                continue
            elif new_ptrn[x]=='[':
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
        if type(x)==list:
            lst2.extend(x)
        else:
            lst2.append(x)
    return lst2

def get_key(d, value):
    for k, v in d.items():
        if value in v:
            return k

def is_family(tree: list[list[str]]) -> bool:
    if len(tree)==1:
        return True
    d = {}
    for x in range(len(tree)):
        person = tree[x][0]
        son = tree[x][1]
        if person==son:
            return False
        if d=={}:
            d.setdefault(person, [son])
        else:
            if person in d.keys():
                d[person].append(son)
            elif person in flatten(d.values()):
                grandpa = get_key(d, person)
                if son==grandpa or son in flatten(d.values()):
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
    if n>=len(s):
        return s

    a = s.split()
    res = a[0]
    for x in range(1, len(a)):
        if len(res)>n:
            return '...'
        elif len(res + ' ' + a[x])<=n:
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
        if price==v:
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
                res += alpha[z+n]
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
        1: lambda x, y: [x-1, y-1],  # left upper square
        2: lambda x, y: [x-1, y],
        3: lambda x, y: [x-1, y+1],
        4: lambda x, y: [x, y+1],
        5: lambda x, y: [x+1, y+1],
        6: lambda x, y: [x+1, y],
        7: lambda x, y: [x+1, y-1],
        8: lambda x, y: [x, y-1]
    }

    res = 0
    for x in range(1, 9):
        a, b = NBRS[x](row, col)
        if len(g)>a>=0 and len(g[0])>b>=0:
            res = res+1 if g[a][b]==1 else res
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
        if s.count('.')>1:
            return s.replace('.', ',')
        else:
            z = s.split('.')[-1]
            z = ''.join(i for i in z if i.isdigit())
            if z.isdigit() and int(z)==0:
                return s.replace('.', ',')
            return s
    if '.' not in s:
        if s.count(',')==1:
            return s.replace(',', '.')
        if s.count(',')>1:
            return s
    s = s.replace(',', '.')
    n = s.count('.') - 1
    return s.replace('.', ',', n)

def checkio(s: str) -> str:
    res = ''
    dt = False
    if '$' not in s:
        return s
    if s[-1]=='.':
        dt = True
        s = s[:-1]
    if s.count('$')>1:
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

QUESTIONS = {"color":'color', "nationality":'man', "beverage":'drink', "cigarettes":'ciga', "pet":'pet'}

# for all
def gt(item, slovar):
    for k,v in slovar.items():
        if item in v:
            return k

# for pancha
def gt2(item, slovar):
    for k,v in slovar.items():
        if item in list(v.values()):
            return k

def lopata(rels, pancha):
    new_rels = []
    for a in rels:
        x = a.split('-')
        if gt2(x[0], pancha)!=None and x[1].isalpha():
            pancha[gt2(x[0], pancha)][gt(x[1], all)] = x[1]
        elif gt2(x[1], pancha)!=None and x[0].isalpha():
            pancha[gt2(x[1], pancha)][gt(x[0], all)] = x[0]
        else:
            new_rels.append(a)
    return pancha, new_rels

def bandura(pancha):
    for key in all.keys():
        spisok = []
        for k,v in pancha.items():
            spisok.append(v[key])
        spisok = list(filter(lambda x: x!='', spisok))
        if len(spisok)==4:
            item = list(filter(lambda x: x not in spisok, all[key]))[0]
            for k,v in pancha.items():
                if v[key]=='':
                    v[key]=item
    return pancha

def answer(rels, q):
    pancha = {k:{'man': '', 'drink': '', 'pet': '', 'ciga': '', 'color': ''} for k in range(1, 6)}
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
    while len(new_rels)>0:
        pancha, new_rels = lopata(new_rels, pancha)
        pancha = bandura(pancha)

    # Answering on the question
    q = q.split('-')
    if q[1]=='number':
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
    if len(set(a))==1:
        return a
    res = [a[0]]
    palin = ''
    for x in range(1, len(a)-1):
        for y in range(x+1, len(a)):
            z = x - (y - x)
            if z>=0 and a[y]==a[z]:
                palin = a[x] if palin=='' else palin
                palin = a[y] + palin + a[z]
                continue
            else:
                if palin!='':
                    res.append(palin)
                    palin = ''
                break
    res.sort(key=len, reverse=True)
    return res[0]

# print(longest_palindromic("123abcba")) # == "abcba"
# print(longest_palindromic("aaaaa")) # == "aaaaa"
# print(longest_palindromic('abc')) # == 'a'
# print(longest_palindromic('abacada')) # == 'aba'

#ALPHA (%41–%5A and %61–%7A), DIGIT (%30–%39)


def checkio(url):
    import string as s
    SIGNS = {'%2D': '-', '%2E': '.', '%5F': '_', '%7E': '~'}
    ALPHA = s.ascii_lowercase
    nums = ['4', '5', '6', '7']

    url = url.lower()
    if ':80/' in url or ':80' in url and url.rfind('0')==len(url)-1:
        url = url.replace(':80', '')
    if '/./' in url and '../' not in url:
        url = url.replace('./', '')
    new_url = url
    if '%' in url:
        x = url.find('%')
        new_url = url[:x]
        while x< len(url):
            if url[x]=='%':
                a = url[x:x+3].upper()
                if a in SIGNS:
                    new_url += SIGNS.get(a)
                    x += 3
                elif url[x+1]=='3' and url[x+2].isdigit():
                    new_url += url[x+2]
                    x += 3
                elif url[x+1] in nums:
                    if url[x+1]=='4':
                        if url[x+2].isdigit():
                            new_url += ALPHA[int(url[x+2])-1]
                        x += 3
                    elif url[x+1]=='5':
                        new_url += ALPHA[ALPHA.index(url[x+2])+18]
                        x += 3
                    elif url[x+1]=='6':
                        new_url += ALPHA[ALPHA.index(url[x+2])+9]
                        x += 3
                    elif url[x+1]=='7':
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
        if x+2<len(new_url):
            if new_url[x+1]=='.' and new_url[x+2]=='/':
                n = new_url[:x-1].rfind('/')
                repl = new_url[n+1:x+3]
                new_url = new_url.replace(repl, '', 1)
            else:
                y = x+1
        else:
            if new_url[x+1]=='.':
                n = new_url[:x-1].rfind('/')
                repl = new_url[n+1:]
                new_url = new_url.replace(repl, '', 1)
                if new_url[-1]=='/':
                    new_url = new_url[:-1]
            else:
                y = x+1

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


checkio = lambda x: x==x[::-1]

print(checkio("asd"))

