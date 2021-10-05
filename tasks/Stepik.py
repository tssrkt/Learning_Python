def check(s):
    brackets = ['(', '[', '{', ')', ']', '}']
    nums = [x for x in range(len(s))]

    x = 0
    while x < len(s):
        if s[x] in brackets:
            x += 1
            continue
        else:
            del nums[x]
            s = s.replace(s[x], '', 1)

    while '()' in s or '[]' in s or '{}' in s:
        if '()' in s:
            del nums[s.find('()')], nums[s.find('()')]
            s = s.replace('()', '')
        if '[]' in s:
            del nums[s.find('[]')], nums[s.find('[]')]
            s = s.replace('[]', '')
        if '{}' in s:
            del nums[s.find('{}')], nums[s.find('{}')]
            s = s.replace('{}', '')

    if s == '': return 'Success'

    opening = []
    closing = []
    for x in s:
        if x in brackets[0:3]:
            opening.append(nums[s.index(x)] + 1)
        elif x in brackets[3:]:
            closing.append(nums[s.index(x)] + 1)

    if closing != []:
        return min(closing)
    return min(opening)


print(check("([](){([])})"))  # == 0
print(check("()[]}"))  # == 5
print(check("{{[()]]"))  # == 7
print(check("{{{[][][]"))  # == 3
print(check("{*{{}"))  # == 3
print(check("[[*"))  # == 2
print(check("{*}"))  # == 0
print(check("{{"))  # == 2
print(check("{}"))  # == 0
print(check(""))  # == 0
print(check("}"))  # == 1
print(check("*{}"))  # == 0
print(check("{{{**[][][]"))  # == 3


