class Warrior:
    def __init__(self):
        self.health = 50
        self.max_health = 50
        self.attack = 5

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def equip_weapon(self, weapon):
        self.health += weapon.health
        self.max_health += weapon.health
        self.attack += weapon.attack

        if hasattr(self, 'vampirism') and hasattr(weapon, 'vampirism'):
            self.vampirism += weapon.vampirism

        if hasattr(self, 'defense') and hasattr(weapon, 'vampirism'):
            self.defense += weapon.defense

        if hasattr(self, 'heal_power') and hasattr(weapon, 'vampirism'):
            self.heal_power += weapon.heal_power


class Rookie(Warrior):
    pass


class Lancer(Warrior):
    # первому, стоящему перед ним сопернику, он наносит урон в размере 100% своей атаки
    # (с учетом защиты соперника, если она есть), а сопернику, который стоит позади - 50% от
    # нанесенного урона (защита соперника уменьшает наносимый копейщиком урон и,
    # соответственно, получаемый вторым юнитом урон).
    def __init__(self):
        super().__init__()
        self.attack = 6


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.max_health = 40
        self.health = 40
        self.attack = 4
        self.vampirism = 50


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.max_health = 60
        self.health = 60
        self.attack = 3
        self.defense = 2


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Healer(Warrior):
    # Каждый раз, когда союзный солдат бьет врага, Healer, стоящий позади союзника лечит его на +2
    # единицы здоровья. При этом исцеление не может поднять здоровье выше максимального уровня.
    def __init__(self):
        super().__init__()
        self.max_health = 60
        self.health = 60
        self.attack = 0
        self.heal_pwr = 2

    def heal(self, unit):
        unit.health = min(unit.max_health, unit.health + self.heal_pwr)


class Warlord(Warrior):
    def __init__(self):
        super().__init__()
        self.max_health = 100
        self.health = 100
        self.attack = 4
        self.defense = 2

########################################################################


class Weapon:
    def __init__(self, health, attack, defense, vampirism, heal_power):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power

class Sword(Weapon):
    def __init__(self):
        self.health = 5
        self.attack = 2

class Shield(Weapon):
    def __init__(self):
        self.health = 20
        self.attack = -1
        self.defense = 2

class GreatAxe(Weapon):
    def __init__(self):
        self.health = -15
        self.attack = 5
        self.defense = -2
        self.vampirism = 10

class Katana(Weapon):
    def __init__(self):
        self.health = -20
        self.attack = 6
        self.defense = -5
        self.vampirism = 10

class MagicWand(Weapon):
    def __init__(self):
        self.health = 30
        self.attack = 3
        self.heal_power = 3


########################################################################

def lancer_attack(lancer, enemy):
    damage = 0
    if type(enemy) == Defender and lancer.attack > enemy.defense:
        damage = lancer.attack/2 - enemy.defense
    else:
        damage = lancer.attack/2
    enemy.health -= damage
    return enemy

def fight(unit_1, unit_2, i=0, army1=False, army2=False, healer_1=False, healer_2=False):
    damage = 0
    while unit_1.is_alive and unit_2.is_alive:
        if army1 and army2 and type(unit_1) == Lancer and len(army2.units)-1>i:
            army2.units[i+1] = lancer_attack(army1.units[i], army2.units[i+1])

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
            if army1 and army2 and type(unit_2) == Lancer and len(army1.units)-1>i:
                army1.units[i+1] = lancer_attack(army2.units[i], army1.units[i+1])

            if type(unit_1) == Defender:
                if unit_2.attack > unit_1.defense:
                    damage = unit_2.attack - unit_1.defense
                    unit_1.health -= damage

            else:
                damage = unit_2.attack
                unit_1.health -= damage

            if type(unit_2) == Vampire and damage != 0:
                unit_2.health += int(damage * unit_2.vampirism / 100)
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

    def move_units(self):
        warlord = [x for x in self.units if type(x)==Warlord]
        if warlord:
            lancers = [x for x in self.units if type(x)==Lancer]
            healers = [x for x in self.units if type(x)==Healer]
            soldiers = [x for x in self.units if not isinstance(x, (Lancer, Healer, Warlord))]
            self.units = []
            if lancers:
                self.units.append(lancers[0])
            elif soldiers:
                self.units.append(soldiers[0])
            elif warlord:
                self.units.extend(warlord)
            if healers:
                self.units.extend(healers)
            if len(lancers)>1:
                self.units.extend(lancers[1:])
            if lancers:
                self.units.extend(soldiers)
            elif len(soldiers)>1:
                self.units.extend(soldiers[1:])
            if lancers or soldiers:
                self.units.extend(warlord)


