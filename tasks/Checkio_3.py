def yama(brace, s, nums):
    reserve_nums = []
    while brace in s:
        n = s.index(brace)
        reserve_nums.append(nums[n])
        del nums[n]
        s = s.replace(brace, '', 1)
    return s, reserve_nums


def lopata(s2, nums=None):
    # Удаляем лопатой одинокие скобки
    br = '()[]{}'
    reserve_nums = []
    for x in range(0, 5, 2):
        if s2.count(br[x]) != s2.count(br[x + 1]):
            if s2.count(br[x]) == 0:
                if nums:
                    s2, reserve_nums = yama(br[x + 1], s2, nums)
                else:
                    s2 = s2.replace(br[x + 1], '')
            elif s2.count(br[x + 1]) == 0:
                if nums:
                    s2, reserve_nums = yama(br[x], s2, nums)
                else:
                    s2 = s2.replace(br[x], '')
    return s2, reserve_nums


def bandura(s2, nums):
    while '()' in s2 or '[]' in s2 or '{}' in s2:
        if '()' in s2:
            x = '()'
        elif '[]' in s2:
            x = '[]'
        elif '{}' in s2:
            x = '{}'
        n = s2.find(x)
        del nums[n]
        del nums[n]
        s2 = s2.replace(x, '', 1)
    return s2, nums


def remove_brackets(s: str) -> str:
    reserve_nums = []
    s, reserve_nums = lopata(s)
    nums = list(range(len(s)))
    s2 = s
    s2, nums = bandura(s2, nums)

    w = 0
    r_nums = []
    while s2 != '':
        s2, r_nums = lopata(s2, nums)
        reserve_nums.extend(r_nums)
        for x in reserve_nums:
            if x in nums:
                nums.remove(x)
        s2, nums = bandura(s2, nums)
        w += 1
        if w >= 4 and s2 != '':
            s2 = s2[1:]
            reserve_nums.append(nums[0])
            del nums[0]

    nums.extend(reserve_nums)

    # Если все чисто
    if nums == []: return s

    # Удаляем все "плохие" скобки из s с помощью nums
    s = list(s)
    while nums != []:
        s[nums[0]] = 0
        del nums[0]

    s = list(filter(lambda x: x != 0, s))
    return ''.join(s)


# print(remove_brackets("[(])"))  # == "()"
# print(remove_brackets("[(()]"))  # == "[()]"
# print(remove_brackets("([)]"))  # == "[]"
#
# print(remove_brackets('[[(}]]'))  # == '[[]]'
# print(remove_brackets('(()()'))  # == '()()'
# print(remove_brackets('[][[['))  # == '[]'
# print(remove_brackets('[[{}()]]'))  # == '[[{}()]]'
# print(remove_brackets('[[[[[['))  # == ''
# print(remove_brackets('))}}]]'))  # == ''
# print(remove_brackets("[[[[}"))  # == ""
# print(remove_brackets(""))  # == ""
# print(remove_brackets("[()()]"))  # == "[()()]"
# print(remove_brackets("[(){}"))  # == "(){}"
# print(remove_brackets("[[{}()]]"))  # == "[[{}()]]"
# print(remove_brackets("{{{((([[["))  # == ""
# print(remove_brackets("(}"))  # == ""
# print(remove_brackets("({}]"))  # == "{}"
# print(remove_brackets("}}){}"))  # == "{}"


def sun_angle(time):
    hour, minute = map(int, time.split(':'))
    if hour < 6 or hour > 18 or hour == 18 and minute > 0: return "I don't see the sun!"
    ans = abs((hour * 15 + minute * 0.25))
    return abs(90 - ans)


# print(sun_angle("07:00"))  # == 15
# print(sun_angle("12:00"))
# print(sun_angle("12:01"))
# print(sun_angle("12:15"))  # == 93.75
# print(sun_angle("01:23"))  # == "I don't see the sun!")


def checkio(data):
    """ Cargo """
    # replace this for solution
    return 0


# print(checkio([10,10]))  # == 0
# print(checkio([10]))  # == 10
# print(checkio([5, 8, 13, 27, 14]))  # == 3
# print(checkio([5,5,6,5]))  # == 1
# print(checkio([12, 30, 30, 32, 42, 49]))  # == 9
# print(checkio([1, 1, 1, 3]))  # == 0


def sakura(kusok):
    res = []
    flat = []
    for k, v in kusok.items():
        if type(v) == dict:
            if v == {}:
                res.append([k, ''])
            else:
                flat = sakura(v)
    if flat:
        for x in flat:
            pass
    return res


