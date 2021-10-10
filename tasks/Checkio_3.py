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
            reserve_nums.append(0)
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





