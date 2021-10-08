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

fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500), 100)

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


