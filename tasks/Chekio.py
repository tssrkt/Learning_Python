def split_pairs(a):
    # your code here
    b = []
    for x in range(0, len(a), 2):
        if x == len(a) - 1:
            b.append(a[x] + '_')
        else:
            b.append(a[x] + a[x + 1])
    return b


##############################

def nearest_value(values: set, one: int):
    # your code here
    if len(values) == 1:
        return one

    z = one
    if max(values) > one:
        z = max(values)

    if abs(min(values)) > one:
        z = abs(min(values))

    for x in range(1, z):
        if one in values:
            return one
        elif (one - x) in values:
            return one - x
        elif (one + x) in values:
            return one + x


############################

def format_namelist(a):
    if not a:
        return ''

    names = []
    for x in a:
        names.append(x.get('name'))

    res = ''
    for x in range(len(names)):
        if len(names)==1 or x == 0:
            res += names[x]
        elif len(names) - x == 1:
            res += ' и ' + names[x]
        else:
            res += ', ' + names[x]
    return res

############################

def print_goods(*args):
    if len(args)==0:
        print('Нет товаров')
    else:
        num = 1
        for x in args:
            if type(x)==str and x!='':
                print(f'{num}. {x}')
                num+=1
        if num==1:
            print('Нет товаров')

############################

def left_join(a: tuple):
    """
    Join strings and replace "right" to "left"
    """
    res = []
    n = 0
    for x in a:
        while 'right' in x:
            n = x.find('right')
            x = x[:n] + 'left' + x[n+5:]
        res.append(x)
    s = ''
    n = 0
    for x in res:
        if n==len(res)-1:
            s += x
        else:
            s += x + ','
        n += 1
    return s

lorem = ["lorem","ipsum","dolor","sit","amet","consectetuer","adipiscing","elit","aenean","commodo","ligula","eget","dolor","aenean","massa","cum","sociis","natoque","penatibus","et","magnis","dis","parturient","montes","nascetur","ridiculus","mus","donec","quam","felis","ultricies","nec","pellentesque","eu","pretium","quis","sem","nulla","consequat","massa","quis"]

#################################

def first_word(text: str):
    """
        returns the first word in a given text.
    """
    from string import punctuation
    punk = punctuation.replace("'", '')
    for x in text:
        if x.isalpha():
            break
        elif x in punk:
            text = text.replace(x, '')

    s = list(text.split())[0]

    for x in s:
        if x in punk or x==' ':
            s = list(text.split(x))[0]
    return s

#################################

def days_diff(a, b):
    import datetime
    d1 = datetime.date(a[0], a[1], a[2])
    d2 = datetime.date(b[0], b[1], b[2])
    res = d1 - d2
    return abs(res.days)

#################################

def backward_string_by_word(text: str) -> str:
    import re
    return re.sub(r'[a-zA-Z]+', lambda x : x.group()[::-1], text)
    # Переворачивает слова, оставляя порядок слов и пунктуацию прежними

#################################

def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    mxs = []
    prices = []

    for x in data:
        prices.append(x['price'])

    for x in range(limit):
        m = max(prices)
        mxs.append(m)
        del prices[prices.index(max(prices))]

    res = []
    for y in mxs:
        for x in data:
            if x['price']==y:
                res.append(x)

    return res

# print(bigger_price(2, [
#         {"name": "bread", "price": 100},
#         {"name": "wine", "price": 138},
#         {"name": "meat", "price": 15},
#         {"name": "water", "price": 1}
#     ]))


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    res = ''

    if (begin not in text) and (end not in text):
        return text
    elif (begin not in text) and (end in text):
        res = text.split(end)[0]

    elif (begin in text) and (end not in text):
        res = text.split(begin)[1]

    elif (begin in text) and (end in text):
        b = text.find(begin)
        e = text.find(end)
        if b > e:
            return ''

        res = text.split(begin)[1]
        res = res.split(end)[0]

    return res

# print(between_markers("No [b]hi","[b]","[/b]"))

def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    if text.count(symbol)<2:
        return None
    else:
        import re
        res = [m.start() for m in re.finditer(symbol, text)]
        return res[1]

######################################

def frequency_sort(items):
    res = sorted(items, key=lambda x: items.count(x), reverse=True)

    d = {}
    for x in items:
        if x not in d.keys():
            d[x] = items.count(x)

    v = list(d.values())
    for x in v:
        if v.count(x) > 1:
            res = sorted(res, key=lambda x: items.index(x))

    return res

