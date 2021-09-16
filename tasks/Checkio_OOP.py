class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def age(self):
        """ Age of person at 01.01.2018 """
        from datetime import date
        d, m, y = (self.birth_date).split('.')
        born = date(int(y), int(m), int(d))
        today = date(2018, 1, 1)
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


    def work(self):
        if self.gender=='male':
            return f'He is a {self.job}'
        elif self.gender=='female':
            return f'She is a {self.job}'
        else:
            return f'Is a {self.job}'

    def money(self):
        money = str(self.working_years * (self.salary*12))
        for x in range(len(money)-1, -1, -3):
            money = money[:x+1] + ' ' + money[x+1:]
        return money.strip()

    def home(self):
        return f'Lives in {self.city}, {self.country}'


# p1 = Person('John', 'Smith', '19.09.1979', 'welder', 15, 3600, 'Canada', 'Vancouver', 'male')
# print(p1.money())
# print(p1.age())



















from abc import ABC, abstractmethod

class Army(ABC):
    @abstractmethod
    def train_swordsman(self, name):
        self.spec = 'swordsman'
        self.name = name
        self.type = self.types.get(self.spec)
        return Swordsman(self.type, self.name, self.army, self.spec)

    @abstractmethod
    def train_lancer(self, name):
        self.spec = 'lancer'
        self.name = name
        self.type = self.types.get(self.spec)
        return Lancer(self.type, self.name, self.army, self.spec)

    @abstractmethod
    def train_archer(self, name):
        self.spec = 'archer'
        self.name = name
        self.type = self.types.get(self.spec)
        return Archer(self.type, self.name, self.army, self.spec)


class AsianArmy(Army):
    types = {'swordsman': 'Samurai', 'lancer': 'Ronin', 'archer': 'Shinobi'}

    def __init__(self):
        self.army = 'Asian'

class EuropeanArmy(Army):
    types = {'swordsman': 'Knight', 'lancer': 'Raubritter', 'archer': 'Ranger'}

    def __init__(self):
        self.army = 'European'

class Warrior(ABC):
    def __init__(self, type, name, army, spec):
        self.type = type
        self.name = name
        self.army = army
        self.spec = spec

    @abstractmethod
    def introduce(self):
        return f'{self.type} {self.name}, {self.army} {self.spec}'

    # "Raubritter Harold, European lancer"
    # "Shinobi Kirigae, Asian archer"

class Swordsman(Warrior):
    pass

class Lancer(Warrior):
    pass

class Archer(Warrior):
    pass



# my_army = EuropeanArmy()
# enemy_army = AsianArmy()
#
# soldier_1 = my_army.train_swordsman("Jaks")
# soldier_2 = my_army.train_lancer("Harold")
# soldier_3 = my_army.train_archer("Robin")
#
# soldier_4 = enemy_army.train_swordsman("Kishimoto")
# soldier_5 = enemy_army.train_lancer("Ayabusa")
# soldier_6 = enemy_army.train_archer("Kirigae")
#
# soldier_1.introduce() == "Knight Jaks, European swordsman"
# soldier_2.introduce() == "Raubritter Harold, European lancer"
# soldier_3.introduce() == "Ranger Robin, European archer"
#
# soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
# soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
# soldier_6.introduce() == "Shinobi Kirigae, Asian archer"












class VoiceCommand():

    def __init__(self, *args):
        self.channels = args

    # переключается на первый канал из списка
    def first_channel(self):
        pass

    # переключается на последний канал из списка.
    def last_channel(self):
        pass

    # переключается на канал номер n. Нумерация каналов начинается с 1, а не с 0.
    def turn_channel(self, n):
        self.n = n

    # переключается на следующий канал. Если текущий канал - последний, то - на первый канал.
    def next_channel(self):
        pass

    # переключается на предыдущий канал. Если текущий канал - первый, то - на последний канал.
    def previous_channel(self):
        pass

    # возвращает название текущего канала.
    def current_channel(self):
        pass

    # принимает 1 аргумент - число N или строку 'name' и возвращает "Yes", если канал
    # с номером N или названием 'name' существует в списке и "No" в ином случае.
    # def is_exist(self, n, name):
    #     pass


"""
По умолчанию до начала работы всех команд включен канал №1.
Ваша задача - создать класс VoiceCommand и методы, описанные ранее.
В этой миссии вам может помочь такой шаблон проектирования, как Iterator .
"""

CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = VoiceCommand(CHANNELS)

controller.first_channel()  # == "BBC"
controller.last_channel()  # == "TV1000"
controller.turn_channel(1)  # == "BBC"
controller.next_channel()  # == "Discovery"
controller.previous_channel()  # == "BBC"
controller.current_channel()  # == "BBC"
# controller.is_exist(4) # == "No"
# controller.is_exist("BBC") # == "Yes"
