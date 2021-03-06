def is_even(num: int) -> bool:
    # return not num%2
    return not num & 1


# print(is_even(2))  # == True
# print(is_even(5))  # == False
# print(is_even(0))  # == True


def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    text = text[0].upper() + text[1:]
    return text + '' if text.endswith('.') else text + '.'


# print(correct_sentence("greetings, friends"))  # == "Greetings, friends."
# print(correct_sentence("Greetings, friends"))  # == "Greetings, friends."
# print(correct_sentence("Greetings, friends."))  # == "Greetings, friends."
# print(correct_sentence("hi"))  # == "Hi."
# print(correct_sentence("welcome to New York"))  # == "Welcome to New York."

from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    return items[items.index(border):] if border in items else items


# print(remove_all_before([1, 2, 3, 4, 5], 3))  # == [3, 4, 5]
# print(remove_all_before([1, 1, 2, 2, 3, 3], 2))  # == [2, 2, 3, 3]
# print(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2))  # == [2, 4, 2, 3, 4]
# print(remove_all_before([1, 1, 5, 6, 7], 2))  # == [1, 1, 5, 6, 7]
# print(remove_all_before([], 0))  # == []
# print(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7))  # == [7, 7, 7, 7, 7, 7, 7, 7, 7]


def end_zeros(num: int) -> int:
    return len(str(num)) - len(str(num).rstrip('0'))


# print(end_zeros(0))  # == 1
# print(end_zeros(1))  # == 0
# print(end_zeros(10))  # == 1
# print(end_zeros(101))  # == 0
# print(end_zeros(245))  # == 0
# print(end_zeros(100100))  # == 2


def split_pairs(a):
    # return [''.join(x) for x in zip(a[::2], a[1::2] + '_')]
    return [a + b for a, b in zip(a[::2], a[1::2] + '_')]


# print(split_pairs('abcd'))  # == ['ab', 'cd']
# print(split_pairs('abc'))  # == ['ab', 'c_']
# print(split_pairs('abcdf'))  # == ['ab', 'cd', 'f_']
# print(split_pairs('a'))  # == ['a_']
# print(split_pairs(''))  # == []


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
        if len(names) == 1 or x == 0:
            res += names[x]
        elif len(names) - x == 1:
            res += ' ?? ' + names[x]
        else:
            res += ', ' + names[x]
    return res


############################

def print_goods(*args):
    if len(args) == 0:
        print('?????? ??????????????')
    else:
        num = 1
        for x in args:
            if type(x) == str and x != '':
                print(f'{num}. {x}')
                num += 1
        if num == 1:
            print('?????? ??????????????')


############################

def left_join(a: tuple):
    """
    Join strings and replace "right" to "left"
    """
    return ','.join(a).replace('right', 'left')


# print(left_join(("left", "right", "left", "stop")))
# print(left_join(("left", "right", "left", "stop")))  # == "left,left,left,stop"
# print(left_join(("bright aright", "ok")))  # == "bleft aleft,ok", "Bright Left"
# print(left_join(("brightness wright",)))  # == "bleftness wleft", "One phrase"
# print(left_join(("enough", "jokes")))  # == "enough,jokes", "Nothing to replace"


lorem = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetuer", "adipiscing", "elit", "aenean", "commodo", "ligula",
         "eget", "dolor", "aenean", "massa", "cum", "sociis", "natoque", "penatibus", "et", "magnis", "dis",
         "parturient", "montes", "nascetur", "ridiculus", "mus", "donec", "quam", "felis", "ultricies", "nec",
         "pellentesque", "eu", "pretium", "quis", "sem", "nulla", "consequat", "massa", "quis"]


#################################

def first_word(text: str):
    """
        returns the first word in a given text.
    """
    return ([x for x in text.replace('.', ' ').replace(',', '').split() if x[0].isalpha()])[0]


# print(first_word("Hello world"))  # == "Hello"
# print(first_word(" a word "))  # == "a"
# print(first_word("don't touch it"))  # == "don't"
# print(first_word("greetings, friends"))  # == "greetings"
# print(first_word("... and so on ..."))  # == "and"
# print(first_word("hi"))  # == "hi"
# print(first_word("Hello.World"))  # == "Hello"


#################################

def days_diff(a, b):
    import datetime
    d1 = datetime.date(a[0], a[1], a[2])
    d2 = datetime.date(b[0], b[1], b[2])
    res = d1 - d2
    return abs(res.days)


#################################

def backward_string_by_word(text: str) -> str:
    return ' '.join([x[::-1] for x in text.split()])


# print(backward_string_by_word(''))  # == ''
# print(backward_string_by_word('world'))  # == 'dlrow'
# print(backward_string_by_word('hello world'))  # == 'olleh dlrow'
# print(backward_string_by_word('hello   world'))  # == 'olleh   dlrow'
# print(backward_string_by_word('welcome to a game'))  # == 'emoclew ot a emag')


#################################


def count_digits(text: str) -> int:
    # return len([x for x in text if x.isdigit()])
    return sum(map(str.isdigit, text))


# print(count_digits('hi'))  # == 0
# print(count_digits('who is 1st here'))  # == 1
# print(count_digits('my numbers is 2'))  # == 1
# print(count_digits('This picture is an oil on canvas '
#  'painting by Danish artist Anna '
#  'Petersen between 1845 and 1910 year'))  # == 8
# print(count_digits('5 plus 6 is'))  # == 2
# print(count_digits(''))  # == 0)


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
            if x['price'] == y:
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
    if begin in text and end in text and text.find(begin) > text.find(end): return ''
    return text[text.find(begin) if begin in text else 0:text.find(end) if end in text else None].replace(begin, '')


# print(between_markers("No [b]hi","[b]","[/b]"))
# print(between_markers('What is >apple<', '>', '<'))  # == "apple", "One sym"
# print(between_markers("<head><title>My new site</title></head>",
#                            "<title>", "</title>"))  # == "My new site", "HTML"
# print(between_markers('No[/b] hi', '[b]', '[/b]'))  # == 'No', 'No opened'
# print(between_markers('No [b]hi', '[b]', '[/b]'))  # == 'hi', 'No close'
# print(between_markers('No hi', '[b]', '[/b]'))  # == 'No hi', 'No markers at all'
# print(between_markers('No <hi>', '>', '<'))  # == '', 'Wrong direction'