def flatten(dic):
    res = {}
    for k, v in dic.items():
        if type(v) == dict:
            if v == {}:
                res.setdefault(k, '')
            else:
                flat = sakura(v)
                print('neo:', flat)
        else:
            res.setdefault(k, v)
    return res


# print(flatten({"key": "value"}))  # == {"key": "value"}
# print(flatten({"key": {"deeper": {"more": {"enough": "value"}}}}))  # == {"key/deeper/more/enough": "value"}
# print(flatten({"empty": {}}))  # == {"empty": ""}


def broken_clock(st_time, wr_time=None, error=None):
    # Если на вход дали список (не ну они нормальные вообще?)
    if wr_time == None:
        st_time, wr_time, error = st_time[0], st_time[1], st_time[2]

    from datetime import datetime, timedelta
    times = ['hours', 'minutes', 'seconds']
    zeros = ['00', '00', '00']
    wr, tms1, at, each, tms2 = error.split()
    wr1, each2 = int(wr[1:]), int(each)
    wr = str(wr1) if wr1 > 9 else '0' + str(wr1)
    each = each if each2 > 9 else '0' + each

    n1 = [times.index(x) for x in times if tms1 in x][0]
    n2 = [times.index(x) for x in times if tms2 in x][0]

    wr = ':'.join([x if tms1 not in times[n] else wr for n, x in enumerate(zeros)])
    each = ':'.join([x if tms2 not in times[n] else each for n, x in enumerate(zeros)])
    tmdelta = [timedelta(hours=wr1), timedelta(minutes=wr1), timedelta(seconds=wr1)][n1]

    # Если на вход дали ерунду, приводим ее в божеский вид
    if each2 > 60:
        adyn, dva = divmod(each2, 60)
        if adyn < 60:
            each = f'00:{adyn}:{dva}' if tms2 in 'seconds' else f'{adyn}:{dva}:00'
        else:
            while adyn > 60:
                tri, adyn = divmod(adyn, 60)
            each = f'{tri}:{adyn}:{dva}'

    tm = str(datetime.strptime(wr_time, '%H:%M:%S') - datetime.strptime(st_time, '%H:%M:%S'))
    if error[0] == '-':
        lol = str(datetime.strptime(each, '%H:%M:%S') - datetime.strptime(wr, '%H:%M:%S'))
    else:
        lol = str(datetime.strptime(each, '%H:%M:%S') + tmdelta)[-8:]

    # Все переводим в секунды
    lol_secs, tm_secs, each_secs = 0, 0, 0
    mnoj = [3600, 60, 1]
    tm_lst = tm.split(':')
    for n, x in enumerate(lol.split(':')):
        lol_secs += int(x) * mnoj[n]
        tm_secs += int(tm_lst[n]) * mnoj[n]
        each_secs = each2 * mnoj[n] if n == n2 else each_secs

    secs = int((tm_secs / lol_secs) * each_secs)
    return str(datetime.strptime(st_time, '%H:%M:%S') + timedelta(seconds=secs))[-8:]


# print(broken_clock(["13:21:11", "20:20:30", "-1 hour at 10600 seconds"]))
# print(broken_clock(["01:16:43", "04:22:30", "+1 minute at 150 seconds"]))
# print(broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds'))  # ==  '00:00:10'
# print(broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds'))  # ==  '06:10:30'
# print(broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute'))  # ==  '14:00:00'
# print(broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours'))  # ==  '07:05:05'
# print(broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds'))  # ==  '00:00:22')

######################################################################################################


def caps_lock(text: str) -> str:
    up, res = False, ''
    for x in text:
        if x == 'a':
            if up:
                up = False
            else:
                up = True
        else:
            if up and x.isupper():
                res += x.lower()
            elif up and x.islower():
                res += x.upper()
            else:
                res += x
    return res


# print(caps_lock("Why are you asking me that?"))  # == "Why RE YOU sking me thT?"
# print(caps_lock("Madder than Mad Brian of Madcastle"))  # == "MDDER THn MD BRIn of MDCstle"