def delete_zero(grp):
    """Удаляем ноли из списка с группами ламп"""
    import itertools as it
    neo = list(it.filterfalse(lambda x: x == 0, grp))
    return neo

class Battle:
    def fight(self, army1, army2):
        if isinstance(army1, Army) and isinstance(army2, Army):
            army1.move_units()
            army2.move_units()
            while len(army1.units) and len(army2.units):
                healer_1, healer_2 = False, False
                if len(army1.units)>1:
                    healer_1 = army1.units[1] if type(army1.units[1]) == Healer else False
                if len(army2.units)>1:
                    healer_2 = army2.units[1] if type(army2.units[1]) == Healer else False

                first_wins = fight(army1.units[0], army2.units[0], 0, army1, army2, healer_1, healer_2)
                if first_wins:
                    del army2.units[0]
                    army2.move_units()
                else:
                    del army1.units[0]
                    army1.move_units()

            if army1.units:
                return True
            return False
        else:
            print('Not correct input!')

    def straight_fight(self, army1, army2):
        while army1.units and army2.units:
            i = 0
            for x, y in zip(army1.units, army2.units):
                first_wins = fight(x, y)
                if first_wins:
                    army2.units[i] = 0
                else:
                    army1.units[i] = 0
                i += 1

            army1.units = delete_zero(army1.units)
            army2.units = delete_zero(army2.units)

        if army1.units:
            return True
        return False


army_5 = Army()
army_5.add_units(Warlord, 1)
army_5.add_units(Warrior, 10)
army_5.add_units(Lancer, 7)
army_5.add_units(Vampire, 3)
army_5.add_units(Healer, 1)
army_5.add_units(Warrior, 4)
army_5.add_units(Healer, 1)
army_5.add_units(Defender, 2)
army_5.move_units()

army_6 = Army()
army_6.add_units(Warrior, 6)
army_6.add_units(Lancer, 5)

battle = Battle()
print(battle.straight_fight(army_5, army_6)) # == False


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
bob = Warrior()
mars = Warrior()

print(battle.fight(my_army, enemy_army)) # == False
print(battle.fight(army_3, army_4)) # == True

####################################################################################################




unit_1 = Warlord()
unit_2 = Vampire()
fight(unit_1, unit_2)
unit_1 = Warlord()
unit_2 = Knight()
fight(unit_1, unit_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 1)
army_2.add_units(Warrior, 2)
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 2)
army_2.add_units(Warrior, 3)
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 5)
army_2.add_units(Warrior, 7)
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 20)
army_2.add_units(Warrior, 21)
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 10)
army_2.add_units(Warrior, 11)
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 11)
army_2.add_units(Warrior, 7)
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 5)
army_1.add_units(Defender, 4)
army_1.add_units(Defender, 5)
army_2.add_units(Warrior, 4)
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Defender, 5)
army_1.add_units(Warrior, 20)
army_2.add_units(Warrior, 21)
army_1.add_units(Defender, 4)
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 10)
army_1.add_units(Defender, 5)
army_2.add_units(Warrior, 5)
army_1.add_units(Defender, 10)
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Defender, 2)
army_1.add_units(Warrior, 1)
army_1.add_units(Defender, 1)
army_2.add_units(Warrior, 5)
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Defender, 5)
army_1.add_units(Vampire, 6)
army_1.add_units(Warrior, 7)
army_2.add_units(Warrior, 6)
army_2.add_units(Defender, 6)
army_2.add_units(Vampire, 6)
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Defender, 2)
army_1.add_units(Vampire, 3)
army_1.add_units(Warrior, 4)
army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 4)
army_2.add_units(Vampire, 3)
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Defender, 11)
army_1.add_units(Vampire, 3)
army_1.add_units(Warrior, 4)
army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 4)
army_2.add_units(Vampire, 13)
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Defender, 9)
army_1.add_units(Vampire, 3)
army_1.add_units(Warrior, 8)
army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 4)
army_2.add_units(Vampire, 13)
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Lancer, 5)
army_1.add_units(Vampire, 3)
army_1.add_units(Warrior, 4)
army_1.add_units(Defender, 2)
army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 4)
army_2.add_units(Vampire, 6)
army_2.add_units(Lancer, 5)
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Lancer, 7)
army_1.add_units(Vampire, 3)
army_1.add_units(Warrior, 4)
army_1.add_units(Defender, 2)
army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 4)
army_2.add_units(Vampire, 6)
army_2.add_units(Lancer, 4)
battle = Battle()
battle.fight(army_1, army_2)
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
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Lancer, 1)
army_1.add_units(Warrior, 3)
army_1.add_units(Healer, 1)
army_1.add_units(Warrior, 4)
army_1.add_units(Healer, 1)
army_1.add_units(Knight, 2)
army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 4)
army_2.add_units(Healer, 1)
army_2.add_units(Vampire, 6)
army_2.add_units(Lancer, 4)
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Lancer, 5)
army_1.add_units(Vampire, 3)
army_1.add_units(Warrior, 4)
army_1.add_units(Defender, 2)
army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 4)
army_2.add_units(Vampire, 6)
army_2.add_units(Lancer, 5)
battle = Battle()
battle.straight_fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Lancer, 7)
army_1.add_units(Vampire, 3)
army_1.add_units(Warrior, 4)
army_1.add_units(Defender, 2)
army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 4)
army_2.add_units(Vampire, 6)
army_2.add_units(Lancer, 4)
battle = Battle()
battle.straight_fight(army_1, army_2)
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
battle.straight_fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Lancer, 4)
army_1.add_units(Warrior, 3)
army_1.add_units(Healer, 1)
army_1.add_units(Warrior, 4)
army_1.add_units(Healer, 1)
army_1.add_units(Knight, 2)
army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 4)
army_2.add_units(Healer, 1)
army_2.add_units(Vampire, 2)
army_2.add_units(Lancer, 4)
battle = Battle()
battle.straight_fight(army_1, army_2)

