def matryoshka(n):
    if n == 1:
        print('Matryoshechka')
    else:
        print('Top of matryoshka n=', n)
        matryoshka(n - 1)
        print('Beneath of matryoshka n=', n)


import graphics as gr

# window = gr.GraphWin('Russian game', 600, 600)
alpha = 0.2


def fractal_rectangle(a, b, c, d, deep=10):
    if deep < 1:
        return
    for m, n in (a, b), (b, c), (c, d), (d, a):
        gr.Line(gr.Point(*m), gr.Point(*n)).draw(window)
    a1 = (a[0] * (1 - alpha) + b[0] * alpha, a[1] * (1 - alpha) + b[1] * alpha)
    b1 = (b[0] * (1 - alpha) + c[0] * alpha, b[1] * (1 - alpha) + c[1] * alpha)
    c1 = (c[0] * (1 - alpha) + d[0] * alpha, c[1] * (1 - alpha) + d[1] * alpha)
    d1 = (d[0] * (1 - alpha) + a[0] * alpha, d[1] * (1 - alpha) + a[1] * alpha)
    fractal_rectangle(a1, b1, c1, d1, deep - 1)


# fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500), 10)
#
# my_rectangle = gr.Rectangle(gr.Point(2, 4), gr.Point(4, 8))
# my_rectangle.draw(window)


#####################################################################


# Алгоритм Евклида
# Два отрезка а и в, какой отрезок кратный обоим?
def evklid(a, b):
    return min(a, b) if not max(a, b) % min(a, b) else 'No NOD in this case'


print(evklid(3, 9))
print(evklid(10, 7))


###############################################################################

# Рекурсивный проход по дереву

def gen_bin(m, prefix=''):
    if m == 0:
        print(prefix)
    else:
        gen_bin(m - 1, prefix + '0')
        gen_bin(m - 1, prefix + '1')


def generate_nums(n: int, m: int, prefix=None):
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
        generate_nums(n, m - 1, prefix)
        prefix.pop()


print()
print('Fibochka')
n = 20
fib = [0, 1] + [0] * (n - 1)
for i in range(2, n + 1):
    fib[i] = fib[i - 1] + fib[i - 2]
    print(fib[i])

################################################################################################
print()


def lcs(a, b):
    f = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = 1 + f[i - 1][j - 1]
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
    return f[-1][-1]


print(lcs([3, 4, 6, 54, 2], [2, 3, 4, 5, 2]))


#############################################################################################


def gis(a):
    f = [0] * (len(a) + 1)
    for i in range(1, len(a) + 1):
        m = 0
        for j in range(0, i):
            if a[i] > a[j] and f[j] > m:
                m = f[j]
        f[i] = m + 1
        return f[len(a)]


###########################################################################################
# Backpack
# Алгоритм дискретной укладки рюкзака
# Алгоритм Левенштейна

def levenstein(a, b):
    f = [[(i + j) if i * j == 0 else 0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1]
            else:
                f[i][j] = 1 + min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1])
    return f[len(a)][len(b)]


print([1, 2, 3, 4], [4, 5, 6, 7, 8])


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
            if stack == []:
                return False
            left = stack.pop()
            assert left in '([', 'Ожидалась открывающая скобка: ' + str(brace)
            if left == '(':
                right = ')'
            elif left == '[':
                right = ']'
            if right != brace:
                return False
    return stack == []


print()
print('BRACKETS')
print(check_brackets('(([()]))[]()'))  # == True
print(check_brackets('([)]()[]'))  # == False
print(check_brackets(')('))  # == False
print(check_brackets('[[]]))(('))  # == False
print(check_brackets('['))  # == False
print(check_brackets('((([[]'))  # == False
print(check_brackets('([()])()'))  # == True


# Графы
def dfs(vertex, G, used=None):
    used = used or set()
    used.add(vertex)
    for n in G[vertex]:
        if n not in used:
            dfs(n, G, used)


# Алгоритм Косарайю
# Выделение сильных компонентов графа
# u - number from 1 to N
visited = [False] * (n + 1)
G = [1, 2, 3, 4, 5]
ans = []


def dfs(start, G, visited, ans):
    visited[start] = True
    for u in G[start]:
        if not visited[u]:
            dfs(u, G, visited)
    ans.append(start)