def decode_vigenere(od, oe, nw):
    from string import ascii_uppercase as alf

    word = ''
    for n, x in enumerate(od):
        a = alf.index(oe[n]) - alf.index(x)
        word += alf[a]

    if len(nw) > len(od):
        fr_word = {}
        for x in range(2, len(word)):
            fr_word[word[0:x]] = word.count(word[0:x])

        for x in fr_word.keys():
            if x == word[len(x):(len(x)) * 2]:
                word = x

        word = word * len(nw) if len(nw) > len(word) else word

    res = ''
    for n, x in enumerate(nw):
        a = alf.index(nw[n]) - alf.index(word[n])
        res += alf[a]
    return res


# print(decode_vigenere(u"AAAAAAAAA", u"ABABABABC", u"ABABABABC"))
# print(decode_vigenere(u"NOBODYEXPECTSTHESPANISHINQUISITION", u"PVFQNGSZWIEDAHJLWRKVWUOMPACWUPXKYV", u"QBVGHXSTAWFOAQTPFGIWICZEPKXDCSPKXOZAKYNVNSNSSYEVWOHKKXIHKCIVSUWFSEEUQBIPRKXQHKHXKFMGRPRGVMGULEUSTMFVQKXIHGKRQCMBULSHRCAQBVVOLWQBWEYUDCUCCXLWTYIRBMGUPFNILFCIEPNIKHBPCXLKJLVGKAWPTSUDXFQMIUCQCPZXJOASYVYNNJSEVRUSLSTHFNOLFCDFCMSGKUGJKZHGYIFKKQQBRVKVQAALGIIFGHTQCQHKCIDYWB"))
# print(decode_vigenere(u"ANDNOWFORSOMETHINGCOMPLETELYDIFFERENT", u"PLWUCJUMKZCZTRAPBTRMFWZRICEFRVUDXYSAI", u"XKTSIZQCKQOPZYGKWZDIBZZRTNTSZAXEAAOASGPVFXPJEKOLXANARBLLMYSRHGLRWCPLWQIZEGEPYRIMIYSFHUBSRSAMPLFFXNNACALMFLBFRJHAVVCETURUPLZHFBJLWPBOPPL"))
# print(decode_vigenere('DONTWORRYBEHAPPY',
#                            'FVRVGWFTFFGRIDRF',
#                            'DLLCZXMFVRVGWFTF'))  # == "BEHAPPYDONTWORRY", "CHECKIO"
# print(decode_vigenere('HELLO', 'OIWWC', 'ICP'))  # == "BYE")


def most_frequent_days(a):
    from calendar import day_name
    from datetime import date
    days = sorted(list(set([date(a, 1, 1).weekday(), date(a, 12, 31).weekday()])))
    return [day_name[x] for x in days]


# print(most_frequent_days(1084))  # == ['Tuesday', 'Wednesday']
# print(most_frequent_days(1167))  # == ['Sunday'])
# print(most_frequent_days(1216))  # == ['Friday', 'Saturday']
# print(most_frequent_days(1492))  # == ['Friday', 'Saturday']
# print(most_frequent_days(1770))  # == ['Monday']
# print(most_frequent_days(1785))  # == ['Saturday']
# print(most_frequent_days(212))  # == ['Wednesday', 'Thursday']
# print(most_frequent_days(1))  # == ['Monday']
# print(most_frequent_days(2135))  # == ['Saturday']
# print(most_frequent_days(3043))  # == ['Sunday']
# print(most_frequent_days(2001))  # == ['Monday']
# print(most_frequent_days(3150))  # == ['Sunday']
# print(most_frequent_days(3230))  # == ['Tuesday']
# print(most_frequent_days(328))  # == ['Monday', 'Sunday']


COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''


def cowsay(text):
    front = True if text[0] == ' ' and len(text) > 39 else False
    text = ' '.join(text.split()) if len(text) > 10 else text
    while '  ' in text:
        text = text.replace('  ', ' ')
    # If text contains word longer 39 chars
    if any([x for x in text.split() if len(x) > 39]):
        a = []
        while len(text) > 39:
            a.append(text[:39])
            text = text[39:]
        a.append(text)
        text = ' '.join(a)

    # If text is on one line only
    if len(text) < 40:
        max_line = len(text)
        res = '\n ' + '_' * (max_line + 2) + '\n'
        res += '< ' + text + ' >\n'
    # Multiple lines text
    else:
        a = []
        line, line2 = [], []
        ready = False
        for word in text.split():
            line.append(word)
            while len(' '.join(line)) > 39:
                line2.append(line.pop())
                ready = True
            if ready:
                a.append(' '.join(line))
                line, ready = line2, False
                line2 = []
        a.append(' '.join(line))
        a = [' '] + a if front else a

        max_line = len(max(a, key=len))
        res = '\n ' + '_' * (max_line + 2) + '\n'
        res += '/ ' + a[0] + ' ' * (max_line - len(a[0])) + ' \\\n'
        # More than 2 lines
        if len(a) > 2:
            for x in a[1:-1]:
                res += '| ' + x + ' ' * (max_line - len(x)) + ' |\n'
        res += '\\ ' + a[-1] + ' ' * (max_line - len(a[-1])) + ' /\n'
    res += ' ' + '-' * (max_line + 2) + COW
    return res