def second_index(text: str, s: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    import re
    return [m.start() for m in re.finditer(s, text)][1] if text.count(s) >= 2 else None


# print(second_index("sims", "s"))  # == 3, "First"
# print(second_index("find the river", "e"))  # == 12, "Second"
# print(second_index("hi", " "))  # is None, "Third"
# print(second_index("hi mayor", " "))  # is None, "Fourth"
# print(second_index("hi mr Mayor", " "))  # == 5, "Fifth")


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
            res = sorted(res, key=lambda x: res.count(x))

    return res


# print(frequency_sort([4,6,2,2,6,4,4,4]))


def safe_pawns(pawns: set) -> int:
    desk = [[0] * 8 for _ in range(8)]
    d = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

    for x in list(pawns):
        desk[abs(int(x[1]) - 8)][d.get(x[0])] = 1

    res = 0
    for y in range(7):
        if sum(desk[y]) != 0:
            for x in range(8):
                if desk[y][x] == 1:
                    if 0 < x < 7 and (desk[y + 1][x - 1] or desk[y + 1][x + 1]) or \
                            x == 0 and desk[y + 1][x + 1] or x == 7 and desk[y + 1][x - 1]:
                        res += 1
    return res


# print(safe_pawns(["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"]))
# print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))  # == 6
# print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))  # == 1
# print(safe_pawns(["e4"]))  # 0,
# print(safe_pawns(["e8"]))  # 0,
# print(safe_pawns(["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"]))  # 7,
# print(safe_pawns(["a8", "b7", "c6", "d5", "e4", "f3", "g2", "h1"]))  # 7,
# print(safe_pawns(["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"]))  # 7,
# print(safe_pawns(["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"]))  # 0,
# print(safe_pawns(["a1", "a2", "a3", "a4", "h1", "h2", "h3", "h4"]))  # 0,
# print(safe_pawns(["b4", "c4", "d4", "e4", "f4", "g4", "e3"]))  # 2,
# print(safe_pawns(["e7", "e6", "d5", "f5", "c4", "e4", "g4", "e8"]))  # 3,
# print(safe_pawns(["a2", "b4", "c6", "d8", "e1", "f3", "g5", "h8"]))  # 0,
# print(safe_pawns(["b6", "a7", "b8", "c7", "g1", "f2", "h2", "g3"]))  # 6,


def words_order(text: str, words: list) -> bool:
    if len(words) >= 2 and words[0] == words[1]:
        return False

    text = text.split()
    w = []
    for x in text:
        if x in words:
            w.append(x)
    if w == words:
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
    return text == text.upper()


# print(is_all_upper("ALL UPPER"))
# print(is_all_upper('ALL UPPER'))  # == True
# print(is_all_upper('all lower'))  # == False
# print(is_all_upper('mixed UPPER and lower'))  # == False
# print(is_all_upper(''))  # == True
# print(is_all_upper('     '))  # == True
# print(is_all_upper('444'))  # == True
# print(is_all_upper('55 55 5'))  # == True

from time import time
from typing import Iterable
def is_ascending(items: Iterable[int]) -> bool:
    return items==sorted(items) and len(set(items))==len(items)
    # return all(a < b for a, b in zip(items, items[1:]))
    # return all(items[i] < items[i + 1] for i in range(len(items) - 1))
    # return all(items[i - 1] < items[i] for i in range(1, len(items)))  # 0.53

# ???????????????? ???????????????????? ??????????????????
st_time, n, lst = time(), 999999, list(range(20))
for i in range(n):
    x = is_ascending(lst)
print(f'{n} iterations, {time() - st_time:.3f} seconds')

# print(is_ascending([-5,10,99,123456]))
# print(is_ascending([1, 2, 2, 3]))


# good solution! but it isn???t speedy )
# you may use all + (comprehension + zip or comprehension + range)


def goes_after(word: str, f: str, s: str) -> bool:
    if f == s or f not in word or s not in word:
        return False

    f = int(word.index(f))
    s = int(word.index(s))
    if f == s - 1:
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
            if x > 0 and text[x - 1] not in vowels and text[x - 1] != ' ':
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
    res = [k for k, v in mx.items() if v == max(mx_lst)]
    res = sorted(res, key=str.lower)

    return res[0]


# print(checkio("Lorem ipsum dolor sit amet"))

def checkio(text, word):
    a = list(text.replace(' ', '').lower().split('\n'))
    for x in a:
        n = a.index(x)
        if word in x:
            y1 = x.find(word) + 1
            y2 = y1 + len(word) - 1
            return ([n + 1, y1, n + 1, y2])

    for x in a[:-1]:
        n = a.index(x)
        for y in range(len(x)):
            if x[y] == word[0] and len(word) <= (len(a) - n):
                for z in range(1, len(word) + 1):
                    q = a[n + z][y]
                    q1 = word[z]
                    if z < len(word) and a[n + z][y] == word[z]:
                        if z == len(word) - 1:
                            return [n + 1, y + 1, n + z + 1, y + 1]
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
        if a[x] == '"' and a[x + 1] == '"':
            res.append('""')
            x += 2
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
        x += 1

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
        if line[x] == line[x + 1]:
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
    elif n == 2:
        if d(s[0]) >= d(s[1]):
            res += d(s[0]) + d(s[1])
        else:
            res += d(s[1]) - d(s[0])

    if n > 4:
        n = 4

    same = 1
    for x in range(1, n):
        num = s[x]

        if d(s[x]) == d(s[x - 1]):
            res += d(s[x])
            same += 1
        elif d(s[x]) < d(s[x - 1]) and same == 3:
            s = s[3:]
            return roman(s, res)
        elif d(s[x]) > d(s[x - 1]) and same == 3:
            res = 0
            res += d(s[x]) - d(s[x - 1]) * 3
        else:
            res -= d(s[x - 1])
    s = s[4:]
    return roman(s, res)


def reverse_roman(s):
    res = roman(s, 0)
    return res


# print(reverse_roman("MMMDCCCX"))
# print(reverse_roman("MMCCCXLVI"))
# print(reverse_roman("MMMCMXCIX"))

def isometric_strings(a, b):
    if a == b or a == b == '':
        return True

    for x in range(len(a)):
        if a[x].isalpha():
            a = a.replace(a[x], str(x))
        if b[x].isalpha():
            b = b.replace(b[x], str(x))
        if a == b:
            return True
    return False


# print(isometric_strings("bar","foo"))
# print(isometric_strings("add", "egg"))  # == True
# print(isometric_strings("foo", "bar"))  # == False
# print(isometric_strings("", ""))  # == True
# print(isometric_strings("all", "all"))  # == True
# print(isometric_strings("gogopy", "doodle"))  # == False


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

    if hours == '1':
        h = 'hour'
    if mins == '1':
        m = 'minute'

    res = f"{day} {month} {year} year {hours} {h} {mins} {m}"
    return res


# print(date_time("01.01.2000 00:00"))

def yaml(a):
    d = {}
    for x in a.splitlines():
        if x != '':
            k, v = x.split(':')[0].strip(), x.split(':')[1].strip()
            v = int(v) if v.isdigit() else v
            v = None if v in ['', 'null'] else v
            v = 'null' if v=='\"null\"' else v
            v = v.replace('\"', '').replace('\\', '"') if type(v)==str else v
            v = False if v=='false' else v
            v = True if v=='true' else v
            d[k] = v
    return d

# print(yaml("name: \"Bob Dylan\"\nchildren: 6\ncoding: \"null\" "))
# print(yaml("name: \"Bob Dylan\"\nchildren: 6\ncoding: null"))
# print(yaml("name: \"Bob Dylan\"\nchildren: 6\ncoding:"))
# print(yaml("name: \"Bob Dylan\"\nchildren: 6\nalive: false"))
# print(yaml("name: \"Alex \\\"Fox\\\"\"\nage: 12\n\nclass: 12b"))
# print(yaml("name: \"Alex Fox\"\nage: 12\n\nclass: 12b"))
# print(yaml("name: Alex\nage: 12"))
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
    if items == []:
        return [[], []]
    x = len(items) // 2 if len(items) % 2 == 0 else len(items) // 2 + 1
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
            word += MORSE.get(y)
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
        if my_even != '' and my_odd != '' and my_even[0] in vowels and my_odd[0] in cons:
            for x in my_even:
                if x not in vowels:
                    v = False
                    break
            for x in my_odd:
                if x not in cons:
                    c = False
                    break
        elif my_even != '' and my_odd != '' and my_even[0] in cons and my_odd[0] in vowels:
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


def binm(n):
    return str(bin(int(n))[2:]).replace('1', '-').replace('0', '.')


def checkio(time_string: str) -> str:
    a, b, c, d, e, f = ''.join(['0' + x if len(x) <= 1 else x for x in time_string.split(':')])
    a = binm(a) if len(binm(a)) == 2 else '.' * (2 - len(binm(a))) + binm(a)
    b = binm(b) if len(binm(b)) == 4 else '.' * (4 - len(binm(b))) + binm(b)
    c = binm(c) if len(binm(c)) == 3 else '.' * (3 - len(binm(c))) + binm(c)
    d = binm(d) if len(binm(d)) == 4 else '.' * (4 - len(binm(d))) + binm(d)
    e = binm(e) if len(binm(e)) == 3 else '.' * (3 - len(binm(e))) + binm(e)
    f = binm(f) if len(binm(f)) == 4 else '.' * (4 - len(binm(f))) + binm(f)
    return f'{a} {b} : {c} {d} : {e} {f}'


# print(checkio("10:37:49"))  # == ".- .... : .-- .--- : -.. -..-"
# print(checkio("21:34:56"))  # == "-. ...- : .-- .-.. : -.- .--."
# print(checkio("00:1:02"))  # == ".. .... : ... ...- : ... ..-."
# print(checkio("23:59:59"))  # == "-. ..-- : -.- -..- : -.- -..-"

from typing import List
import math


def total_cost(calls: List[str]) -> int:
    a = []
    for n, x in enumerate(calls):
        if n == 0:
            a.append(math.ceil((int(x[20:]) / 60)))
        else:
            if x[8:10] == calls[n - 1][8:10]:
                a[-1] += int(math.ceil((int(x[20:]) / 60)))
            else:
                a.append(int(math.ceil((int(x[20:]) / 60))))

    return sum([x if x<=100 else 100 + (x - 100) * 2 for x in a])


# print(total_cost(["2014-01-01 01:12:13 181","2014-01-02 20:11:10 600","2014-01-03 01:12:13 6009","2014-01-03 12:13:55 200"]))
# # == 124
# print(total_cost(("2014-02-05 01:00:00 1",
#                        "2014-02-05 02:00:00 1",
#                        "2014-02-05 03:00:00 1",
#                        "2014-02-05 04:00:00 1")))  # == 4



def flat_list(a):
    # neo = []
    # for x in a:
    #     neo.extend(flat_list(x) if type(x) == list else [x])
    # return neo
    for i in a: yield from [i] if i * 0 == 0 else flat_list(i)


# print(list(flat_list([-1, [1, [-2], 1], -1])))  # == [-1, 1, -2, 1, -1]

def how_deep(structure, res=1):
    for x in structure:
        if isinstance(x, (tuple, list, set)):
            if res < 2:
                res += 1
            res = res + how_deep(x) - 1
    return res


# print(how_deep([1,2,[3,[4]]]))

def checkio(n):
    fed = 0
    pigs = 0
    fd = n

    for x in range(1, n + 1):
        if pigs >= fd:
            break

        if x <= (fd - pigs):
            fed += x
        else:
            fed += (fd - pigs)

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


# print(create_zigzag(3, 3, 5))
# print(create_zigzag(3,5))

def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    if len(line) == 1 or (len(line) == 2 and line[0] != line[1]):
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
            if x in y and x[-1] == y[-1]:
                res += 1
        if res > 1:
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

    return [a.index(max(a)) + 1, max(a)]


# print(highest_building([0,0,1,0],[1,0,1,0],[1,1,1,0],[1,1,1,1]))
# print(highest_building([0,0,0,1,0,0,0],[0,0,1,1,1,0,0],[0,1,1,1,1,1,0],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]))
# print(highest_building([0,0,1,0],[1,0,1,0],[1,1,1,0],[1,1,1,1]))


# print(a, len(a))
# print(b, len(b))
# print(a-b, b-a)

from collections import Counter


def verify_anagrams(a, b):
    a = Counter(a.lower().replace(' ', ''))
    b = Counter(b.lower().replace(' ', ''))

    if not a - b and not b - a and len(a) == len(b):
        return True
    return False


# print(verify_anagrams("  Hi  all  ","all hi"))
# print(verify_anagrams("a","abcd"))
# print(verify_anagrams("The Morse Code","There Come Dots"))

def except_zero(items: list) -> Iterable:
    srt = items[:]
    srt.sort()
    srt = [x for x in srt if x > 0]
    res = []
    y = 0
    for x in items:
        if x == 0:
            res.append(0)
        else:
            res.append(srt[y])
            y += 1
    return res


# print(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7]))

def recall_password(gri: List[str], pas: List[str]) -> str:
    res = ''
    for _ in range(4):
        res += ''.join(x for p, g in zip(pas, gri) for x, y in zip(p, g) if y == 'X')
        gri = list(zip(*gri[::-1]))
    return res


# print(recall_password(['X...', '..X.', 'X..X', '....'],  ['itdf', 'gdce', 'aton', 'qrdi']))
# == 'icantforgetiddqd'


def checkio(year: int) -> int:
    """???????????????????? ???????????????????? ???????????? 13 ?? ????????"""
    import calendar
    res = 0
    for x in range(1, 13):
        if calendar.weekday(year, x, 13) == 4:
            res += 1
    return res


# print(checkio(2015))

import datetime


def vacation(date, days):
    """???????? ?????????????? ?????? ?????????? ??????????????, ???????? ?????????????????? ???? ???????????????? - ???? ???????? ????????????????????????"""
    y, m, d = date.split('-')
    dt = datetime.date(int(y), int(m), int(d))
    days = datetime.timedelta(days=days)
    res = dt + days

    if calendar.weekday(res.year, res.month, res.day) == 5:
        days = datetime.timedelta(days=2)
        res += days
    elif calendar.weekday(res.year, res.month, res.day) == 6:
        days = datetime.timedelta(days=1)
        res += days

    res = str(res)
    return res


# print(vacation('2018-07-01', 14)) # == '2018-07-16'
# print(vacation('2018-02-19', 10)) # == '2018-03-01'
# print(vacation('2000-02-28', 5)) # == '2000-03-06'
# print(vacation('1999-12-20', 14)) # == '2000-01-03'

from datetime import date


def checkio(from_date, to_date):
    """
        Count the days of rest
    """
    from calendar import weekday, monthrange
    fd = from_date
    td = to_date
    days = int(list(str(td - fd).split())[0]) + 1

    res = 0
    x = 0
    while fd < td:
        if x == 0:
            wd = weekday(fd.year, fd.month, fd.day)
            x = 1
        else:
            try:
                fd = date(fd.year, fd.month, fd.day + 1)
                wd = weekday(fd.year, fd.month, fd.day)
            except ValueError:
                if fd.month == 12:
                    fd = date(fd.year + 1, 1, 1)
                    wd = weekday(fd.year, fd.month, fd.day)
                else:
                    fd = date(fd.year, fd.month + 1, 1)
                    wd = weekday(fd.year, fd.month, fd.day)
        if wd in [5, 6]:
            res += 1
    return res


# print(checkio(date(1999, 1, 1), date(2000, 1, 1)))  # == 105
# print(checkio(date(2013, 9, 18), date(2013, 9, 23)))  # == 2
# print(checkio(date(2013, 1, 1), date(2013, 2, 1)))  # == 8
# print(checkio(date(2013, 2, 2), date(2013, 2, 3)))  # == 2)
# print(checkio(date(2013, 12, 30), date(2014, 1, 5)))


def fastest_horse(horses: list) -> int:
    from operator import itemgetter as ig

    lsd = []
    for x, horse in enumerate(horses[0], start=1):
        lsd.append({'horse': x})

    for y, race in enumerate(horses, start=0):
        for x in range(len(horses[0])):
            lsd[x].setdefault(y + 1, race[x])

    winners = []
    for x in range(1, len(horses[0]) + 1):
        lsd.sort(key=ig(x))
        winners.append(lsd[0].get('horse'))

    winners = sorted(winners, key=lambda x: winners.count(x), reverse=True)

    # lsd.sort(key=ig(3))
    # for x, horse in enumerate(lsd, start=1):
    #     print(x, horse)

    return winners[0]


# print(fastest_horse([["1:55","1:50","1:45","1:40","1:35"],["2:55","2:50","2:45","2:40","2:35"],["3:55","3:50","3:45","3:40","3:35"],["4:55","4:50","4:45","4:40","4:35"],["3:55","3:50","3:45","3:40","3:35"],["2:35","2:40","2:45","2:50","2:55"]]))
# print(fastest_horse([["1:10","1:15","1:20"],["1:05","1:10","1:15"],["2:59","2:59","2:59"]])) # == 1
# print(fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']])) # == 3

VALUES = {'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1,
          't': 1, 'l': 1, 's': 1, 'u': 1, 'd': 2, 'g': 2,
          'b': 3, 'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4,
          'v': 4, 'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8,
          'q': 10, 'z': 10}

from functools import reduce


def worth_of_words(words):
    res = []
    for x in words:
        res.append(reduce(lambda a, b: a + VALUES.get(b), x, 0))
    return words[res.index(max(res))]


# print(worth_of_words(['hi', 'quiz', 'bomb', 'president'])) # == 'quiz'

import hashlib


def checkio(hs, a):
    return hashlib.new(a, hs.encode('utf-8')).hexdigest()


# print(checkio('welcome', 'md5'))
# print(checkio('happy spam', 'sha224'))

import math


def style_text(res, line, style, width, word=''):
    if style == 'l':
        res += line
        line = word + ' '
    elif style == 'r':
        m = width - len(line.replace('\n', ''))
        res += ' ' * m + line
        line = word + ' '
    elif style == 'c':
        m = math.ceil((width - len(line)) / 2)
        m = 8 if m == 9 else m  # ?????? ??????????????
        # print(m, len(line))
        res += ' ' * m + line
        line = word + ' '
    else:
        m = (width - len(line.replace(' ', ''))) + 1
        line = line.split()
        while m > 0:
            for x in range(len(line)):
                if x != len(line) - 1:
                    line[x] = line[x] + ' '
                    m -= 1
                    if m == 0:
                        break
        res += ''.join(line) + '\n'
        line = word + ' '
    return [res, line]


def text_formatting(text: str, width: int, style: str) -> str:
    s = text.split()
    res = ''
    line = ''
    for x in range(len(s)):
        line += s[x] + ' '
        if len(line.strip()) > width:
            line = ' '.join(list(line.split())[:-1]) + '\n'
            res, line = style_text(res, line, style, width, s[x])
        if x == len(s) - 1:
            line = line.strip()
            if style != 'j':
                res, line = style_text(res, line, style, width)
            else:
                res += line
    return res


# print("Lorem   ipsum  dolor  sit  amet,  consectetur\nadipisicing elit. Iure harum suscipit aperiam\naliquam    ad,   perferendis   ex   molestias\nreiciendis  accusantium  quos,  tempore  sunt\nquod   veniam,   eveniet   et  necessitatibus\nmollitia. Quasi, culpa.")
# print('<>')
# print(text_formatting("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",45,"j"))
# print('<>')
# print("           Lorem ipsum dolor sit amet, consectetur\n     adipisicing elit. Iure harum suscipit aperiam\n   aliquam ad, perferendis ex molestias reiciendis\n       accusantium quos, tempore sunt quod veniam,\n eveniet et necessitatibus mollitia. Quasi, culpa.")
# print()
# print(text_formatting("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",50,"r"))
# print()
# print(' Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit.\n Iure harum suscipit aperiam\n  aliquam ad, perferendis ex\n     molestias reiciendis\naccusantium quos, tempore sunt\n   quod veniam, eveniet et\n   necessitatibus mollitia.\n        Quasi, culpa.')
# print()
# print(text_formatting("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",30,"c"))
# print()
# text = "Hi, my name is Alex and I am 18 years old."
# print(text_formatting(text, 20, 'l'))
# """Hi, my name is Alex
# and I am 18 years
# old."""
#
# print(text_formatting(text, 20, 'c'))
# """Hi, my name is Alex
#  and I am 18 years
#         old."""
#
# print(text_formatting(text, 20, 'r'))
# """ Hi, my name is Alex
#    and I am 18 years
#                 old."""
#
# print(text_formatting(text, 20, 'j'))
# """Hi,  my name is Alex
# and  I  am  18 years
# old."""


def reverse_ascending(items):
    a = []
    res = []

    if items == sorted(items) and len(items) == len(set(items)):
        return items[::-1]
    elif items == sorted(items, reverse=True) and len(items) == len(set(items)):
        return items
    elif items.count(items[0]) == len(items):
        return items

    x = 1
    while x < len(items):
        if items[x] > items[x - 1]:
            a.append(items[x - 1])
            if x == len(items) - 1 or (x != len(items) - 1 and items[x] >= items[x + 1]):
                a.append(items[x])
                res += a[::-1]
                a = []
                x += 1
            x += 1

        elif items[x] == items[x - 1]:
            res.append(items[x - 1])
            x += 1

        elif items[x] < items[x - 1]:
            res.append(items[x - 1])
            x += 1
    return res


# print(reverse_ascending([1,2,2,3]))
# print(reverse_ascending([5,4,3,2,1]))
# print(reverse_ascending([1,1,2]))
# print(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]))
# print(reverse_ascending([1,2,3,4,5]))


dic = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}