# for i in range(1, n+1):
#     if not visited[i]:
#         dfs(i, G, visited, ans)
#
# ans[:] = ans[::-1]

# BFS - Обход Графов в Ширину
# n, m = map(int, input().split())
print()
print('Обход Графов в Ширину')
tup = ((0, 1), (0, 12), (0, 11), (0, 6), (1, 3), (1, 2), (2, 5), (2, 3), (4, 2), (7, 3), (8, 9), (10, 8))
vs = iter(tup)
n, m = 15, len(tup)

graph = {i: set() for i in range(n)}
for i in range(m):
    # v1, v2 = map(int, input().split())
    v1, v2 = next(vs)
    graph[v1].add(v2)
    graph[v2].add(v1)

from collections import deque

distances = [None] * n
start_vertex = 0
distances[start_vertex] = 0
queue = deque([start_vertex])
parents = [None] * n

while queue:
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        if distances[neigh_v] is None:
            distances[neigh_v] = distances[cur_v] + 1
            parents[neigh_v] = cur_v
            queue.append(neigh_v)

end_vertex = 9
path = [end_vertex]
parent = parents[end_vertex]
while not parent is None:
    path.append(parent)
    parent = parents[parent]

print(path)
print(distances)
print(parents)
for k, v in graph.items():
    print(k, v)

# Задача про шахматного коня
# Найти минимальный путь шахматного коня из одной клетки доски в другую
# from collections import deque
print()
print('Chess Horse')
letters = 'abcdefgh'
numbers = '12345678'
graph = {}

# 64 empty cells of chess desk
for i in letters:
    for n in numbers:
        graph[i + n] = set()

distances = {v: None for v in graph}
parents = {v: None for v in graph}
start_vertex = 'd4'
end_vertex = 'f7'

distances[start_vertex] = 0
queue = deque([start_vertex])


def add_edge(v1, v2):
    graph[v1].add(v2)
    graph[v2].add(v1)


for i in range(8):
    for j in range(8):
        v1 = letters[i] + numbers[j]
        v2 = ''
        if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i + 2] + numbers[j + 1]
            add_edge(v1, v2)
        if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i - 2] + numbers[j + 1]
            add_edge(v1, v2)
        if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i + 1] + numbers[j + 2]
            add_edge(v1, v2)
        if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i - 1] + numbers[j + 2]
            add_edge(v1, v2)

while queue:
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        if distances[neigh_v] is None:
            distances[neigh_v] = distances[cur_v] + 1
            parents[neigh_v] = cur_v
            queue.append(neigh_v)

path = [end_vertex]
parent = parents[end_vertex]
while not parent is None:
    path.append(parent)
    parent = parents[parent]

print('Path from d4 to f7:', path)

# Нахождение кратчайшего цикла
# 1. Обход в ширину из каждой вершины
# 2. Если пытаемся попасть в посещенную вершину - значит есть цикл
# 3. Запустив обход из каждой вершины выбираем кратчайший

# Нахождение всех вершин на кратчайшем пути (a, b)
# 1. Запускаем обходы в ширину из a и из b с подсчетом расстояний
# 2. Расстояния до вершины х храним как d_a[x] & d_b[x]
# 3. Если d_a[x] + d_b[x] = d_a[b], то вершина лежит на кратчайшем пути

# Кратчайший путь четной длины
# 1. Строим вспомогательный граф, каждая вершина е превращается в 2 вершины: е0 и е1
# 2. Каждое ребро (u, v) превращается в 2 ребра: (u0, v1) & (u1, v0)
# 3. Найти кратчайший путь четный путь из a & b == найти в новом графе кратчайший путь из a0 в b0

# Самая короткая цепочка друзей между пользователям ВК
# Получение данных: HTTP-запросы + VK API
# 1. Задаем id_start, id_end

print()


