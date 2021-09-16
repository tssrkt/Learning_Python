class Warrior:
    def __init__(self):
        self.max_health = 50
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        return False


class Lancer(Warrior):
    # первому, стоящему перед ним сопернику, он наносит урон в размере 100% своей атаки
    # (с учетом защиты соперника, если она есть), а сопернику, который стоит позади - 50% от
    # нанесенного урона (защита соперника уменьшает наносимый копейщиком урон и,
    # соответственно, получаемый вторым юнитом урон).
    def __init__(self):
        self.attack = 6
        self.health = 50


class Vampire(Warrior):
    def __init__(self):
        self.max_health = 40
        self.health = 40
        self.attack = 4
        self.vampirism = 50


class Defender(Warrior):
    def __init__(self):
        self.max_health = 60
        self.health = 60
        self.attack = 3
        self.defense = 2


class Knight(Warrior):
    def __init__(self):
        self.attack = 7


class Healer(Warrior):
    # Каждый раз, когда союзный солдат бьет врага, Healer, стоящий позади союзника лечит его на +2
    # единицы здоровья. При этом исцеление не может поднять здоровье выше максимального уровня.
    def __init__(self):
        self.max_health = 60
        self.health = 60
        self.attack = 0
        self.heal_pwr = 2

    def heal(self, unit):
        unit.health = min(unit.max_health, unit.health + self.heal_pwr)


def fight(unit_1, unit_2, healer_1=False, healer_2=False):
    damage = 0
    while unit_1.is_alive and unit_2.is_alive:
        if type(unit_2) == Defender:
            if unit_1.attack > unit_2.defense:
                damage = unit_1.attack - unit_2.defense
                unit_2.health -= damage
        else:
            damage = unit_1.attack
            unit_2.health -= damage

        if type(unit_1) == Vampire and damage != 0:
            unit_1.health += int(damage * unit_1.vampirism / 100)
            if unit_1.health > unit_1.max_health:
                unit_1.health = unit_1.max_health

        if unit_1.is_alive and healer_1:
            healer_1.heal(unit_1)

        # Если второй воин (которого ударили) еще живой
        if unit_2.is_alive:
            if type(unit_1) == Defender:
                if unit_2.attack > unit_1.defense:
                    damage = unit_2.attack - unit_1.defense
                    unit_1.health -= damage

            else:
                damage = unit_2.attack
                unit_1.health -= damage

            if type(unit_2) == Vampire and damage != 0:
                unit_2.health += (damage / int(100 / unit_2.vampirism))
                if unit_1.health > unit_1.max_health:
                    unit_1.health = unit_1.max_health

            if unit_2.is_alive and healer_2:
                healer_2.heal(unit_2)

    if unit_1.is_alive and not unit_2.is_alive:
        return True
    return False


class Army:
    def __init__(self):
        self.units = []
    def add_units(self, units, count):
        for x in range(count):
            self.units.append(units())


def lancer_attack(lancer, enemy):
    damage = 0
    if type(enemy) == Defender and lancer.attack > enemy.defense:
        damage = lancer.attack/2 - enemy.defense
    else:
        damage = lancer.attack/2
    enemy.health -= damage
    return enemy


class Battle():
    def fight(self, army1, army2):
        if isinstance(army1, Army) and isinstance(army2, Army):
            x, y = 0, 0
            healer_1 = army1.units[x + 1] if x + 1 < len(army1.units) and type(army1.units[x + 1]) == Healer else False
            healer_2 = army2.units[y + 1] if y + 1 < len(army2.units) and type(army2.units[y + 1]) == Healer else False
            first_win = fight(army1.units[x], army2.units[y], healer_1, healer_2)
            if type(army1.units[x]) == Lancer:
                army2.units[y] = lancer_attack(army1.units[x], army2.units[y])
            if type(army2.units[y]) == Lancer:
                army1.units[x] = lancer_attack(army2.units[y], army1.units[x])

            while True:
                if first_win:
                    if y < len(army2.units) - 1:
                        y += 1
                    else:
                        return True
                else:
                    if x < len(army1.units) - 1:
                        x += 1
                    else:
                        return False
                healer_1 = army1.units[x + 1] if x+1<len(army1.units) and type(army1.units[x + 1]) == Healer else False
                healer_2 = army2.units[y + 1] if y+1<len(army2.units) and type(army2.units[y + 1]) == Healer else False
                first_win = fight(army1.units[x], army2.units[y], healer_1, healer_2)
                if type(army1.units[x]) == Lancer:
                    army2.units[y] = lancer_attack(army1.units[x], army2.units[y])
                if type(army2.units[y]) == Lancer:
                    army1.units[x] = lancer_attack(army2.units[y], army1.units[x])
        else:
            print('Not correct input!')


army_1 = Army()
army_2 = Army()
army_1.add_units(Lancer, 7)
army_1.add_units(Vampire, 3)
army_1.add_units(Healer, 1)
army_1.add_units(Warrior, 4)
army_1.add_units(Healer, 1)
army_1.add_units(Defender, 2)

army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 4)
army_2.add_units(Healer, 1)
army_2.add_units(Vampire, 6)
army_2.add_units(Lancer, 4)
battle = Battle()

print(battle.fight(army_1, army_2))  #

chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

print(fight(chuck, bruce))  # == True
print(fight(dave, carl))  # == False
print(chuck.is_alive)  # == True
print(bruce.is_alive)  # == False
print(carl.is_alive)  # == True
print(dave.is_alive)  # == False
print(fight(carl, mark))  # == False
print(carl.is_alive)  # == False

my_army = Army()
my_army.add_units(Knight, 3)

enemy_army = Army()
enemy_army.add_units(Warrior, 3)

army_3 = Army()
army_3.add_units(Warrior, 20)
army_3.add_units(Knight, 5)

army_4 = Army()
army_4.add_units(Warrior, 30)

battle = Battle()

print(battle.fight(my_army, enemy_army))  # == True
print(battle.fight(army_3, army_4))  # == False

carl = Warrior()
jim = Knight()
# print(fight(carl, jim))

bob = Warrior()
mars = Warrior()


# print(fight(bob, mars))