# print(frequency_sort([4,6,2,2,6,4,4,4]))

def safe_pawns(pawns: set) -> int:
    desk = []
    for x in range(8):
        desk.append([0]*8)

    d = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}

    pawns = list(pawns)
    for x in pawns:
        desk[abs(int(x[1])-8)][d.get(x[0])] = 1

    res = 0
    for y in range(8):
        if sum(desk[y])==0:
            continue
        elif y<7:
            for x in range(8):
                if desk[y][x]==1:
                    if 0<x<7 and (desk[y+1][x-1]==1 or desk[y+1][x+1]==1):
                        res+=1
                    elif x==0 and desk[y+1][x+1]==1:
                        res+=1
                    elif x==7 and desk[y+1][x-1]==1:
                        res+=1

    # for x in desk:
    #     print(x)

    return res

# print(safe_pawns(["a2","b2","c2","d2","e2","f2","g2","h2"]))

def words_order(text: str, words: list) -> bool:
    if len(words)>=2 and words[0]==words[1]:
        return False

    text = text.split()
    w = []
    for x in text:
        if x in words:
            w.append(x)
    if w==words:
        return True
    return False

# print(words_order("hi world im here",["world"]))

def checkio(number: int) -> int:
    s = (str(number)).replace('0', '')
    res = 1
    for x in s:
        res *= int(x)
    return res

# print(checkio(123405))

def is_all_upper(text: str) -> bool:
    text = text.replace(' ', '')
    if text=='' or text.isdigit() or text.islower():
        return False
    else:
        for x in text:
            if x.islower():
                return False
    return True

# print(is_all_upper("ALL UPPER"))

from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
    srt = sorted(items)
    if srt==items:
        return True
    return False

# print(is_ascending([-5,10,99,123456]))


def goes_after(word: str, f: str, s: str) -> bool:
    if f == s or f not in word or s not in word:
        return False

    f = int(word.index(f))
    s = int(word.index(s))
    if f==s-1:
        return True
    return False

# print(goes_after("world","d","w"))

def translate(text: str) -> str:
    vowels = 'aeiouy'
    res = ''
    x = 0
    while x < len(text):
        if text[x] == ' ':
            res += text[x]
            x += 1
            continue
        elif text[x] in vowels:
            if x > 0 and text[x - 1] not in vowels and text[x-1]!=' ':
                x += 1
                continue
            elif x < len(text) - 2 and text[x] == text[x + 1] == text[x + 2]:
                res += text[x]
                x += 3
        else:
            res += text[x]
            x += 1
    return res

# print(translate("hieeelalaooo")) # == "hello"
# print(translate("hoooowe yyyooouuu duoooiiine")) # == "how you doin"
# print(translate("aaa bo cy da eee fe")) # == "a b c d e f"
# print(translate("sooooso aaaaaaaaa")) # == "sos aaa"
# print("Coding complete? Click 'Check' to earn cool rewards!")


def checkio(s1: str, s2: str) -> str:
    s1 = s1.split(',')
    s2 = s2.split(',')
    a = []
    res = ''
    for x in s1:
        if s2.count(x) >= 1:
            a.append(x + ',')

    a.sort()

    for x in a:
        res += x

    if len(res) != 0 and res[-1] == ',':
        res = res[:-1]

    return res

# print(checkio(["one,two,three","four,five,one,two,six,three"]))
import string

def check_pangram(text):
    '''
        is the given text is a pangram.
    '''
    s = list(map(str, string.ascii_letters[:26]))
    text = text.lower()

    if len(text) > 0:
        for x in range(26):
            if s[x] not in text:
                return False
    return True

# print(check_pangram("The quick brown fox jumps over the lazy dog."))

def checkio(text: str) -> str:
    text = text.lower()
    s = [x for x in text if x.isalpha()]
    mx = {}
    for x in s:
        if x in mx.keys():
            mx[x] += 1
        else:
            mx.setdefault(x, 1)
    mx_lst = mx.values()
    res = []
    res = [k for k,v in mx.items() if v == max(mx_lst)]
    res = sorted(res, key=str.lower)

    return res[0]

# print(checkio("Lorem ipsum dolor sit amet"))