# print('VKONTAKTE BONUS')
# import requests
# import time
# from tqdm import tqdm
#
# HOST = 'https://api,vk.com/method/'
# VERSION = '5.74'
# access_token = ''
# r = requests.get(HOST + 'users.get', params = {'user_ids': '1699912, 1',
#                                                'access_token': access_token,
#                                                'v': VERSION})
# r_json = r.json()['response'][0]
# # {'first_name': 'Vasya', 'id': 1699912, 'last_name': 'Vasyliev'}
# id_start = 1699912
# id_end = 111900610
#
# def get_friends_list(id_user):
#     r = requests.get(HOST + 'users.get', params={'user_id': '1699912, 1',
#                                                  'access_token': access_token,
#                                                  'v': VERSION})
#
#     if 'response' in r.json():
#         return r.json()['response']['items']
#     return []
#
# # from collections import deque
# queue = deque(get_friends_list(id_start))
#
# distances = {v: 1 for v in graph}
# parents = {v: 111900610 for v in graph}
#
# while id_end not in distances:
#     cur_user = queue.popleft()
#     new_users = get_friends_list(cur_user)
#     time.sleep(0.2)
#     for u in tqdm(new_users):
#         if u not in distances:
#             queue.append(u)
#             distances[u] = distances[cur_user] + 1
#             parents[u] = cur_user

# print(parents)

##########################################################################################


# Алгоритм Дейкстры поиска кратчайшего расстояния в графе
# Обход графа в ширину с перезажиганием
# Требование: веса - положительные числа, ноль можно
# Асимптотика: O(N**2)
# Цель: поиск кратчайших путей от исходной вершины ко всем остальным


def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight


def read_graph():
    M = int(input())  # count of edges, and strings A, B and weight
    G = {}
    for i in range(M):
        a, b, weight = input().split()
        weight = float(weight)
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)
    return G


def dijkstra(G, start):
    Q = deque()
    S = {}
    S[start] = 0
    Q.push(start)
    while Q:
        v = Q.pop()
        for u in G[v]:
            if (u not in S) or (S[v] + G[v][u]) < S[u]:
                S[u] = S[v] + G[v][u]
                Q.push(u)


# Алгоритм Фледа-Уоршелла
# Тип динамическое программирование
# Цель: кратчайшие расстояния от каждой вершины к каждой
# Асимптотика: O(N**3)
# Работает даже если есть отрицательные веса, но не с циклами отрицательного веса

# ДЕРЕВЬЯ
# Дерево - это граф без циклов
# Двоичное дерево - корневое дерево, где у каждой вершины не больше 2 детей
# H (высота дерева) - это максимальное количество ребер от корня до листа
# Упорядоченное дерево - порядок дочерних вершин имеет значение
# Двоичное дерево поиска (у каждой вершины есть ключ) - структура данных,
# хранящая в вершинах элементы, содержащие ключ, при этом на множестве ключей есть
# операция сравнимости (можно ключ к1 сравнить с ключом к2)
a = [7, 3, 9, 5, 4, 1, 2, 8, 6, 10, 12]
# 7 is root
# 3 is left from root because 3<7
# 9 is right from root because 9>7
# 5 is right form 3 because 5<7 and 5>3
# less - left, bigger - right
# height of tree k = (2**k+1) - 1

# Балансировка (сделать так чтобы у каждого узла по два ребенка, а не по одному в одну сторону)
# Дерево сбалансировано если для каждой вершины высота ее левого и правого поддеревьев отличается
# не более чем на единицу.
# Алгоритмы балансировки:
# 1. АВЛ-дерево
# 2. Красно-черное двоичное дерево поиска

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# Эйлеров цикл - это цикл, который проходит через каждое ребро графа один раз.
# Эйлеров граф - в нем есть Эйлеров цикл.
# Признаки: 1) Связный. 2) Все степени вершин четные.

# Гамильтонов цикл - это цикл, который проходит через каждую вершину графа, но не каждое ребро один раз.
# Гамильтонов граф - граф с Гамильтоновым циклом. Задача NP полна.

# Жадный алгоритм Дейкстры

# Алгоритм Флойда-Уоршелла





# def main():
#     G = read_graph()
#     start = input('Insert start vertex: ')
#     while start not in G:
#         start = input('This vertex is not in graph. Insert correct start vertex: ')
#     shortest_distances = dijkstra(G, start)
#     finish = input('From which vertex should we start the path?')
#     while finish not in G:
#         start = input('This vertex is not in graph. Insert correct end vertex: ')
#     shortest_path = reveal_shortest_path(start, finish, shortest_distances)
#
# if __name__ = '__main__':
#     main()
