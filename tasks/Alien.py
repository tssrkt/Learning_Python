class Warrior:
    def __init__(self):
        self.health = 50
        self.max_health = self.health
        self.attack = 5
        self.defense = 0
        self.is_alive = True
        self.vampirism = 0
        self.longhit = 0
        self.acumdam = 0
        self.heal_pwr = 0

    def check(self):
        if self.health <= 0:
            self.is_alive = False

    def heal(self, unit):
        unit.health = min(unit.max_health, unit.health + self.heal_pwr)


class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack = 3
        self.defense = 2
        self.health = 60
        self.max_health = self.health


class Vampire(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack = 4
        self.health = 40
        self.max_health = self.health
        self.vampirism = 0.5


class Lancer(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack = 6
        self.longhit = 0.5


class Healer(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack = 0
        self.heal_pwr = 2
        self.health = 60
        self.max_health = self.health


class Army:
    def __init__(self):
        self.forces = []

    def add_units(self, type, number):
        for i in range(number):
            self.forces.append(type())


class Battle:
    def fight(self, army1, army2):
        while army1.forces and army2.forces:
            if len(army1.forces) > 1 and len(army2.forces) > 1:
                fight(army1.forces[0], army2.forces[0], army1.forces[1], army2.forces[1])
            elif len(army1.forces) > 1:
                fight(army1.forces[0], army2.forces[0], army1.forces[1])
            elif len(army2.forces) > 1:
                fight(army1.forces[0], army2.forces[0], 0, army2.forces[1])
            else:
                fight(army1.forces[0], army2.forces[0])
            if len(army1.forces) > 1:
                army1.forces[1].health -= army1.forces[0].acumdam
                army1.forces[0].acumdam = 0
                if army1.forces[1].is_alive == False:
                    del army1.forces[1]
            if len(army2.forces) > 1:
                army2.forces[1].health -= army2.forces[0].acumdam
                army2.forces[0].acumdam = 0
                if army2.forces[1].is_alive == False:
                    del army2.forces[1]
            if army1.forces[0].is_alive == True:
                del army2.forces[0]
            else:
                del army1.forces[0]
        if army1.forces:
            return True
        return False


def fight(u1, u2, *args):
    i = 0
    while u1.health > 0 and u2.health > 0:
        if i % 2 == 0:
            u2.health -= max(u1.attack - u2.defense, 0)
            u2.acumdam += max(u1.attack - u2.defense, 0) * u1.longhit
            u1.health += max(u1.attack - u2.defense, 0) * u1.vampirism
            if len(args) > 0 and args[0] != 0:
                args[0].heal(u1)
        else:
            u1.health -= max(u2.attack - u1.defense, 0)
            u1.acumdam += max(u2.attack - u1.defense, 0) * u2.longhit
            u2.health += max(u2.attack - u1.defense, 0) * u2.vampirism
            if len(args) > 1:
                args[1].heal(u2)
        i += 1
    u1.check()
    u2.check()
    if u1.is_alive == True:
        return True
    return False

# print('WARRIORS')
# army_1 = Army()
# army_2 = Army()
# # army_1.add_units(Lancer, 7)
# army_1.add_units(Vampire, 1)
# army_1.add_units(Healer, 1)
# army_1.add_units(Warrior, 4)
# army_1.add_units(Healer, 1)
# army_1.add_units(Defender, 2)
#
# # army_2.add_units(Warrior, 4)
# army_2.add_units(Defender, 1)
# army_2.add_units(Healer, 1)
# army_2.add_units(Vampire, 6)
# army_2.add_units(Lancer, 4)
# battle = Battle()
#
# print(battle.fight(army_1, army_2))  #

# Palindromic Palindrome
"f\";]1-::[s==s:s adbmal=oikcehc;";checkio=lambda s:s==s[::-1];"\f"


# Cipher Map
def recall_password(grille, password):
    answer = ""
    for _ in range(4):
        answer += ''.join([password[r][c] for r in range(4) for c in range(4) if grille[r][c] == 'X'])
        grille = list(map(''.join, zip(*grille[::-1])))
    return answer

##############################################################################

# перевод координат из строки в пару (ряд, столбец): "b1" -> (0,1)
str2coord = lambda s: (int(s[1])-1, ord(s[0])-ord('a'))
# обратная функция
coord2str = lambda c: chr(c[1]+ord('a'))+str(c[0]+1)

# проверка что 2 ферзя не бьют труг друга
def can_be_placed(p1, p2):
    (r1,c1), (r2,c2) = p1, p2
    return r1 != r2 and c1 != c2 and abs(r2-r1) != abs(c2-c1)

# проверка что новый ферзь не бьёт ни один из уже установленных
can_be_placed_on_board = lambda queens, pos: all(can_be_placed(p, pos) for p in queens)
# проверка на занятость ряда
is_row_occupied = lambda queens, r: sum(1 for p in queens if p[0]==r)

def place_one_queen(queens, r):
    # в списке 8 ферзей - значит всех расставили
    if len(queens) == 8: return set(map(coord2str, queens))
    # вышли за границу доски - тут нам делать нечего
    if r == 8: return set()
    if is_row_occupied(queens, r):
        # в текущем ряду уже занято - попытаемся в следующем
        return place_one_queen(queens, r+1)
    for c in range(8):
        # идём по столбцам и пытаемся поставить ферзя
        if can_be_placed_on_board(queens, (r,c)):
            # можно поставить - ставим и переходим на следующий ряд
            result = place_one_queen(queens+[(r,c)], r+1)
            # вернулись с результатом - значит дальше можно не искать - возвращаемся и передаём результат выше
            if result: return result

def place_queens(positions):
    queens = []
    # размещаем исходных ферзей и проверяем, что они не бьют друг друга
    for pos in positions:
        coord = str2coord(pos)
        if not can_be_placed_on_board(queens, coord):
            return set()
        queens.append(coord)

    res = place_one_queen(queens, 0)
    return res if res else set()

# просто печатаем положение ферзей на доске (для наглядности)
def print_board(queens):
    coords = list(map(str2coord, queens))
    print(' ', *list(map(chr, range(65, 65+8))))
    for r in range(7,-1,-1):
        print(r+1, end=' ')
        for c in range(8):
            print('X' if (r,c) in coords else '*', end=' ')
        print(r+1)
    print(' ', *list(map(chr, range(65, 65+8))))

print(place_queens({"b1", "c4", "d6", "e8"}))
print(place_queens({"b2", "c4", "d6", "e8"}))  # {"b2", "c4", "d6", "e8", "a5", "f3", "g1", "h7"},
print(place_queens({"b2", "c4", "d6", "e8", "a7", "g5"})) # == set())
print(place_queens(["b2", "c4", "d6", "e8"]))
# "answer": [["b2", "c4", "d6", "e8"], True],
# "show": '{"b2", "c4", "d6", "e8"}'
print(place_queens(["b2", "c4", "d6", "e8", "a7", "g5"]))
# "answer": [["b2", "c4", "d6", "e8", "a7", "g5"], False],
# "show": '{"b2", "c4", "d6", "e8", "a7", "g5"}'
print(place_queens(["a5", "b7", "c1", "e2", "f8", "g6", "h3"]))
# "answer": [["a5", "b7", "c1", "e2", "f8", "g6", "h3"], True],
# "show": '{"a5", "b7", "c1", "e2", "f8", "g6", "h3"}'
print(place_queens(["a1", "h8"]))
# "answer": [["a1", "h8"], False],
# "show": '{"a1", "h8"}'
print(place_queens(["d5"]))
# "answer": [["d5"], True],
# "show": '{"d5"}'
print(place_queens(["b2", "f7"]))
# "answer": [["b2", "f7"], True],
# "show": '{"b2", "f7"}'
print(place_queens(["b3", "d4", "f5"]))
# "answer": [["b3", "d4", "f5"], False],
# "show": '{"b3", "d4", "f5"}'
print(place_queens(["b3", "d2", "f5"]))
# "answer": [["b3", "d2", "f5"], True],
# "show": '{"b3", "d2", "f5"}'
print(place_queens(["a4", "g8", "h2", "e1", "f6"]))
# "answer": [["a4", "g8", "h2", "e1", "f6"], True],
# "show": '{"a4", "g8", "h2", "e1", "f6"}'
print(place_queens(["c3", "d3", "e3", "f3"]))
# "answer": [["c3", "d3", "e3", "f3"], False],
# "show": '{"c3", "d3", "e3", "f3"}'
print(place_queens(["d5", "d7", "e1"]))
# "answer": [["d5", "d7", "e1"], False],
# "show": '{"d5", "d7", "e1"}'

def life_counter(state, tick_n):
    AROUND = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    lives = {(r,c) for r in range(len(state)) for c in range(len(state[0])) if state[r][c]}
    for _ in range(tick_n):
        death,born = set(),dict()
        for r,c in lives:
            neighbors = 0
            for rc in [(r+dr,c+dc) for dr,dc in AROUND]:
                if rc in lives:
                    neighbors += 1
                else:
                    born[rc] = 1 if rc not in born else born[rc]+1
            if neighbors<2 or neighbors>3:
                death.add((r,c))
        lives -= death
        lives |= {rc for rc in born if born[rc]==3}
    return len(lives)

def checkio(number):
    'return roman numeral using the specified integer value from range 1...3999'
    roman = ''
    romanmappings = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
                     40: "XL", 50: "L", 90: "XC", 100: "C",
                     400: "CD", 500: "D", 900: "CM", 1000: "M" }
    for intVal in sorted(list(romanmappings.keys()), reverse=True):
        while number >= intVal:
            roman += romanmappings[intVal]
            number -= intVal
    return roman

###############

import re

def is_stressful(subj):
    return (subj.isupper() or
            subj.endswith('!!!') or
            any(re.search('+[.!-]*'.join(c for c in word), subj.lower())
                for word in ['help', 'asap', 'urgent']))


# print(is_stressful("HI HOW ARE YOU?"))  # == True
# print(is_stressful("UUUURGGGEEEEENT here"))  # == True
# print(is_stressful("Hi"))  # == False
# print(is_stressful("I neeed HELP"))  # == True
# print(is_stressful("HELP"))  # == True
# print(is_stressful("Attention!!!"))  # == True
# print(is_stressful("HHHEEEEEEEEELLP"))  # == True
# print(is_stressful("H-E-L-P"))  # == True
# print(is_stressful("H! E! L! P!"))  # == True

from typing import Iterable, List, Tuple, Union
Node = Union[int, str]
Tree = Tuple[Node, List['Tree']]

def on_same_path(tree: Tree, pairs: List[Tuple[Node, Node]]) -> Iterable[bool]:
    def walk(pair, tree, path):
        return (
            tree[0] == pair[0] and pair[1] in path
            or
            tree[0] == pair[1] and pair[0] in path
            or
            any(walk(pair, subtree, path + [tree[0]]) for subtree in tree[1])
        )
    return [walk(pair, tree, []) for pair in pairs]

print(on_same_path([1,[[2,[[4,[]],[5,[[7,[]],[8,[]],[9,[]]]]]],[3,[[6,[]]]]]],[[1,5],[2,9],[2,6]]))
print(on_same_path(
    ('Me', [('Daddy', [('Grandpa', []),
                       ('Grandma', [])]),
            ('Mom', [('Granny', []),
                     ('?', [])])]),
    [('Grandpa', 'Me'), ('Daddy', 'Granny')],))  # == [True, False])