def checkio(text, word):
    a = list(text.replace(' ', '').lower().split('\n'))
    for x in a:
        n = a.index(x)
        if word in x:
            y1=x.find(word)+1
            y2=y1+len(word)-1
            return ([n+1, y1, n+1, y2])

    for x in a[:-1]:
        n = a.index(x)
        for y in range(len(x)):
            if x[y] == word[0] and len(word) <= (len(a) - n):
                for z in range(1, len(word)+1):
                    q = a[n + z][y]
                    q1 = word[z]
                    if z<len(word) and a[n + z][y] == word[z]:
                        if z == len(word)-1:
                            return [n+1, y+1, n + z+1, y+1]
                        continue
                    else:
                        break
    return None

# print(checkio("DREAMING of apples on a wall,\nAnd dreaming often, dear,\nI dreamed that, if I counted all,\n-How many would appear?","ten"))
# checkio("He took his vorpal sword in hand:\nLong time the manxome foe he sought--\nSo rested he by the Tumtum tree,\nAnd stood awhile in thought.\nAnd as in uffish thought he stood,\nThe Jabberwock, with eyes of flame,\nCame whiffling through the tulgey wood,\nAnd burbled as it came!","noir")
# checkio("Twas brillig, and the slithy toves\nDid gyre and gimble in the wabe;\nAll mimsy were the borogoves,\nAnd the mome raths outgrabe.","stog")

def find_quotes(a):
    s = ''
    res = []
    n = 0
    x = 0
    while x < len(a):
        if a[x]=='"' and a[x+1]=='"':
            res.append('""')
            x +=2
            continue
        elif a[x] == '"' and n == 0:
            n = 1
            x += 1
        elif a[x] != '"' and n == 0:
            x += 1
            continue

        if a[x] != '"' and n == 1:
            n = x
            for z in a[n:]:
                if z != '"':
                    s += z
                else:
                    res.append(s)
                    x += len(s) + 1
                    n = 0
                    s = ''
                    break
        x+=1

    return res

# print(find_quotes("count empty quotes \"\""))
# print(find_quotes('"Greetings"'))

def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    res = 1
    a = []
    for x in range(len(line[:-1])):
        if line[x] == line[x+1]:
            res += 1
        else:
            a.append(res)
            res = 1

    return max(a)

# print(long_repeat("ddvvrwwwrggg"))

dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def d(x):
    return dic.get(x)

def roman(s, res):
    n = len(s)
    res += d(s[0])

    if n == 0:
        return 1
    elif n == 1:
        return res
    elif n==2:
        if d(s[0])>=d(s[1]):
            res += d(s[0])+d(s[1])
        else:
            res += d(s[1])-d(s[0])

    if n>4:
        n=4

    same = 1
    for x in range(1, n):
        num=s[x]

        if d(s[x]) == d(s[x - 1]):
            res += d(s[x])
            same+=1
        elif d(s[x]) < d(s[x-1]) and same==3:
            s = s[3:]
            return roman(s, res)
        elif d(s[x]) > d(s[x-1]) and same==3:
            res=0
            res+=d(s[x])-d(s[x-1])*3
        else:
            res -= d(s[x - 1])
    s=s[4:]
    return roman(s, res)


def reverse_roman(s):
    res = roman(s, 0)
    return res

# print(reverse_roman("MMMDCCCX"))
# print(reverse_roman("MMCCCXLVI"))
# print(reverse_roman("MMMCMXCIX"))

def isometric_strings(a, b):
    for x in range(len(a)):
        if a[x].isalpha():
            a=a.replace(a[x], str(x))
        if b[x].isalpha():
            b=b.replace(b[x], str(x))
        if a==b:
            return True
    return False

# print(isometric_strings("bar","foo"))

d = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
     7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}


def date_time(time: str) -> str:
    h = 'hours'
    m = 'minutes'

    day = str(int(time[:2]))
    month = d.get(int(time[3:5]))
    year = time[6:10]
    hours = str(int(time[11:13]))
    mins = str(int(time[-2] + time[-1]))

    if hours=='1':
        h='hour'
    if mins=='1':
        m = 'minute'

    res = f"{day} {month} {year} year {hours} {h} {mins} {m}"
    return res

# print(date_time("01.01.2000 00:00"))

