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
                    s2, reserve_nums = yama(br[x+1], s2, nums)
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
        if '()' in s2: x = '()'
        elif '[]' in s2: x = '[]'
        elif '{}' in s2: x = '{}'
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
    while s2!='':
        s2, r_nums = lopata(s2, nums)
        reserve_nums.extend(r_nums)
        for x in reserve_nums:
            if x in nums:
                nums.remove(x)
        s2, nums = bandura(s2, nums)
        w += 1
        if w>=4 and s2!='':
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
    if hour<6 or hour>18 or hour==18 and minute>0: return "I don't see the sun!"
    ans = abs((hour * 15 + minute * 0.25))
    return abs(90 - ans)

# print(sun_angle("07:00"))  # == 15
# print(sun_angle("12:00"))
# print(sun_angle("12:01"))
# print(sun_angle("12:15"))  # == 93.75
# print(sun_angle("01:23"))  # == "I don't see the sun!")











def checkio(data):
    """ Cargo """
    #replace this for solution
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
        if type(v)==dict:
            if v=={}: res.append([k, ''])
            else:
                flat = sakura(v)
    if flat:
        for x in flat:
            pass
    return res

def flatten(dic):
    res = {}
    for k, v in dic.items():
        if type(v)==dict:
            if v=={}: res.setdefault(k, '')
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
    if wr_time==None:
        st_time, wr_time, error = st_time[0], st_time[1], st_time[2]

    from datetime import datetime, timedelta
    times = ['hours', 'minutes', 'seconds']
    zeros = ['00', '00', '00']
    wr, tms1, at, each, tms2 = error.split()
    wr1, each2 = int(wr[1:]), int(each)
    wr = str(wr1) if wr1>9 else '0' + str(wr1)
    each = each if each2>9 else '0' + each

    n1 = [times.index(x) for x in times if tms1 in x][0]
    n2 = [times.index(x) for x in times if tms2 in x][0]

    wr = ':'.join([x if tms1 not in times[n] else wr for n, x in enumerate(zeros)])
    each = ':'.join([x if tms2 not in times[n] else each for n, x in enumerate(zeros)])
    tmdelta = [timedelta(hours=wr1), timedelta(minutes=wr1), timedelta(seconds=wr1)][n1]

    # Если на вход дали ерунду, приводим ее в божеский вид
    if each2>60:
        adyn, dva = divmod(each2, 60)
        if adyn<60:
            each = f'00:{adyn}:{dva}' if tms2 in 'seconds' else f'{adyn}:{dva}:00'
        else:
            while adyn>60:
                tri, adyn = divmod(adyn, 60)
            each = f'{tri}:{adyn}:{dva}'

    tm = str(datetime.strptime(wr_time, '%H:%M:%S') - datetime.strptime(st_time, '%H:%M:%S'))
    if error[0]=='-':
        lol = str(datetime.strptime(each, '%H:%M:%S') - datetime.strptime(wr, '%H:%M:%S'))
    else:
        lol = str(datetime.strptime(each, '%H:%M:%S') + tmdelta)[-8:]

    # Все переводим в секунды
    lol_secs, tm_secs, each_secs = 0, 0, 0
    mnoj = [3600, 60, 1]
    tm_lst = tm.split(':')
    for n, x in enumerate(lol.split(':')):
        lol_secs += int(x)*mnoj[n]
        tm_secs += int(tm_lst[n])*mnoj[n]
        each_secs = each2*mnoj[n] if n==n2 else each_secs

    secs = int((tm_secs/lol_secs)*each_secs)
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
        if x=='a':
            if up: up = False
            else: up = True
        else:
            if up and x.isupper(): res += x.lower()
            elif up and x.islower(): res += x.upper()
            else: res += x
    return res


# print(caps_lock("Why are you asking me that?"))  # == "Why RE YOU sking me thT?"
# print(caps_lock("Madder than Mad Brian of Madcastle"))  # == "MDDER THn MD BRIn of MDCstle"

def decode_vigenere(od, oe, nw):
    from string import ascii_uppercase as alf

    word = ''
    for n, x in enumerate(od):
        a = alf.index(oe[n]) - alf.index(x)
        word += alf[a]

    if len(nw)>len(od):
        fr_word = {}
        for x in range(2, len(word)):
            fr_word[word[0:x]] = word.count(word[0:x])

        for x in fr_word.keys():
            if x==word[len(x):(len(x))*2]:
                word = x

        word = word*len(nw) if len(nw)>len(word) else word

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
    text = ' '.join(text.split())
    if len(text.split())==1 and len(text)>39:
        a = []
        while len(text)>39:
            a.append(text[:39])
            text = text[39:]
        a.append(text)
        text = ' '.join(a)
    n = 41 if len(text) >= 40 else len(text)+2
    res = '\n ' + '_' * n + '\n'
    if len(text)<40: res += '< ' + text + ' >\n'
    else:
        a = []
        line, line2 = [], []
        ready = False
        for word in text.split():
            line.append(word)
            while len(' '.join(line))>39:
                line2.append(line.pop())
                ready = True
            if ready:
                a.append(' '.join(line))
                line, ready = line2, False
                line2 = []
        a.append(' '.join(line))

        res += '/ ' + a[0] + ' '*(39-len(a[0])) + ' \\\n'
        if len(a)>2:
            for x in a[1:-1]:
                res += '| ' + x + ' '*(39-len(x)) + ' |\n'
        res += '\\ ' + a[-1] + ' '*(39-len(a[-1])) + ' /\n'
    res += ' ' + '-'*n + COW
    return res

print(cowsay("onehundredtwentytwo and one hundredfiftyone"))
print(cowsay("looooooooooooooooooooooooooooooooooooong"))
print(cowsay("loooooooooooooooooooooooooooooooooooong"))
print(cowsay("loooooooooooooooooooooooooooooooooooong"))
print(cowsay("spaces                           inside"))
print(cowsay('Your bunny wrote'))
print(cowsay('A longtextwithonlyonespacetofittwolines.'))
print(cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'))\

"""

 _________________________________________
/ looooooooooooooooooooooooooooooooooooon \
\ g                                       /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""