# print(cowsay(" 0123456789012345678901234567890123456789 "))
# print(cowsay("    c     "))
# print(cowsay(" a"))
# print(cowsay("onehundredtwentytwo and one hundredfiftyone"))
# print(cowsay("looooooooooooooooooooooooooooooooooooong"))
# print(cowsay("loooooooooooooooooooooooooooooooooooong"))
# print(cowsay("loooooooooooooooooooooooooooooooooooong"))
# print(cowsay("spaces                           inside"))
# print(cowsay('Your bunny wrote'))
# print(cowsay('A longtextwithonlyonespacetofittwolines.'))
# print(cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'))\

"""

 _____________________________
/ onehundredtwentytwo and one \
\ hundredfiftyone             /
 -----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""


def get_keys(pwr):
    sort_values = sorted(pwr.values(), reverse=True)
    keys, ks = [], list(pwr.keys())
    for i in sort_values:
        k = 0
        while ks:
            if pwr[ks[k]] == i:
                keys.append(ks[k])
                del ks[k]
                break
            else:
                k += 1
    return keys


def power_supply(web, pwr):
    keys, k = get_keys(pwr), 0
    while k < len(keys):
        key, x = keys[k], 0
        while x < len(web):
            if key in web[x][0]:
                if len(web[x]) > 1:
                    sila = pwr.get(web[x][0])
                    if sila > 0:
                        pwr.setdefault(web[x][1], sila - 1)
                        del web[x]
                    else:
                        del web[x][0]
                else:
                    del web[x]
            elif len(web[x]) > 1 and key in web[x][1]:
                sila = pwr.get(web[x][1])
                if sila > 0:
                    pwr.setdefault(web[x][0], sila - 1)
                    del web[x]
                else:
                    del web[x][1]
            else:
                x += 1
        keys = get_keys(pwr)
        k += 1

    res = []
    for x in web:
        res.extend(x)
    return set(res)


# print(power_supply([["p0","c1"],["p0","c2"],["p0","c3"],["p0","c4"],["c4","c9"],["c4","c10"],["c10","c11"],["c11","p12"],["c2","c5"],["c2","c6"],["c5","c7"],["c5","p8"]],{"p0":1,"p12":4,"p8":1}))
# #  == ["c6","c7"]
# print(power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}))  # == set(['c0', 'c3'])
# print(power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}))  # == set([]))
# print(power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}))  # == set(['с2'])


# Determinant
def checkio(m):
    if len(m) == 1: return m[0][0]
    res = 0
    for a, row in enumerate(m):
        cut_m = [x[1:] for n, x in enumerate(m) if n != a]
        res += m[a][0] * checkio(cut_m) * (-1) ** a
    return res


# print(checkio([[2,7,6,4,2,0],[3,0,8,2,5,6],[3,8,9,1,0,3],[9,4,5,0,8,6],[8,9,0,6,4,6],[1,6,3,0,7,1]]))  # -140558
# print(checkio([[7, 8, 9, 7], [9, 4, 4, 7], [1, 8, 1, 7], [9, 0, 7, 1]]))  # == -464
# print(checkio([[1]]))  # == 1
# print(checkio([[4,3], [6,3]]))  # == -6
# print(checkio([[1, 3, 2],
#                 [1, 1, 4],
#                 [2, 2, 1]]))  # == 14)


from typing import Iterable


def can_balance(w: Iterable) -> int:
    if len(w) == 1: return 0
    for n, x in enumerate(w[1:-1], start=1):
        before = [x * y for y, x in enumerate(reversed(w[:n]), start=1)]
        after = [x * y for y, x in enumerate(w[n + 1:], start=1)]
        if sum(before) == sum(after):
            return n
    return -1


# print(can_balance([42]))  # == 0
# print(can_balance([6, 1, 10, 5, 4]))  # == 2
# # 10*1 == 3*1 + 2*2 + 1*3
# print(can_balance([10, 3, 3, 2, 1]))  # == 1


def rotate(state, nums):
    bullets = [(sum(y == n for y in nums)) for n, _ in enumerate(state)]
    z, mx, res = 0, max(bullets), []
    while z < mx:
        step = 0
        for _ in bullets:
            correct = not any([x for n, x in enumerate(bullets) if bullets[n] > 0 and state[n] == 0])
            if correct: res.append(step)
            step += 1
            state = [state[-1]] + state[:-1]
        z += 1
    return [x for n, x in enumerate(res) if res[:n].count(x) == 0]


# print(rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]))  # == [1, 8]
# print(rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]))  # == []
# print(rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]))  # == [0]
# print(rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]))  # == [0, 5])

def bin_to_dec(lst):
    return sum([y * 2 ** n for x in lst for n, y in enumerate(x[::-1])])


def checkio(a, b):
    a, b = bin(a)[2:], bin(b)[2:]
    res_and = [[int(x) & int(y) > 0 for y in b] for x in a]
    res_or = [[int(x) | int(y) for y in b] for x in a]
    res_xor = [[int(x != y) for y in b] for x in a]
    return bin_to_dec(res_and) + bin_to_dec(res_or) + bin_to_dec(res_xor)


# print(checkio(4, 6))  # == 38
# print(checkio(2, 7))  # == 28
# print(checkio(7, 2))  # == 18


def checkio(cells):
    (start, end), steps, vd = [(8 - int(e[1]), ord(e[0]) - 97) for e in cells.split('-')], 0, set()
    STEPS, nxt = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)], {start}
    while end not in nxt:
        vd.update(nxt)
        nxt = {(x + dx, y + dy) for (x, y) in nxt
               for dx, dy in STEPS if 8 > x + dx >= 0 and 8 > y + dy >= 0 and (x + dx, y + dy) not in vd}
        steps += 1
    return steps


# print(checkio("a1-h8"))  # == 6, "Fifth")
# print(checkio("b1-d5"))  # == 2, "First"
# print(checkio("a6-b8"))  # == 1, "Second"
# print(checkio("h1-g2"))  # == 4, "Third"
# print(checkio("h8-d7"))  # == 3, "Fourth"


def lol(points, ys, n, u):
    while len(ys) > 1:
        ys = sorted(ys, key=lambda x: x[n])
        points.remove(ys[u])
        del ys[u]
    return points


def check_points(points, x, y, n, m):
    same = [point for point in points if point[m] == x]
    if len(same) > 1:
        ys_less, ys_more = [], []
        for point in same:
            if y > point[n]:
                ys_less.append(point)
            else:
                ys_more.append(point)
        if ys_less: points = lol(points, ys_less, n, 0)
        if ys_more: points = lol(points, ys_more, n, -1)
    return points


def berserk_rook(hero, enemies):
    hero, desk = [8 - int(hero[1]), ord(hero[0]) - 97], [[0] * 8 for _ in range(8)]
    enemies, points, graph, nxt = list(enemies), [hero], [[hero]], [[hero]]
    ready, ready_lst = 0, []

    for x in enemies:
        desk[8 - int(x[1])][ord(x[0]) - 97] = 1

    while ready < len(graph):
        for m, z in enumerate(graph):
            if m in ready_lst: continue
            x, y = z[-1][0], z[-1][1]
            points = [[x, n] for n, a in enumerate(desk[x]) if a == 1 and [x, n] not in z]
            points.extend([[n, y] for n, a in enumerate(list(zip(*desk))[y]) if a == 1 and [n, y] not in z])
            points = check_points(points, x, y, 1, 0)
            points = check_points(points, y, x, 0, 1)

            if points:
                path = [x[:] for x in nxt[m]]
                n2 = m
                for n1, w in enumerate(points):
                    if w not in nxt[m]:
                        nxt[n2].append(w)
                        if len(points) > 1 and n1 != len(points) - 1:
                            nxt.append(path[:])
                            n2 = -1
            else:
                ready += 1
                ready_lst.append(m)
        graph = nxt
    return len(max(graph, key=len)) - 1


# print(berserk_rook('h1', ('a5', 'b6', 'e2', 'a2', 'h5', 'e4', 'e6', 'h7')))  # == 7
# print(berserk_rook(u'a2', {u'f6', u'f8', u'f2', u'a6', u'h6'}))  # == 4)
# print(berserk_rook(u'd3', {u'd6', u'b6', u'c8', u'g4', u'b8', u'g6'}))  # == 5
# print(berserk_rook(u'a2', {u'f6', u'f2', u'a6', u'f8', u'h8', u'h6'}))  # == 6
# print(berserk_rook('c5', ('h5',))) # == 1
# print(berserk_rook('c5', ('e3', 'b6', 'e7', 'f2', 'd6', 'b4', 'g8', 'd4')))  # == 0
# print(berserk_rook('e5', ('e8', 'e2', 'h8', 'h5', 'b5', 'h2', 'b2', 'b8')))  # == 8
# print(berserk_rook('c5', ('a5', 'd5', 'g5', 'h5', 'b5', 'e5', 'f5')))  # == 7
# print(berserk_rook('e1', ('e8', 'h1', 'c2', 'h5', 'e4', 'a1', 'e6', 'a3')))  # == 3
# print(berserk_rook('c7', ('d5', 'f7', 'e6', 'e7', 'c5', 'd6', 'e5', 'c6')))  # == 8
# print(berserk_rook('c7', ('d5', 'f7', 'e7', 'c5', 'd6', 'd4', 'c6', 'c4')))  # == 6


def tree_walker(tree, target):
    if type(tree) == int or tree == target:
        return int(tree == target)
    itr = tree if isinstance(tree, (list, tuple)) else list(tree.values())
    res = 0
    for x in itr:
        if x == target:
            res += 1
        elif isinstance(x, (list, dict, tuple)):
            res += tree_walker(x, target)
    return res


# print(tree_walker(tree=[1, "2", 3, [[3], 1, {1: "one"}]], target=1))  # == 2                                        #example #1
# print(tree_walker(tree={"one": 1, "two": [{1: "one", 2: "two"}, 1, "1", "one"]}, target=1))  # == 2                 #example #2
# print(tree_walker(tree={"one": [1, 2], "two": [{1: "one", 2: "two"}, [1, 2], "1", "one"]}, target=[1, 2]))  # == 2  #example #3
# print(tree_walker(tree=5, target=5))  # == 1


from typing import List

STEPS = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def lam(mp, a, b, islands, rs=0):
    for y in STEPS:
        a1, b1 = a + y[0], b + y[1]
        if 0 <= a1 < len(mp) and 0 <= b1 < len(mp[0]) and mp[a1][b1] == 1 and [a1, b1] not in islands:
            islands.append([a1, b1])
            rs += 1
            rs, islands = lam(mp, a1, b1, islands, rs)
    return rs, islands


def checkio(mp: List[List[int]]) -> List[int]:
    islands, res = [], []
    for a, row in enumerate(mp):
        for b, x in enumerate(row):
            if x == 1 and [a, b] not in islands:
                islands.append([a, b])
                rs, islands = lam(mp, a, b, islands)
                res.append(rs + 1)
    return sorted(res)


# print(checkio([[1, 1, 1, 1, 0, 1, 1, 1, 1]]))  # == [4, 4]
# print(checkio([[0,0,0,0,0],[0,0,1,1,0],[0,0,0,1,0],[0,1,0,0,0],[0,0,0,0,0]]))
# print(checkio([[1],[1],[1],[1],[1],[1],[1],[1],[1]]))


def digit_stack(coms):
    stack, res = [], 0
    for x in coms:
        if 'PUSH' in x:
            stack.append(int(x.replace('PUSH ', '')))
        elif x == 'PEEK' and stack:
            res += stack[-1]
        elif x == 'POP' and stack:
            res += stack.pop()
    return res


# print(digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]))  # == 8
# print(digit_stack(["POP", "POP"]))  # == 0
# print(digit_stack(["PUSH 9", "PUSH 9", "POP"]))  # == 9
# print(digit_stack([]))  # == 0)


def checkio(n):
    radix = int(max(n), 36) + 1
    for x in range(radix, 37):
        if int(n, x) % (x - 1) == 0:
            return x
    return 0


# print(checkio(u"18"))  # == 10
# print(checkio(u"1010101011"))  # == 2
# print(checkio(u"222"))  # == 3
# print(checkio(u"A23B"))  # == 14
# print(checkio(u"IDDQD"))  # == 0


















def encode(message, key):
    return message


def decode(secret_message, key):
    return secret_message

# print(encode("Fizz Buzz is x89 XX.", "checkio101"))  # == "do2y7mt22kry94y2y2"
# print(decode("do2y7mt22kry94y2y2", "checkio101"))  # == "fizxzbuzzisx89xzxz"