def yaml(a):
    d = {}
    a = a.split()
    v = ''
    lk = []
    lv = []
    for x in a:
        if ':' in x:
            if a.index(x)>0 and a[a.index(x)-1].count(':')>0:
                v = None
            if v=='false':
                lv.append(False)
                v = ''
            elif v=='true':
                lv.append(True)
                v = ''
            elif v!='':
                lv.append(v)
                v = ''
            lk.append(x[:-1])
        else:
            v = v + ' ' + x

    if v!='':
        lv.append(v)
        v=''

    for x in range(len(lk)):
        y = lv[x].strip().replace('\\', '')
        if y.isdigit():
            y = int(y)
        else:
            y = y.replace('"', '')

        print(y)

        d.setdefault(lk[x], y)

    return d

# print(yaml("name: Alex\nage: 12"))
# print(yaml("name: Alex Fox\nage: 12\n\nclass: 12b"))
# print(yaml("name: \"Bob Dylan\"\nchildren: 6\nalive: false"))

def checkio(a) -> str:
    res = ['O', 'X', 'D']
    d = 0

    for x in range(len(a)):
        w = 0
        while w < 2:
            if a[x].count(res[w]) == 3 or a[0][x] == a[1][x] == a[2][x] == res[w]:
                return res[w]
            if a[0][0] == a[1][1] == a[2][2] == res[w] or a[0][2] == a[1][1] == a[2][0] == res[w]:
                return res[w]
            w += 1

    return "D"

# print(checkio(["OO.","XOX","XOX"]))

def split_list(items: list) -> list:
    if items==[]:
        return [[], []]
    x = len(items)//2 if len(items)%2==0 else len(items)//2+1
    return [items[:x], items[x:]]

# print(split_list([1, 2, 3, 4, 5, 6]))

MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code):
    res = ''
    word = ''
    words = code.split('   ')
    for x in words:
        x = x.split()
        for y in x:
            word+=MORSE.get(y)
        res += word + ' '
        word = ''
    res = res.capitalize()
    return res

# print(morse_decoder("... --- -- .   - . -..- -"))

def checkio(line: str) -> str:
    vowels = 'A E I O U Y'.lower().split()
    cons = 'B C D F G H J K L M N P Q R S T V W X Z'.lower().split()
    a = line.lower().split()

    my_even = ''
    my_odd = ''
    res = 0
    b = []

    if ',' in line or '.' in line:
        for x in a:
            x = x.split(',')
            if type(x) == list:
                b += x
            else:
                b.append(x)

        a = b[:]
        b = []
        for x in a:
            x = x.split('.')
            if type(x) == list:
                b += x
            else:
                b.append(x)

    else:
        b = a[:]

    from string import punctuation
    for w in b:
        for x in w:
            if x in punctuation:
                b[b.index(w)] = w.replace(x, "")

    b = [x for x in b if x.isalpha()]
    a = []

    for w in b:
        if len(w) == 1:
            continue

        for x in range(len(w)):
            if (x + 1) % 2 == 0:
                my_even += w[x]
            else:
                my_odd += w[x]

        v = True
        c = True
        if my_even != '' and my_odd!='' and my_even[0] in vowels and my_odd[0] in cons:
            for x in my_even:
                if x not in vowels:
                    v = False
                    break
            for x in my_odd:
                if x not in cons:
                    c = False
                    break
        elif my_even != '' and my_odd!='' and my_even[0] in cons and my_odd[0] in vowels:
            for x in my_even:
                if x not in cons:
                    c = False
                    break
            for x in my_odd:
                if x not in vowels:
                    v = False
                    break
        else:
            c = False
            v = False

        if c == True and v == True:
            res += 1

        my_even = ''
        my_odd = ''

    return res

# print(checkio("My name is ..."))
# print(checkio("A quantity of striped words."))
# print(checkio("Dog,cat,mouse,bird.Human."))
# print(checkio("To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?"))
# print(checkio("1st 2a ab3er root rate"))

def binar_morze(n):
    if n=='0':
        return '.'

    n = int(n)
    a = [1]
    while a[-1]<=n:
        a.append(a[-1]*2)
        if a[-1] > n:
            del a[-1]
            break

    a = a[::-1]
    res = ''
    sm = 0
    for x in a:
        if a.index(x)==0 or sm+x<=n:
            sm += x
            res += '-'
        elif sm+x>n:
            res +='.'
    return res