print('*'*50)

army_1 = Army()
army_2 = Army()
army_1.add_units(Warlord, 1)
army_1.add_units(Warrior, 2)
army_1.add_units(Lancer, 2)
army_1.add_units(Healer, 2)
army_2.add_units(Warlord, 1)
army_2.add_units(Vampire, 1)
army_2.add_units(Healer, 2)
army_2.add_units(Knight, 2)
army_1.move_units()
army_2.move_units()
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 2)
army_1.add_units(Lancer, 2)
army_1.add_units(Defender, 1)
army_1.add_units(Warlord, 3)
army_2.add_units(Warlord, 2)
army_2.add_units(Vampire, 1)
army_2.add_units(Healer, 5)
army_2.add_units(Knight, 2)
army_1.move_units()
army_2.move_units()
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 2)
army_1.add_units(Lancer, 3)
army_1.add_units(Defender, 1)
army_1.add_units(Warlord, 4)
army_2.add_units(Warlord, 1)
army_2.add_units(Vampire, 1)
army_2.add_units(Rookie, 1)
army_2.add_units(Knight, 1)
army_1.units[0].equip_weapon(Sword())
army_2.units[0].equip_weapon(Shield())
army_1.move_units()
army_2.move_units()
battle = Battle()
battle.fight(army_1, army_2)
army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 2)
army_1.add_units(Lancer, 3)
army_1.add_units(Defender, 1)
army_1.add_units(Warlord, 1)
army_2.add_units(Warlord, 5)
army_2.add_units(Vampire, 1)
army_2.add_units(Rookie, 1)
army_2.add_units(Knight, 1)
army_1.units[0].equip_weapon(Sword())
army_2.units[0].equip_weapon(Shield())
army_1.move_units()
army_2.move_units()
battle = Battle()
battle.straight_fight(army_1, army_2)
unit_1 = Warrior()
unit_2 = Vampire()
weapon_1 = Weapon(-10, 5, 0, 40, 0)
weapon_2 = Sword()
unit_1.equip_weapon(weapon_1)
unit_2.equip_weapon(weapon_2)
fight(unit_1, unit_2)
unit_1 = Defender()
unit_2 = Lancer()
weapon_1 = Shield()
weapon_2 = GreatAxe()
unit_1.equip_weapon(weapon_1)
unit_2.equip_weapon(weapon_2)
fight(unit_1, unit_2)
unit_1 = Healer()
unit_2 = Knight()
weapon_1 = MagicWand()
weapon_2 = Katana()
unit_1.equip_weapon(weapon_1)
unit_2.equip_weapon(weapon_2)
fight(unit_1, unit_2)
unit_1 = Defender()
unit_2 = Vampire()
weapon_1 = Shield()
weapon_2 = MagicWand()
weapon_3 = Shield()
weapon_4 = Katana()
unit_1.equip_weapon(weapon_1)
unit_1.equip_weapon(weapon_2)
unit_2.equip_weapon(weapon_3)
unit_2.equip_weapon(weapon_4)
fight(unit_1, unit_2)
weapon_1 = MagicWand()
weapon_2 = GreatAxe()
my_army = Army()
my_army.add_units(Knight, 1)
my_army.add_units(Lancer, 1)
enemy_army = Army()
enemy_army.add_units(Vampire, 1)
enemy_army.add_units(Healer, 1)
my_army.units[0].equip_weapon(weapon_1)
my_army.units[1].equip_weapon(weapon_2)
enemy_army.units[0].equip_weapon(weapon_1)
enemy_army.units[1].equip_weapon(weapon_2)
battle = Battle()
battle.fight(my_army, enemy_army)
weapon_1 = Sword()
weapon_2 = GreatAxe()
my_army = Army()
my_army.add_units(Defender, 1)
my_army.add_units(Warrior, 1)
enemy_army = Army()
enemy_army.add_units(Knight, 1)
enemy_army.add_units(Healer, 1)
my_army.units[0].equip_weapon(weapon_2)
my_army.units[1].equip_weapon(weapon_2)
enemy_army.units[0].equip_weapon(weapon_1)
enemy_army.units[1].equip_weapon(weapon_1)
battle = Battle()
battle.fight(my_army, enemy_army)
weapon_1 = Katana()
weapon_2 = Shield()
my_army = Army()
my_army.add_units(Defender, 2)
enemy_army = Army()
enemy_army.add_units(Knight, 1)
enemy_army.add_units(Vampire, 1)
my_army.units[0].equip_weapon(weapon_1)
my_army.units[1].equip_weapon(weapon_1)
enemy_army.units[0].equip_weapon(weapon_1)
enemy_army.units[1].equip_weapon(weapon_1)
battle = Battle()
battle.fight(my_army, enemy_army)
weapon_1 = Weapon(-20, 6, 1, 40, -2)
weapon_2 = Weapon(20, -2, 2, -55, 3)
my_army = Army()
my_army.add_units(Knight, 3)
enemy_army = Army()
enemy_army.add_units(Warrior, 1)
enemy_army.add_units(Defender, 2)
my_army.units[0].equip_weapon(weapon_1)
my_army.units[1].equip_weapon(weapon_1)
my_army.units[2].equip_weapon(weapon_2)
enemy_army.units[0].equip_weapon(weapon_1)
enemy_army.units[1].equip_weapon(weapon_2)
enemy_army.units[2].equip_weapon(weapon_2)
battle = Battle()
battle.fight(my_army, enemy_army)
weapon_1 = Weapon(-20, 1, 1, 40, -2)
weapon_2 = Weapon(20, 2, 2, -55, 3)
my_army = Army()
my_army.add_units(Vampire, 3)
enemy_army = Army()
enemy_army.add_units(Warrior, 1)
enemy_army.add_units(Defender, 2)
my_army.units[0].equip_weapon(weapon_1)
my_army.units[1].equip_weapon(weapon_1)
my_army.units[2].equip_weapon(weapon_2)
enemy_army.units[0].equip_weapon(weapon_1)
enemy_army.units[1].equip_weapon(weapon_2)
enemy_army.units[2].equip_weapon(weapon_2)
battle = Battle()
battle.straight_fight(my_army, enemy_army)
weapon_1 = Katana()
weapon_2 = Shield()
my_army = Army()
my_army.add_units(Vampire, 2)
my_army.add_units(Rookie, 2)
enemy_army = Army()
enemy_army.add_units(Warrior, 1)
enemy_army.add_units(Defender, 2)
my_army.units[0].equip_weapon(weapon_1)
my_army.units[1].equip_weapon(weapon_1)
my_army.units[2].equip_weapon(weapon_2)
enemy_army.units[0].equip_weapon(weapon_1)
enemy_army.units[1].equip_weapon(weapon_2)
enemy_army.units[2].equip_weapon(weapon_2)
battle = Battle()
battle.straight_fight(my_army, enemy_army)

weapon_1 = Sword()
weapon_2 = GreatAxe()
my_army = Army()
my_army.add_units(Vampire, 3)
enemy_army = Army()
enemy_army.add_units(Warrior, 1)
enemy_army.add_units(Defender, 1)
my_army.units[0].equip_weapon(weapon_2)
my_army.units[1].equip_weapon(weapon_2)
my_army.units[2].equip_weapon(weapon_2)
enemy_army.units[0].equip_weapon(weapon_1)
enemy_army.units[1].equip_weapon(weapon_1)
battle = Battle()
battle.straight_fight(my_army, enemy_army)

weapon_1 = Katana()
weapon_2 = MagicWand()
my_army = Army()
my_army.add_units(Rookie, 3)
enemy_army = Army()
enemy_army.add_units(Defender, 1)
enemy_army.add_units(Healer, 1)
my_army.units[0].equip_weapon(weapon_1)
my_army.units[1].equip_weapon(weapon_1)
my_army.units[2].equip_weapon(weapon_1)
enemy_army.units[0].equip_weapon(weapon_2)
enemy_army.units[1].equip_weapon(weapon_2)
battle = Battle()
battle.straight_fight(my_army, enemy_army)