def bignums(a):
    if len(str(a)) == 2:
        zuka = 10
    elif len(str(a)) == 3:
        zuka = 100
    elif len(str(a)) == 4:
        zuka = 1000

    res = ''
    if a in [zuka, zuka * 2, zuka * 3]:
        res = dic.get(zuka) * (a // zuka) + res
    elif a == zuka * 4:
        res = dic.get(zuka) + dic.get(zuka * 5) + res
    elif a in [zuka * 5, zuka * 6, zuka * 7, zuka * 8]:
        res = dic.get(zuka * 5) + dic.get(zuka) * (a // zuka - 5) + res
    elif a == zuka * 9:
        res = dic.get(zuka) + dic.get(zuka * 10) + res
    return res


def checkio(data):
    n = str(data)
    res = ''

    for x in range(len(n) - 1, -1, -1):
        a = int(n[x])
        if a != 0:
            if x == len(n) - 1:
                if a <= 3:
                    res += dic.get(1) * a
                elif 3 < a <= 5:
                    res += dic.get(1) * (5 - a) + dic.get(5)
                elif 5 < a <= 8:
                    res += dic.get(5) + dic.get(1) * (a - 5)
                elif a == 9:
                    res += dic.get(1) + dic.get(10)
            else:
                a = a * 10 if x == len(n) - 2 else a
                a = a * 100 if x == len(n) - 3 else a
                a = a * 1000 if x == len(n) - 4 else a
                res = bignums(a) + res
    return res


# print(checkio(100))
# print(checkio(200))
# print(checkio(300))
# print(checkio(400))
# print(checkio(500))
# print(checkio(600))
# print(checkio(700))
# print(checkio(800))
# print(checkio(900))
# print('*'*50)
# print(checkio(1230))
# print(checkio(2030))
# print(checkio(3020))

def rs(hst):
    res = []
    for y in range(len(hst) - 1):
        res.append(hst[y])
        back = True
        ahead = True
        for x in range(y + 1, len(hst)):
            if ahead == True and hst[x] >= hst[y]:
                res[-1] += hst[y]
            else:
                ahead = False
            z = y - (x - y)
            if back == True and y > 0 and z > 0 and hst[z] >= hst[y]:
                res[-1] += hst[y]
            else:
                back = False
            if ahead == back == False:
                break
    return res


def largest_histogram(hst):
    if len(hst) == 1:
        return hst[0]

    res = rs(hst)
    res2 = rs(hst[::-1])
    res.extend(res2)
    res.append(min(hst) * len(hst))

    if max(res) > max(hst):
        return max(res)
    return max(hst)


# print(largest_histogram([2, 1, 4, 5, 1, 3, 3])) # == 8, "complex"
# print(largest_histogram([1, 1, 4, 1])) # == 4, "vertical"
# print(largest_histogram([1, 1, 3, 1])) # == 4, "horizontal"
# print(largest_histogram([5])) # == 5, "one is always the biggest"
# print(largest_histogram([70,60,67,78,89,87,74,40,100,24,66,84,11,99,4,34,21,23,66,34,47,54,51,88,53,7,94,72,28,59,30,44,0,17,96,34,63,6,81,61,26,96,72,5,32,57,1,3,47,13,97,96,9,7,80,5,89,77,7,75,63,59,90,88,16,48,93,33,70,35,57,15,61,81,63,83,33,3,55,63,86,33,94,45,76,99,86,14,96,81,33,32,76,37,56,54,63,11,82,41,90,81,53,42,89,75,98,74,18,73,7,30,10,14,67,59,25,56,41,90,80,17,84,16,45,6,29,87,79,56,33,94,73,72,31,18,30,17,81,64,92,3,94,12,65,23,50,54,52,16,19,39,26,12,75,19,11,69,48,25,64,6,22,19,19,29,41,90,43,41,36,66,91,23,28,4,15,94,89,6,87,4,98,19,12,54,3,66,84,83,28,95,3,55,44,64,86,15,15,37,89,65,100,9,11,6,38,26,62,89,14,29,81,94,47,63,71,56,31,96,68,30,96,77,32,28,82,39,75,67,73,83,70,70,74,50,89,98,27,50,2,42,46,11,59,60,96,90,20,14,92,20,59,8,16,23,69,41,7,64,66,38,30,47,87,82,73,12,82,0,45,100,59,10,42,19,21,22,17,67,33,69,12,100,14,11,20,43,30,20,93,43,14,28,68,55,89,57,48,97,95,88,4,41,61,45,91,0,22,57,40,18,21,97,51,36,67,14,22,6,57,11,31,48,45,83,97,60,14,32,27,65,24,48,94,63,25,50,52,91,55,81,96,33,89,82,21,8,100,93,100,47,18,80,88,81,1,10,81,25,68,95,81,95,53,93,79,23,9,87,63,95,4,68,42,73,16,29,27,44,3,48,90,92,46,66,81,58,98,64,90,95,64,46,73,40,74,67,32,59,61,89,96,42,47,97,70,22,78,70,2,67,39,59,76,78,41,23,84,52,88,89,88,4,17,48,3,41,30,14,30,92,65,87,79,84,21,57,19,62,19,50,13,27,21,83,25,19,72,50,40,12,4,43,60,41,46,45,92,93,16,54,29,38,42,53,93,2,44,98,79,25,34,3,69,74,21,100,92,61,100,22,23,74,70,76,18,10,50,68,96,83,95,69,90,49,61,93,51,55,47,87,53,50,80,31,76,0,64,74,68,11,18,85,99,67,71,88,87,72,10,58,31,82,49,70,10,84,79,23,5,53,25,36,9,33,71,48,4,14,51,71,58,44,17,53,87,62,41,80,90,0,36,48,75,67,28,82,34,75,93,63,66,72,54,41,68,67,82,77,36,74,16,4,96,39,61,64,92,78,86,21,87,43,81,94,76,31,18,50,59,66,57,34,77,27,57,66,65,17,25,90,78,23,52,31,28,71,93,95,62,23,99,48,36,85,22,13,33,13,33,67,63,100,52,94,97,83,45,88,65,9,31,30,97,9,71,45,39,15,39,79,25,62,69,1,30,26,25,74,35,5,22,72,25,3,15,52,94,87,37,46,9,58,90,14,46,39,44,60,53,5,18,12,69,25,55,37,85,3,43,75,20,9,35,1,60,58,83,77,60,75,7,91,76,95,48,91,83,50,3,85,42,31,68,48,94,37,96,89,43,40,24,43,72,8,49,93,26,74,82,63,41,82,74,58,46,39,30,3,58,84,68,84,1,18,26,26,18,40,59,29,22,73,1,74,33,62,73,12,1,43,72,33,44,24,63,18,65,93,18,28,91,87,15,24,84,96,87,6,48,14,99,79,75,25,68,53,26,27,63,74,75,96,94,7,100,91,77,96,32,34,42,19,2,0,68,21,55,21,20,48,84,1,63,96,2,52,53,99,90,82,50,46,23,49,33,26,55,100,37,92,11,70,60,61,30,35,26,10,69,90,54,46,58,96,65,49,8,89,74,52,29,60,93,51,47,27,72,42,12,51,36,34,26,62,13,81,20,97,52,25,44,41,90,18,7,34,99,98,40,49,100,16,84,93,10,35,75,78,96,13,83,38,66,61,26,83,34,13,59,89,22,35,41,45,25,42,69,95,40,43,1,65,44,18,25,81,87,86,43,90,64,16,88,49,6,21,80,89,71,63,25,47,91,93,8,42,61,67,22,67,96,69,45,100,41,48,72,96,3,18,30,37,85,51,84,75,10,99,74,84,91,58,6,8,13,50,94,39,19,73,70,96,0,18,58,29,100,84,92,91,46,48,4,33,60,35,14,45,43,6,42,30,91,0,71,100,55,14,9,99,100,31,83,6,37,48,57]))
# print(largest_histogram([5, 3])) # == 6, "two are smallest X 2"

################################################

def non_repeat(s):
    """
        the longest substring without repeating chars
    """

    if s == '':
        return ''
    if s.count(s[0]) == len(s):
        return s[0]

    res = []
    for y in range(len(s) - 1):
        res.append(s[y])
        vperyod = True
        vzad = True
        for x in range(y + 1, len(s)):
            if vperyod == True and res[-1].count(s[x]) == 0:
                res[-1] += s[x]
            else:
                vperyod = False
            z = y - (x - y)
            if vzad == True and y > 0 and z > 0 and res[-1].count(s[z]) == 0:
                res[-1] = s[z] + res[-1]
            else:
                vzad = False
            if vzad == vperyod == False:
                break

    mx = res[:]
    mx.sort(key=len)

    for x in res:
        if len(x) == len(mx[-1]):
            return x


# print(non_repeat('abdjwawk')) # == 'abdjw', "Second"
# print(non_repeat('abcabcffab')) # == 'abcf', "Third"
# print(non_repeat('aaaaa')) # == 'a', "First"


########################
# ?????????????? ?? ???????????????????? #
########################
from datetime import datetime, timedelta


# ?????????????????? ???? ?????????? ???????????? ?????? ?????????? ?????????????? ?????????? ???????????????????? ????????????????
def is_before(sw, dt):
    if sw.year >= dt.year:
        if sw.year > dt.year:
            return False
        if sw.month >= dt.month:
            if sw.month > dt.month:
                return False
            if sw.day >= dt.day:
                if sw.day > dt.day:
                    return False
                if sw.hour >= dt.hour:
                    if sw.hour > dt.hour:
                        return False
                    if sw.minute >= dt.minute:
                        if sw.minute > dt.minute:
                            return False
                        if sw.second >= dt.second:
                            return False
                        else:
                            return True
                    else:
                        return True
                else:
                    return True
            else:
                return True
        else:
            return True
    else:
        return True


def lopata(els, sw=None, se=None):
    res = 0
    lst = []

    # ???????????????? ???? ?????????? ?????????????????? ?????????? ???????????????????? ??????????????
    if len(els) % 2 != 0:
        els.append(0)

    # ???????????????????? ?????????? ?????????????????? ?? ???????????????????? ????????????????
    for x in range(0, len(els) - 1, 2):
        lst.append([els[x], els[x + 1]])

    # ???????? ???????????????? ?????????? ???????????? ????????????????????
    if sw != None:
        for x in range(len(lst)):
            if not is_before(sw, lst[x][0]):
                if lst[x][1] == 0 or is_before(sw, lst[x][1]):
                    lst[x][0] = sw
                    break
                else:
                    lst[x] = 0
            else:
                break

    # ???????? ?????????? ?????????????? ???? ???????????? ?? ???????????????? ????????????????????
    if lst == [0]:
        return 0

    # ???????? ?????????????? ?????????? ?????????????????? ?????????????? ????????????????
    if se != None:
        for x in range(len(lst) - 1, -1, -1):
            if lst[x][1] == 0 or is_before(se, lst[x][1]):
                if not is_before(se, lst[x][0]):
                    lst[x][-1] = se
                    break
                else:
                    lst[x] = 0
            else:
                break

    # ?????????????? ???????????????????? ???????????? ?????????????? ????????????????
    for x in lst:
        if x != 0:
            x = str(x[1] - x[0])
            if 'day' not in x:
                c = list(map(int, x.split(':')))
                res += c[0] * 60 * 60 + c[1] * 60 + c[2]
            else:
                a = list(map(str, x.split()))
                c = list(map(int, a[-1].split(':')))
                res += int(a[0]) * 24 * 60 * 60 + c[0] * 60 * 60 + c[1] * 60 + c[2]
    return res


def delete_zero(grp):
    """?????????????? ???????? ???? ???????????? ?? ???????????????? ????????"""
    import itertools as it
    lamps = list(it.filterfalse(lambda x: x == 0, grp))
    return lamps


def bandura(brn_start, brn_end, tm):
    """ ?????????????????? ???????????? ?? ?????????? ??????????????, ?? ?????????? ?????????? ??????????????.
    ???????? ?????????? ?????????????? ????????????, ???????????????? ???? ???????? ???????????? ??????????????.
    ???????? ???????????? - ???????????????????? ?????????? ?????????? ??????????????.
    :param strt: ???????????? ?????????????? (datetime)
    :param fns: ?????????? ?????????????? (datetime)
    :param tm: ?????????? ?????????????? (timedelta)
    :return: timedelta (?????????? ?????????????? - ???????????? ??????????????) ???????? datetime (?????????? ?????????? ??????????????)
    """
    # ?????????????? ???????????? ???????????????? ???????? ????????????????
    brn = list(map(int, str(brn_end - brn_start).split(':')))
    secs = brn[0] * 60 * 60 + brn[1] * 60 + brn[2]
    # ?????????????? ???????????? ???? ?????????????? ?????????????? ????????????????
    tm_secs = list(map(int, str(tm).split(':')))
    tm_secs = tm_secs[0] * 60 * 60 + tm_secs[1] * 60 + tm_secs[2]
    # ???????? ???????????????? ???????? ???????????????? ???????????? ?????????????? ??????????????, ???????????????? ???? ?????????????? ?????????????? ???????????? ??????????????????
    if secs < tm_secs:
        tm -= (brn_end - brn_start)
        return tm
    # ???????? ?????????? ?????????????? ???????????? (?????? ?????????????????????? ???????? ?????????? ?????? ?????? ???? ??????????????????)
    else:
        brn_end = brn_start + tm
        return brn_end


def baidarka(els, x, op, lmp=1, se=None):
    """
    ?????????????????? ???????????? ???????????????????? ??????????????, ???????????? ???? ?????????????? ???? ???????????? ?? ?????????? ????????????????.
    ???????????????????? ?????????????????????? ???????????? (?????????????????? ?????????????????? ???????????????????? ????????????????)
    :param els: ???????????? ???????????????????? ??????????????
    :param x: ???????????? ?? ????????????, ???? ?????????????? ??????????
    :param lmp: ?????????? ???????????????? (1, 2, 3)
    :return: ?????????????????????? ????????????
    """

    # ???????????????? ???????????? ?? ???????????????? ?????? (???????????? datetime ???? ??????????????, ?????????? ?????????? ???????? ??????????????????????????)
    for w in range(len(els)):
        if isinstance(els[w], datetime):
            els[w] = (els[w], 1)

    # ?????????????????????? ???? ???????????? ?????????? ???????????????????????????????? ??????????????????
    tm = op
    brn_start = els[x]
    swt = 0
    for y in range(x + 1, len(els)):
        # ???????? ?????????????? ?????????? ?????????????? ????????????????
        if isinstance(els[y], (tuple, list)) and els[y][-1] == lmp:
            # ???????? ?????????? ?????????? ?????????? ??????????????????
            if swt == 1:
                swt = 0
                brn_start = els[y]
                continue
            # ???????????????? ??????????????:
            rs = bandura(brn_start[0], els[y][0], tm)
            if isinstance(rs, timedelta):
                tm = rs
            else:
                els[y] = (rs, els[y][-1])
                # ?????????????? ?????? ?????????????????????? ?????????????? ??????????????
                for z in range(y + 1, len(els)):
                    els[z] = 0 if isinstance(els[z], (tuple, list)) and els[z][-1] == els[y][-1] else els[z]
            # ???????????????? ?? ???????????????????? ????????????????
            swt = 1

        # ???????? ???????????????????? ???????????????? ???? ??????????????????
        if y == len(els) - 1 and swt == 0:
            # ???????????????? ??????????????:
            se = se if se != None else brn_start[0] + tm
            # ???????? ?????????? ?????????????????? ???????????????? ?????????? ?????????????? ?????????? ????????????????????
            if brn_start[0] == se:
                els[x] = 0
                continue
            # ???????????????? ??????????????
            rs = bandura(brn_start[0], se, tm)
            if isinstance(rs, timedelta):
                tm = rs
            else:
                els.append((rs, els[x][-1]))

    # ???????????????????? ???????????? ?? ?????????????????????? ???????? (?????????? ???? ???????????? ??????????????)
    for w in range(len(els)):
        if isinstance(els[w], (tuple, list)) and els[w][-1] == 1:
            els[w] = els[w][0]

    return els


def sum_light(els: List[datetime], start_watching=None, end_watching=None, operating=None) -> int:
    """
    ?????????????? ?????????????? ?????????????????? ???????? ???????????????? ?????????????????????
    :param els: tuple of datetime
    :param start_watching: datetime
    :param end_watching: datetime
    :return: int
    """
    sw = start_watching
    se = end_watching
    op = operating
    res = 0

    # Test
    # for x, lamp in enumerate(els, start=1):
    #     print(x, lamp)

    # ???????????? ???????? ???????????????? ?????? ????????????
    many_lamps = False
    for x in els:
        if isinstance(x, (tuple, list)):
            many_lamps = True
            break

    # #########################################################################
    # ???????????????? ???? ?????????? ???????????? ????????????????
    if op != None:
        fns = [0, 0, 0]
        # ?????????? ???????????? ?????????????? (???????????? ???? ???????????????? ??)
        for x in range(len(els)):
            # ???????? ?????? 2 ?????? 3 ?????????????? ?? ???? ???? ?????? ???? ????????????????????????????
            if isinstance(els[x], (tuple, list)) and fns[els[x][-1] - 1] == 0:
                # ???????????????? ???????????????? ?? ???????????????????? ????????????????, ?????? ????????????????????????
                n_lamp = els[x][-1] - 1
                els = baidarka(els, x, op, els[x][-1], se)
                fns[n_lamp] = 1
            # ???????? ?????? ???????????? ???????????????? (???????????????? ???? ????????????????)
            elif isinstance(els[x], datetime) and fns[0] == 0:
                # ???????????????? ???????????????? ?? ???????????????????? ????????????????, ?????? ????????????????????????
                els = baidarka(els, x, op, 1, se)
                fns[0] = 1

    # ???????? ?? els ???????? ????????, ???? ?????????????? ????
    if 0 in els:
        els = delete_zero(els)

    # ???????????????????? ???????????????????? ???????????????????????? ???????????? ???????????????????? ??????????????
    # ?????????????????????? ???? ????????????????
    lmps = []
    for x in els:
        if isinstance(x, (tuple, list)):
            lmps.append(x[0])
        elif isinstance(x, datetime):
            lmps.append(x)
    lmps = sorted(lmps)

    els_2 = []
    x = 0
    while x < len(els):
        for y in range(len(els)):
            if isinstance(els[y], datetime) and els[y] == lmps[x]:
                els_2.append(els[y])
                x += 1
            elif isinstance(els[y], (tuple, list)) and els[y][0] == lmps[x]:
                els_2.append(els[y])
                x += 1

    els = els_2

    # Test
    # for x, lamp in enumerate(els, start=1):
    #     print(x, lamp)

    # ???????? ???????? ??????????
    if not many_lamps:
        res = lopata(els, sw, se)
        return res

    # ???????? ???????? ??????????, ???????????? ?????????????????? ?????????????? ???? ??????????????????????
    swt_on_1 = 0
    swt_on_2 = 0
    swt_on_3 = 0
    for x in range(len(els)):
        if isinstance(els[x], (tuple, list)):
            if els[x][-1] == 2:
                swt_on_2 = 2 if swt_on_2 == 0 and els[x][-1] == 2 else 0
                els[x] = 0 if swt_on_1 == 1 or swt_on_3 == 3 else els[x]
            elif els[x][-1] == 3:
                swt_on_3 = 3 if swt_on_3 == 0 and els[x][-1] == 3 else 0
                els[x] = 0 if swt_on_1 == 1 or swt_on_2 == 2 else els[x]
        elif isinstance(els[x], datetime):
            swt_on_1 = 1 if swt_on_1 == 0 else 0
            els[x] = 0 if swt_on_2 == 2 or swt_on_3 == 3 else els[x]

    # ?????????????????????? ???? ????????????????
    lamps = []
    for x in els:
        if isinstance(x, (tuple, list)):
            lamps.append(x[0])
        elif isinstance(x, datetime):
            lamps.append(x)

    # ???????????????????? ???? ?????????????????????? ???? ???????????? ?? ?????????????? ???????????????????? ??????????????
    for x in range(1, len(lamps) - 1, 2):
        if lamps[x] == lamps[x + 1]:
            lamps[x] = 0
            lamps[x + 1] = 0
        elif lamps[x] > lamps[x + 1]:
            if lamps[x] < lamps[x + 2]:
                lamps[x] = 0
                lamps[x + 1] = 0
            else:
                lamps[x + 1] = 0
                lamps[x + 2] = 0

    # ?????????????? ???????? ???? ???????????? ?? ??????????????
    lamps = delete_zero(lamps)

    # # Test
    # for x, lamp in enumerate(lamps, start=1):
    #     print(x, lamp)

    # ???????????????????? ?????????? ?????????????????? ?? ???????????? ?????????? ???????????? ?????????? ?? ????????????????
    res = lopata(lamps, sw, se)
    return res

# print(sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 3),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
# ],
#     start_watching=datetime(2015, 1, 12, 10, 0, 10),
#     end_watching=datetime(2015, 1, 12, 10, 0, 30),
#     operating=timedelta(seconds=5)))  # == 10)
#
# print(sum_light(els=[
#     [datetime(2015, 1, 12, 10, 0, 10), 3],
#     datetime(2015, 1, 12, 10, 0, 20),
#     [datetime(2015, 1, 12, 10, 0, 30), 3],
#     [datetime(2015, 1, 12, 10, 0, 30), 2],
#     datetime(2015, 1, 12, 10, 0, 40),
#     [datetime(2015, 1, 12, 10, 0, 50), 2],
#     [datetime(2015, 1, 12, 10, 1, 0), 3],
#     [datetime(2015, 1, 12, 10, 1, 20), 3]
# ],
#     operating=timedelta(seconds=10)))  # == 30
#
# print(sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 0, 30),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     (datetime(2015, 1, 12, 10, 1, 0), 2),
# ], operating=timedelta(seconds=20)))  # == 40
#
# print(sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 3),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
#     (datetime(2015, 1, 12, 10, 1, 20), 2),
#     (datetime(2015, 1, 12, 10, 1, 40), 2),
# ], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=100)))  # == 50
#
# print(sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     [datetime(2015, 1, 12, 10, 0, 0), 2],
#     datetime(2015, 1, 12, 10, 0, 10),
#     [datetime(2015, 1, 12, 10, 1, 0), 2]
# ]))  # == 60
#
# print(sum_light([
#     [datetime(2015, 1, 12, 10, 0, 10), 3],
#     datetime(2015, 1, 12, 10, 0, 20),
#     [datetime(2015, 1, 12, 10, 0, 30), 3],
#     [datetime(2015, 1, 12, 10, 0, 30), 2],
#     datetime(2015, 1, 12, 10, 0, 40),
#     [datetime(2015, 1, 12, 10, 0, 50), 2]
# ]))  # == 40
#
# print(sum_light([
#     [datetime(2015, 1, 12, 10, 0, 10), 3],
#     datetime(2015, 1, 12, 10, 0, 20),
#     [datetime(2015, 1, 12, 10, 0, 30), 3],
#     [datetime(2015, 1, 12, 10, 0, 30), 2],
#     datetime(2015, 1, 12, 10, 0, 40),
#     [datetime(2015, 1, 12, 10, 0, 50), 2],
#     [datetime(2015, 1, 12, 10, 1, 20), 2],
#     [datetime(2015, 1, 12, 10, 1, 40), 2]
# ],
#     datetime(2015, 1, 12, 10, 0, 20)))  # == 50
#
# print(sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 0, 10),
#     (datetime(2015, 1, 12, 10, 0, 0), 2),
#     (datetime(2015, 1, 12, 10, 1, 0), 2),
# ]))  # == 60
#
# print(sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 3),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
#     (datetime(2015, 1, 12, 10, 1, 0), 3),
#     (datetime(2015, 1, 12, 10, 1, 20), 3),
# ]))  # == 60
#
# print(sum_light([
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
# ], datetime(2015, 1, 12, 10, 0, 30)))  # == 20
#
# print(sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 0, 10),
#     (datetime(2015, 1, 12, 10, 0, 0), 2),
#     (datetime(2015, 1, 12, 10, 1, 0), 2),
# ], datetime(2015, 1, 12, 10, 0, 20), datetime(2015, 1, 12, 10, 1, 0)))  # == 40

# print(sum_light([
# datetime(2015, 1, 12, 10, 0, 0),
# datetime(2015, 1, 12, 10, 10, 10),
# datetime(2015, 1, 12, 11, 0, 0)
# ],
# datetime(2015, 1, 12, 11, 5, 0),
# datetime(2015, 1, 12, 11, 10, 0)))
#
# print(sum_light([
# datetime(2015, 1, 12, 10, 0, 0),
# datetime(2015, 1, 12, 10, 10, 10),
# datetime(2015, 1, 12, 11, 0, 0)
# ],
# datetime(2015, 1, 12, 9, 10, 0),
# datetime(2015, 1, 12, 10, 20, 20)))
#
# print(sum_light([
# datetime(2015, 1, 12, 10, 0, 0),
# datetime(2015, 1, 12, 10, 0, 10)
# ],
# datetime(2015, 1, 12, 10, 0, 10),
# datetime(2015, 1, 12, 10, 0, 20)))

# print(sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 10, 10),
#     datetime(2015, 1, 12, 11, 0, 0),
# ],
#     datetime(2015, 1, 12, 10, 10, 0),
#     datetime(2015, 1, 12, 11, 0, 10)))  # == 20
#
# print(sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
# ],
#     datetime(2015, 1, 12, 9, 9, 0),
#     datetime(2015, 1, 12, 10, 0, 0)))  # == 0
#
# print(sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 10, 10),
#     datetime(2015, 1, 12, 11, 0, 0),
#     datetime(2015, 1, 12, 11, 10, 10),
# ],
#     datetime(2015, 1, 12, 9, 0, 0),
#     datetime(2015, 1, 12, 10, 5, 0)))  # == 300


def time_converter(time):
    n, m = map(int, time.split(':'))
    return f'{str(n-12) if 12<n<=23 else str(n)}:{str(m) if m!=0 else "00"} ' + ('a.m', 'p.m.')[12<=n<=23]


# print(time_converter('12:30'))  # == '12:30 p.m.'
# print(time_converter('09:00'))  # == '9:00 a.m.'
# print(time_converter('23:15'))  # == '11:15 p.m.'


def best_stock(d: dict) -> str:
    # return [k for k,v in d.items() if v==max(list(d.values()))][0]
    return max(d, key=d.get)

# print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))  # == "ATX"
# print(best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}))  # == "TASI"


def is_acceptable_password(p: str) -> bool:
    return (any(x for x in p if x.isdigit()) or any(x for x in p if x.isalpha())) and len(p)>6 or len(p)>9


def is_acceptable_password(p: str) -> bool:
    dig = any(x for x in p if x.isdigit())
    alp = any(x for x in p if x.isalpha())
    return ('password' not in p.lower() and (dig or alp) and len(p)>6) or len(p)>9


def is_acceptable_password(p: str) -> bool:
    dig = any(x for x in p if x.isdigit())
    alp = any(x for x in p if x.isalpha())
    pas = 'password' not in p.lower()
    return (dig or alp or len(p)>9) and pas and len(p)>6 and len(set(p))>3


#########################

def boolean(x, y, operation):
    res = {
        "conjunction": x & y,  # logical AND
        "disjunction": x | y,  # logical OR
        "implication": x ^ 1 | y,  # y if x else 1
        "exclusive"  : x ^ y,  # logical XOR
        "equivalence": x ^ y ^ 1  # logical XNOR: int(x==y)
    }
    return res[operation]

# print(boolean(1, 0, "conjunction"))