def checkio(time_string: str) -> str:
    a = time_string.split(':')
    res = ''
    nums = [2,4,3,4,3,4]
    i = 0

    for x in a:
        if len(x)<=1:
            a[a.index(x)]='0'+x

    zuka = 0
    for x in a:
        for n in x:
            bm = binar_morze(n)
            bm = '.'*(nums[i] - len(bm)) + bm
            res += bm + ' '
            i+=1
        if zuka<2:
            res += ': '
        zuka += 1
    res = res.strip()
    return res

# print(checkio("10:37:49"))
# print(checkio("00:1:02"))
# print(checkio("23:59:59"))

from typing import List
import math

def total_cost(calls: List[str]) -> int:
    a = []
    for x in calls:
        if calls.index(x) == 0:
            a.append(math.ceil((int(x.split()[-1])/ 60)))
        else:
            if x[8:10] == calls[calls.index(x) - 1][8:10]:
                a[-1] += int(math.ceil((int(x.split()[-1])/ 60)))
            else:
                a.append(int(math.ceil((int(x.split()[-1])/ 60))))

    res = 0
    for x in a:
        if x <= 100:
            res += x
        else:
            res += 100 + (x - 100) * 2

    return res

# print(total_cost(["2014-01-01 01:12:13 181","2014-01-02 20:11:10 600","2014-01-03 01:12:13 6009","2014-01-03 12:13:55 200"]))

class Warrior:
    health = 50
    attack = 5

    def is_alive(self):
        if self.health > 0:
            return True
        return False


class Knight(Warrior):
    attack = 7


def fight(unit_1, unit_2):
    while unit_1.is_alive() and unit_2.is_alive():
        unit_2.health -= unit_1.attack

        if unit_2.is_alive():
            unit_1.health -= unit_2.attack

    if unit_1.is_alive() and not unit_2.is_alive():
        return True
    return False

carl = Warrior()
jim = Knight()
# print(fight(carl, jim))

bob = Warrior()
mars = Warrior()
# print(fight(bob, mars))

def flat_list(a, neo=None):
    if a == []:
        return []

    for x in a:
        if neo is None:
            neo = []
        if type(x) == list:
            neo = neo + flat_list(x)
        else:
            neo.append(x)
    return neo

# print(flat_list([-1, [1, [-2], 1], -1]))

def how_deep(structure, res=1):
    for x in structure:
        if isinstance(x, (tuple, list, set)):
            res+=1
            res = how_deep(x, res)
    return res

# print(how_deep([1,2,[3,[4]]]))

def checkio(n):
    fed = 0
    pigs = 0
    fd = n

    for x in range(1, n + 1):
        if pigs >= fd:
            break

        if x <= (fd-pigs):
            fed += x
        else:
            fed += (fd-pigs)

        pigs += x
        fd -= pigs

        if fd <= 0:
            break
    return fed

# print(checkio(3))
# print(checkio(5))

def clock_angle(time):
    hour, minute = map(int, time.split(':'))
    ans = abs((hour * 30 + minute * 0.5) - (minute * 6))
    return abs(min(360 - ans, ans))

# print(clock_angle("02:30")) # == 105, "02:30"
# print(clock_angle("13:42")) # == 159, "13:42"
# print(clock_angle("01:42")) # == 159, "01:42"
# print(clock_angle("01:43")) # == 153.5, "01:43"
# print(clock_angle("00:00")) # == 0, "Zero"
# print(clock_angle("12:01")) # == 5.5, "Little later"
# print(clock_angle("18:00")) # == 180, "Opposite"

def create_zigzag(rows: int, cols: int, start: int = 1) -> List[List[int]]:
    res = []
    is_evn = 0

    for x in range(rows):
        res.append([])
        for y in range(cols):
            res[-1].append(start)
            start += 1
        if is_evn == 1:
            a = res[-1]
            res[-1] = a[::-1]
            is_evn = 0
        else:
            is_evn = 1
    return res

# print(create_zigzag(3,5))

def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    if len(line) == 1 or (len(line) == 2 and line[0]!=line[1]):
        return line

    res = []
    n = 0

    for x in range(1, len(line)):
        if line[n:x].count(line[x]) > 0:
            res.append(line[n:x])
            n = x
        elif x == len(line) - 1 and res == []:
            res.append(line)

    res = sorted(res, key=len)
    if res != []:
        return res[-1]
    return ''

