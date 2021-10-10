def matryoshka(n):
    if n==1:
        print('Matryoshechka')
    else:
        print('Top of matryoshka n=', n)
        matryoshka(n-1)
        print('Beneath of matryoshka n=', n)


import graphics as gr
window = gr.GraphWin('Russian game', 600, 600)
alpha = 0.2

def fractal_rectangle(a,b,c,d, deep=10):
    if deep<1:
        return
    for m,n in (a, b), (b, c), (c, d), (d, a):
        gr.Line(gr.Point(*m), gr.Point(*n)).draw(window)
    a1 = (a[0]*(1-alpha) + b[0]*alpha, a[1]*(1-alpha) + b[1]*alpha)
    b1 = (b[0]*(1-alpha) + c[0]*alpha, b[1]*(1-alpha) + c[1]*alpha)
    c1 = (c[0] * (1 - alpha) + d[0] * alpha, c[1] * (1 - alpha) + d[1] * alpha)
    d1 = (d[0]*(1-alpha) + a[0]*alpha, d[1]*(1-alpha) + a[1]*alpha)
    fractal_rectangle(a1, b1, c1, d1, deep-1)

fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500), 10)

my_rectangle = gr.Rectangle(gr.Point(2, 4), gr.Point(4, 8))
my_rectangle.draw(window)


#####################################################################


# Алгоритм Евклида
# Два отрезка а и в, какой отрезок кратный обоим?
def evklid(a, b):
    return min(a, b) if not max(a, b)%min(a, b) else 'No NOD in this case'

print(evklid(3, 9))
print(evklid(10, 7))


###############################################################################

# Рекурсивный проход по дереву

def gen_bin(m, prefix=''):
    if m == 0:
        print(prefix)
    else:
        gen_bin(m-1, prefix+'0')
        gen_bin(m-1, prefix+'1')

def generate_nums(n:int, m:int, prefix=None):
    """
    Генерит все числа (с лидирующими незначащими нулями)
    в n-ричной системе счисления.
    :param n: n <= 10
    :param m: длина
    :param prefix:
    :return:
    """
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for digit in range(n):
        prefix.append(digit)
        generate_nums(n, m-1, prefix)
        prefix.pop()

print()
print('Fibochka')
n = 20
fib = [0, 1] + [0] * (n-1)
for i in range(2, n+1):
    fib[i] = fib[i-1]+fib[i-2]
    print(fib[i])

################################################################################################
print()

def lcs(a, b):
    f = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1]==b[j-1]:
                f[i][j]=1+f[i-1][j-1]
            else:
                f[i][j]=max(f[i-1][j], f[i][j-1])
    return f[-1][-1]

print(lcs([3,4,6,54,2], [2,3,4,5,2]))


#############################################################################################


def gis(a):
    f = [0]*(len(a)+1)
    for i in range(1, len(a)+1):
        m = 0
        for j in range(0, i):
            if a[i]>a[j] and f[j]>m:
                m = f[j]
        f[i] = m + 1
        return f[len(a)]

###########################################################################################
# Backpack
# Алгоритм дискретной укладки рюкзака
# Алгоритм Левенштейна

def levenstein(a, b):
    f = [[(i+j) if i*j==0 else 0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1]==b[j-1]:
                f[i][j]=f[i-1][j-1]
            else:
                f[i][j]=1+min(f[i-1][j], f[i][j-1], f[i-1][j-1])
    return f[len(a)][len(b)]


print([1,2,3,4], [4,5,6,7,8])


# Алгоритм Кнута-Морриса-Пратта (КМП)

######################################################################################

# BRACKETS
def check_brackets(s):
    """ Is brackets sequence correct? """
    stack = []
    for brace in s:
        if brace not in '()[]':
            continue
        if brace in '([':
            stack.append(brace)
        else:
            assert brace in ')]', 'Катасрофа! Ожидалась закрывающаяся скобка: ' + str(brace)
            if stack==[]:
                return False
            left = stack.pop()
            assert left in '([', 'Ожидалась открывающая скобка: ' + str(brace)
            if left == '(':
                right = ')'
            elif left == '[':
                right = ']'
            if right != brace:
                return False
    return stack==[]

print()
print('BRACKETS')
print(check_brackets('(([()]))[]()'))  # == True
print(check_brackets('([)]()[]'))  # == False
print(check_brackets(')('))  # == False
print(check_brackets('[[]]))(('))  # == False
print(check_brackets('['))  # == False
print(check_brackets('((([[]'))  # == False
print(check_brackets('([()])()'))  # == True
