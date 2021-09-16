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

print('WARRIORS')
army_1 = Army()
army_2 = Army()
# army_1.add_units(Lancer, 7)
army_1.add_units(Vampire, 1)
army_1.add_units(Healer, 1)
army_1.add_units(Warrior, 4)
army_1.add_units(Healer, 1)
army_1.add_units(Defender, 2)

# army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 1)
army_2.add_units(Healer, 1)
army_2.add_units(Vampire, 6)
army_2.add_units(Lancer, 4)
battle = Battle()

print(battle.fight(army_1, army_2))  #

# Palindromic Palindrome
"f\";]1-::[s==s:s adbmal=oikcehc;";checkio=lambda s:s==s[::-1];"\f"


# Cipher Map
def recall_password(grille, password):
    answer = ""
    for _ in range(4):
        answer += ''.join([password[r][c] for r in range(4) for c in range(4) if grille[r][c] == 'X'])
        grille = list(map(''.join, zip(*grille[::-1])))
    return answer