# print(non_repeat("abcabcffab"))
# print(non_repeat("wq"))
# print(non_repeat("dfghj"))

def checkio(words_set):
    for x in words_set:
        res = 0
        for y in words_set:
            if x in y and x[-1]==y[-1]:
                res += 1
        if res>1:
            return True
    return False

# print(checkio(["hello","la","hellow","cow"]))

def highest_building(*b):
    n = len(b)
    m = len(b[0])
    a = []
    for x in range(m):
        z = 0
        for y in range(n):
            z += b[y][x]
        a.append(z)

    return [a.index(max(a))+1, max(a)]

# print(highest_building([0,0,1,0],[1,0,1,0],[1,1,1,0],[1,1,1,1]))
# print(highest_building([0,0,0,1,0,0,0],[0,0,1,1,1,0,0],[0,1,1,1,1,1,0],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]))
# print(highest_building([0,0,1,0],[1,0,1,0],[1,1,1,0],[1,1,1,1]))





def checkio(s, s2=''):
    a = [s.count('(') - s.count(')'), s.count('[') - s.count(']'), s.count('{') - s.count('}')]
    b = ['(', '[', '{']
    c = [')', ']', '}']
    d = c + b

    if s2!='':
        s = s2

    zuzuka = True
    for x in d:
        if x in s:
            zuzuka = False
            break
    if zuzuka == True:
        return True

    for x in range(len(a)):
        if a[x] != 0:
            return False

    res = True
    for x in range(len(s)):
        if s[x] in b:
            z = b.index(s[x])
            n = s.rfind(c[z])
            s2 = s[x + 1:n]
            res = checkio(s, s2)

    return res

# print(checkio("((5+3)*2+1)"))
# print(checkio("(3+{1-1)}"))


def sm(a, b, x, costs):
    res = []
    for y in x:
        if y != a and isinstance(y, str):
            for z in costs:
                if y in z and b in z:
                    res.append(costs[costs.index(z)][-1]+costs[costs.index(x)][-1])
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

        if next=='' and a in x and b not in x:
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

    if prices==[]:
        return 0

    return min(prices)

# print(cheapest_flight([["A","C",40],["A","B",20],["A","D",20],["B","C",50],["D","C",70]],"D","C"))
# print(cheapest_flight([["A","C",100],["A","B",20],["D","F",900]],"A","F"))
# print(cheapest_flight([["A","C",40],["A","B",20],["A","D",20],["B","C",50],["D","C",70]],"D","C"))
# print(cheapest_flight([["A","B",10],["A","C",15],["B","D",15],["C","D",10]],"A","D"))
# print(cheapest_flight([["A","B",10],["A","C",20],["B","D",15],["C","D",5],["D","E",5],["E","F",10],["C","F",25]],"A","F"))

# OOP
print()
print('*'*50)
print('OOP')

class VoiceCommand():

    def __init__(self, *args):
        self.channels = args

    # переключается на первый канал из списка
    def first_channel(self):
        pass

    # переключается на последний канал из списка.
    def last_channel(self):
        pass

    # переключается на канал номер n. Нумерация каналов начинается с 1, а не с 0.
    def turn_channel(self, n):
        self.n = n

    # переключается на следующий канал. Если текущий канал - последний, то - на первый канал.
    def next_channel(self):
        pass

    # переключается на предыдущий канал. Если текущий канал - первый, то - на последний канал.
    def previous_channel(self):
        pass

    # возвращает название текущего канала.
    def current_channel(self):
        pass

    # принимает 1 аргумент - число N или строку 'name' и возвращает "Yes", если канал
    # с номером N или названием 'name' существует в списке и "No" в ином случае.
    # def is_exist(self, n, name):
    #     pass

"""
По умолчанию до начала работы всех команд включен канал №1.
Ваша задача - создать класс VoiceCommand и методы, описанные ранее.
В этой миссии вам может помочь такой шаблон проектирования, как Iterator .
"""

CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = VoiceCommand(CHANNELS)

controller.first_channel() # == "BBC"
controller.last_channel() # == "TV1000"
controller.turn_channel(1) # == "BBC"
controller.next_channel() # == "Discovery"
controller.previous_channel() # == "BBC"
controller.current_channel() # == "BBC"
# controller.is_exist(4) # == "No"
# controller.is_exist("BBC") # == "Yes"

