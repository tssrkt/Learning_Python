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



