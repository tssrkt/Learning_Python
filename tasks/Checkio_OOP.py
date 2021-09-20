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
        if self.gender == 'male':
            return f'He is a {self.job}'
        elif self.gender == 'female':
            return f'She is a {self.job}'
        else:
            return f'Is a {self.job}'

    def money(self):
        money = str(self.working_years * (self.salary * 12))
        for x in range(len(money) - 1, -1, -3):
            money = money[:x + 1] + ' ' + money[x + 1:]
        return money.strip()

    def home(self):
        return f'Lives in {self.city}, {self.country}'


# p1 = Person('John', 'Smith', '19.09.1979', 'welder', 15, 3600, 'Canada', 'Vancouver', 'male')
# print(p1.money())
# print(p1.age())


class Building:

    def __init__(self, south, west, width_WE, width_NS, height=10):
        if not isinstance(any([south, west, width_WE, width_NS, height]), (int, float)):
            raise TypeError('Not correct input.')
        self.south_west = [south, west]
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        nw = [self.width_NS + self.south_west[0], self.south_west[1]]
        ne = [nw[0], self.south_west[1] + self.width_WE]
        se = [self.south_west[0], ne[1]]
        return {"north-west": nw, "north-east": ne, "south-west": self.south_west, "south-east": se}

    def area(self):
        return self.width_WE * self.width_NS

    def volume(self):
        return self.width_WE * self.width_NS * self.height

    def __repr__(self):
        return f"Building({self.south_west[0]}, {self.south_west[1]}, {self.width_WE}, {self.width_NS}, {self.height})"


# print(Building(10, 10, 1, 2, 2))
# print(Building(0, 0, 10.5, 2.546))
# print(Building(1, 2, 2, 2).corners())


class Friends:
    cons = []

    def __init__(self, *args):
        for arg in args:
            if isinstance(arg, (list, tuple)):
                Friends.cons.extend([x for x in arg if x not in Friends.cons])
            else:
                if arg not in Friends.cons:
                    Friends.cons.append(arg)

    @classmethod
    def add(cls, bond):
        if bond in cls.cons:
            return False
        cls.cons.append(bond)
        return True

    @classmethod
    def remove(cls, bond):
        if bond in cls.cons:
            cls.cons.remove(bond)
            return True
        return False

    @classmethod
    def names(cls):
        names = set()
        for bond in cls.cons:
            for name in bond:
                names.add(name)
        return names

    @classmethod
    def connected(cls, name):
        names = set()
        for bond in cls.cons:
            if name in bond:
                for x in bond:
                    if x != name:
                        names.add(x)
        return names


f = Friends({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"})
f1 = Friends({'Alice', 'Robocop'})
# print(f.add({'Emma', 'Jhon'}))
# print(f.names())
# print(f.connected("a"))
# f2 = Friends([{"And", "Or"}, {"For", "And"}])
# print(f2.add({"Or", "And"}))
# print(Friends.cons)


###########################################################################################


from abc import ABC, abstractmethod


class Army(ABC):
    @abstractmethod
    def train_swordsman(self, name):
        pass

    @abstractmethod
    def train_lancer(self, name):
        pass

    @abstractmethod
    def train_archer(self, name):
        pass


class AsianArmy(Army):
    types = {'swordsman': 'Samurai', 'lancer': 'Ronin', 'archer': 'Shinobi'}

    def __init__(self):
        self.army = 'Asian'

    def train_swordsman(self, name):
        self.spec = 'swordsman'
        self.name = name
        return Swordsman(self.types['swordsman'], self.name, self.army, self.spec)

    def train_lancer(self, name):
        self.spec = 'lancer'
        self.name = name
        return Lancer(self.types['lancer'], self.name, self.army, self.spec)

    def train_archer(self, name):
        self.spec = 'archer'
        self.name = name
        return Archer(self.types['archer'], self.name, self.army, self.spec)


class EuropeanArmy(Army):
    types = {'swordsman': 'Knight', 'lancer': 'Raubritter', 'archer': 'Ranger'}

    def __init__(self):
        self.army = 'European'

    def train_swordsman(self, name):
        self.spec = 'swordsman'
        self.name = name
        return Swordsman(self.types['swordsman'], self.name, self.army, self.spec)

    def train_lancer(self, name):
        self.spec = 'lancer'
        self.name = name
        return Lancer(self.types['lancer'], self.name, self.army, self.spec)

    def train_archer(self, name):
        self.spec = 'archer'
        self.name = name
        return Archer(self.types['archer'], self.name, self.army, self.spec)


class Warrior(ABC):
    def __init__(self, type, name, army, spec):
        self.type = type
        self.name = name
        self.army = army
        self.spec = spec

    def introduce(self):
        return f'{self.type} {self.name}, {self.army} {self.spec}'


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
# print(soldier_1.introduce()) # == "Knight Jaks, European swordsman"
# print(soldier_2.introduce()) # == "Raubritter Harold, European lancer"
# print(soldier_3.introduce()) # == "Ranger Robin, European archer"
#
# print(soldier_4.introduce()) # == "Samurai Kishimoto, Asian swordsman"
# print(soldier_5.introduce()) # == "Ronin Ayabusa, Asian lancer"
# print(soldier_6.introduce()) # == "Shinobi Kirigae, Asian archer"

class AbstractCook(ABC):
    @abstractmethod
    def add_food(self, food_amount, food_price):
        pass

    @abstractmethod
    def add_drink(self, drink_amount, drink_price):
        pass

    @abstractmethod
    def total(self):
        pass


class JapaneseCook(AbstractCook):
    food = {'meal': 'Sushi', 'drink': 'Tea'}

    def __init__(self):
        self.food_amount = 0
        self.food_price = 0
        self.drink_amount = 0
        self.drink_price = 0

    def add_food(self, food_amount, food_price):
        self.food_price += (food_price * food_amount)

    def add_drink(self, drink_amount, drink_price):
        self.drink_price += (drink_price * drink_amount)

    def total(self):
        return f"{self.food['meal']}: {self.food_price}, {self.food['drink']}: " \
               f"{self.drink_price}, Total: {self.food_price + self.drink_price}"


class RussianCook(AbstractCook):
    food = {'meal': 'Dumplings', 'drink': 'Compote'}

    def __init__(self):
        self.food_amount = 0
        self.food_price = 0
        self.drink_amount = 0
        self.drink_price = 0

    def add_food(self, food_amount, food_price):
        self.food_price += (food_price * food_amount)

    def add_drink(self, drink_amount, drink_price):
        self.drink_price += (drink_price * drink_amount)

    def total(self):
        return f"{self.food['meal']}: {self.food_price}, {self.food['drink']}: " \
               f"{self.drink_price}, Total: {self.food_price + self.drink_price}"


class ItalianCook(AbstractCook):
    food = {'meal': 'Pizza', 'drink': 'Juice'}

    def __init__(self):
        self.food_amount = 0
        self.food_price = 0
        self.drink_amount = 0
        self.drink_price = 0

    def add_food(self, food_amount, food_price):
        self.food_price += (food_price * food_amount)

    def add_drink(self, drink_amount, drink_price):
        self.drink_price += (drink_price * drink_amount)

    def total(self):
        return f"{self.food['meal']}: {self.food_price}, {self.food['drink']}: " \
               f"{self.drink_price}, Total: {self.food_price + self.drink_price}"


# client_4 = JapaneseCook()
# client_4.add_food(1, 65)
# client_4.add_drink(4, 10)
# client_4.add_drink(2, 5)
# print(client_4.total())
#
# client_1 = JapaneseCook()
# client_1.add_food(2, 20)
# client_1.add_drink(5, 4)
# print(client_1.total())  # == "Sushi: 40, Tea: 20, Total: 60"
#
# client_2 = RussianCook()
# client_2.add_food(1, 40)
# client_2.add_drink(5, 20)
# print(client_2.total())  # == "Dumplings: 40, Compote: 100, Total: 140"
#
# client_3 = ItalianCook()
# client_3.add_food(2, 20)
# client_3.add_drink(2, 10)
# print(client_3.total())  # == "Pizza: 40, Juice: 20, Total: 60"

# Singleton

class CapitalMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(CapitalMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Capital(metaclass=CapitalMeta):

    def __init__(self, nm):
        self.nm = nm

    def name(self):
        return self.nm


# ukraine_capital_1 = Capital("Kyiv")
# ukraine_capital_2 = Capital("London")
# ukraine_capital_3 = Capital("Marocco")
# print(ukraine_capital_1.name())
# print(ukraine_capital_2.name()) # == "Kyiv"
# print(ukraine_capital_3.name()) # == "Kyiv"

# Mediator

# from abc import ABC
import itertools as it


class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass


class Chat(Mediator):

    def __init__(self):
        self.dialogue = ''
        self.iniciator = ''

    def notify(self, sender, text):
        if self.dialogue == '':
            if type(sender) == Human:
                self.iniciator = 'human'
            elif type(sender) == Robot:
                self.iniciator = 'robot'
        if type(sender) == Human:
            self.dialogue += text + '\n'
        elif type(sender) == Robot:
            self.dialogue += text + '\n'

    def connect_human(self, member):
        if type(member) == Human:
            self._human = member
            self._human.mediator = self

    def connect_robot(self, member):
        if type(member) == Robot:
            self._robot = member
            self._robot.mediator = self

    def show_human_dialogue(self):
        chat = self.dialogue.split('\n')
        chat = list(it.filterfalse(lambda x: x == '', chat))
        members = [f'{self._human.name} said: ', f'{self._robot.serial_number} said: ']
        i = 0 if self.iniciator == 'human' else 1
        res = ''
        for x in chat:
            fin = '' if chat.index(x) == len(chat) - 1 else '\n'
            res += members[i] + x + fin
            i = 0 if i == 1 else 1
        return res

    def show_robot_dialogue(self):
        chat = self.dialogue.split('\n')
        chat = list(it.filterfalse(lambda x: x == '', chat))
        members = [f'{self._human.name} said: ', f'{self._robot.serial_number} said: ']
        i = 0 if self.iniciator == 'human' else 1
        res = ''
        for x in chat:
            fin = '' if chat.index(x) == len(chat) - 1 else '\n'
            x = ''.join(['0' if y in "aeiouAEIOU" else '1' for y in x])
            res += members[i] + x + fin
            i = 0 if i == 1 else 1
        return res


class Member:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class Human(Member):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def send(self, text):
        self.mediator.notify(self, text)


class Robot(Member):
    def __init__(self, serial_number):
        super().__init__()
        self.serial_number = serial_number

    def send(self, text):
        self.mediator.notify(self, text)


# chat = Chat()
# karl = Human("Karl")
# bot = Robot("R2D2")
# chat.connect_human(karl)
# chat.connect_robot(bot)
# karl.send("Hi! What's new?")
# bot.send("Hello, human. Could we speak later about it?")
# print(chat.show_human_dialogue()) # == """Karl said: Hi! What's new?
# # R2D2 said: Hello, human. Could we speak later about it?"""
# print(chat.show_robot_dialogue()) # == """Karl said: 101111011111011
# # R2D2 said: 10110111010111100111101110011101011010011011"""

# Strategy
# from abc import ABC, abstractmethod
from math import pi


class Parameters:
    def __init__(self, data):
        self._data = data
        self.shape = ''

    def choose_figure(self, shape):
        self.shape = shape

    def perimeter(self):
        return round(self.shape.perimeter(self._data), 2)

    def area(self):
        return round(self.shape.area(self._data), 2)

    def volume(self):
        return round(self.shape.volume(self._data), 2)


class Shape(ABC):
    @abstractmethod
    def perimeter(self, data):
        pass

    @abstractmethod
    def area(self, data):
        pass

    @abstractmethod
    def volume(self, data):
        pass


class Circle(Shape):
    def perimeter(self, data):
        return 2 * pi * data

    def area(self, data):
        return pi * data ** 2

    def volume(self, data):
        return 0


class Triangle(Shape):
    def perimeter(self, data):
        return 3 * data

    def area(self, data):
        return round((data ** 2 * (3 ** 0.5)) / 4, 2)

    def volume(self, data):
        return 0


class Square(Shape):
    def perimeter(self, data):
        return 4 * data

    def area(self, data):
        return data ** 2

    def volume(self, data):
        return 0


class Pentagon(Shape):
    def perimeter(self, data):
        return 5 * data

    def area(self, data):
        return (data ** 2 / 4) * (25 + 10 * (5 ** 0.5)) ** 0.5

    # (5*data**2)/4*(5-2*5**0.5)*0.5

    def volume(self, data):
        return 0


class Hexagon(Shape):
    def perimeter(self, data):
        return 6 * data

    def area(self, data):
        return ((3 * 3 ** 0.5) / 2) * data ** 2

    def volume(self, data):
        return 0


class Cube(Shape):
    def perimeter(self, data):
        return 12 * data

    def area(self, data):
        return 6 * data ** 2

    def volume(self, data):
        return data ** 3


# figure = Parameters(10)
# figure.choose_figure(Circle())
# print(figure.area()) # == 314.16
# figure.choose_figure(Triangle())
# print(figure.perimeter()) # == 30
# figure.choose_figure(Square())
# print(figure.area()) # == 100
# figure.choose_figure(Pentagon())
# print(figure.perimeter()) # == 50
# figure.choose_figure(Hexagon())
# print(figure.perimeter()) # == 60
# figure.choose_figure(Cube())
# print(figure.volume()) # == 1000


# Interpreter
import abc


class AE(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def interpret(self):
        pass


class HackerLanguage(AE):
    def __init__(self):
        self.message = ''

    def interpret(self):
        self.message.interpret()

    def write(self, text):
        self.message += text

    def delete(self, n):
        self.message = self.message[:(len(self.message) - n)]

    def send(self):
        msg = ''
        for x in self.message:
            if x.isalpha():
                msg += (bin(ord(x)))[2:]
            elif x.isspace():
                msg += '1000000'
            else:
                msg += x
        return msg

    def read(self, text):
        msg = ''
        n = 0
        from string import punctuation as pn
        while n < len(text):
            if text[n] in pn:
                msg += text[n]
                n += 1
            else:
                if text[n:n + 7] == '1000000':
                    msg += ' '
                    n += 7
                elif text[n] in ['1', '0']:
                    res = 0
                    decimal = 1
                    for y in reversed(text[n:n + 7]):
                        res += decimal if int(y) == 1 else 0
                        decimal *= 2
                    msg += chr(res)
                    n += 7
                else:
                    msg += x
                    n += 1
        return msg


# m_1 = HackerLanguage()
# m_1.write('Remember: 21.07.2018 at 11:11AM')
# m_1.delete(2)
# m_1.write('PM')
# print(m_1.send())  # == '10100101100101110110111001011101101110001011001011110010:100000021.07.2018100000011000011110100100000011:1110100001001101'
#
# m_2 = HackerLanguage()
# print(m_2.read('10011011111001100000011001011101101110000111010011101100100000011010011110011100000011011011110010.11100101101111110001011011111110100@11001111101101110000111010011101100.110001111011111101101'))
# # == 'My email is mr.robot@gmail.com'


# from abc import ABC, abstractmethod


class RemoteControl:
    def __init__(self, microwave):
        self.microwave = microwave

    def set_time(self, time):
        self.microwave.set_time(time)

    def add_time(self, time):
        self.microwave.add_time(time)

    def del_time(self, time):
        self.microwave.del_time(time)

    def show_time(self):
        return self.microwave.show_time()


class MicrowaveBase(ABC):
    def __init__(self):
        self.time = '00:00'

    def set_time(self, time):
        self.time = time

    def add_time(self, time):
        mns, scs = (self.time).split(':')
        if time[-1] == 's':
            secs = int(time[:-1])
            mins = 0
            scs = int(scs) + secs
            if scs >= 60:
                mins = scs // 60
                scs = scs % 60
            mns = int(mns) + mins
            mns = 90 if mns > 90 else (0 if mns < 0 else mns)
            scs = 0 if mns == 90 else scs
            mns = '0' + str(mns) if mns < 10 else str(mns)
            scs = '0' + str(scs) if scs < 10 else str(scs)
            self.time = f'{mns}:{scs}'
        else:
            mins = int(time[:-1])
            mns = 90 if mins + int(mns) > 90 else mins + int(mns)
            mns = '0' + str(mns) if mns < 10 else str(mns)
            self.time = f'{mns}:{scs}'

    def del_time(self, time):
        mns, scs = self.time.split(':')
        if time[-1] == 's':
            scs = int(scs) - int(time[:-1])
            scs = 0 if scs < 0 else scs
            scs = '0' + str(scs) if scs < 10 else str(scs)
            self.time = f'{mns}:{scs}'
        else:
            mins = int(time[:-1])
            mns = 0 if int(mns) - mins < 0 else int(mns) - mins
            mns = '0' + str(mns) if mns < 10 else str(mns)
            self.time = f'{mns}:{scs}'

    @abstractmethod
    def show_time(self):
        pass


class Microwave1(MicrowaveBase):
    def show_time(self):
        return '_' + self.time[1:]


class Microwave2(MicrowaveBase):
    def show_time(self):
        return self.time[:-1] + '_'


class Microwave3(MicrowaveBase):
    def show_time(self):
        return self.time



# m_1 = Microwave1()
# rc_6 = RemoteControl(m_1)
# rc_6.set_time("02:20")
# rc_6.del_time("0s")
# rc_6.add_time("40s")
# print(rc_6.show_time())  # == "_3:00"
#
# m_2 = Microwave2()
# rc_2 = RemoteControl(m_2)
# rc_2.set_time("89:00")
# rc_2.add_time("90s")
# rc_2.add_time("20m")
# print(rc_2.show_time())  # == "90:0_"
#
# microwave_1 = Microwave1()
# microwave_2 = Microwave2()
# microwave_3 = Microwave3()
#
# remote_control_1 = RemoteControl(microwave_1)
# remote_control_1.set_time("01:00")
#
# remote_control_2 = RemoteControl(microwave_2)
# remote_control_2.add_time("90s")
#
# remote_control_3 = RemoteControl(microwave_3)
# remote_control_3.del_time("300s")
# remote_control_3.add_time("100s")
#
# print(remote_control_1.show_time())  # == "_1:00"
# print(remote_control_2.show_time())  # == "01:3_"
# print(remote_control_3.show_time())  # == "01:40"

from itertools import cycle

class Lamp:
    def __init__(self):
        self.states = cycle(['Green', 'Red', 'Blue', 'Yellow'])
        self.iter = iter(self.states)

    def light(self):
        return next(cycle(self.states))


# lamp_1 = Lamp()
# lamp_2 = Lamp()
#
# lamp_1.light()  # Green
# lamp_1.light()  # Red
# lamp_2.light()  # Green
#
# print(lamp_1.light()) # == "Blue"
# print(lamp_1.light()) # == "Yellow"
# print(lamp_1.light()) # == "Green"
# print(lamp_2.light()) # == "Red"
# print(lamp_2.light()) # == "Blue"


class Party:
    def __init__(self, place):
        self.place = place
        self.friends = []

    def add_friend(self, friend) -> None:
        self.friends.append(friend)

    def del_friend(self, friend) -> None:
        self.friends.remove(friend)

    def send_invites(self, invite) -> None:
        for friend in self.friends:
            friend.invite = invite
            friend.place = self.place


class Friend:
    def __init__(self, name):
        self.name = name
        self.invite = ''
        self.place = ''

    def show_invite(self) -> None:
        if self.invite=='':
            return "No party..."
        return f"{self.place}: {self.invite}"


# party = Party("Midnight Pub")
# nick = Friend("Nick")
# john = Friend("John")
# lucy = Friend("Lucy")
# chuck = Friend("Chuck")
#
# party.add_friend(nick)
# party.add_friend(john)
# party.add_friend(lucy)
# party.send_invites("Friday, 9:00 PM")
# party.del_friend(nick)
# party.send_invites("Saturday, 10:00 AM")
# party.add_friend(chuck)
#
# print(john.show_invite())  # == "Midnight Pub: Saturday, 10:00 AM"
# print(lucy.show_invite())  # == "Midnight Pub: Saturday, 10:00 AM"
# print(nick.show_invite())  # == "Midnight Pub: Friday, 9:00 PM"
# print(chuck.show_invite())  # == "No party..."


class Text:
    def __init__(self):
        self.text = ''
        self.font = ''

    def write(self, text):
        self.text += text

    def set_font(self, font):
        self.font = '[' + font + ']'

    def show(self):
        return self.font + self.text + self.font

    def restore(self, old_version):
        self.text = old_version[0]
        self.font = old_version[1]

class SavedText:
    def __init__(self):
        self.versions = []

    def save_text(self, text):
        self.versions.append([text.text, text.font])

    def get_version(self, number):
        return self.versions[number]


# text = Text()
# saver = SavedText()
# text.write("At the very beginning ")
# saver.save_text(text)
# text.set_font("Arial")
# saver.save_text(text)
# text.write("there was nothing.")
#
# print(text.show())  # == "[Arial]At the very beginning there was nothing.[Arial]"
# text.restore(saver.get_version(0))
# print(text.show())  # == "At the very beginning "


class VoiceCommand():
    def __init__(self, channels):
        self.channels = channels
        self.num = 0

    # переключается на первый канал из списка
    def first_channel(self):
        self.num = 0
        return self.channels[0]

    # переключается на последний канал из списка.
    def last_channel(self):
        self.num = len(self.channels)-1
        return self.channels[-1]

    # переключается на канал номер n. Нумерация каналов начинается с 1, а не с 0.
    def turn_channel(self, n):
        self.num = n-1
        return self.channels[n-1]

    # переключается на следующий канал. Если текущий канал - последний, то - на первый канал.
    def next_channel(self):
        if self.num == len(self.channels)-1:
            self.num = 0
            return self.channels[0]
        self.num += 1
        return self.channels[self.num]

    # переключается на предыдущий канал. Если текущий канал - первый, то - на последний канал.
    def previous_channel(self):
        if self.num == 0:
            self.num = len(self.channels)-1
            return self.channels[-1]
        self.num -= 1
        return self.channels[self.num]

    # возвращает название текущего канала.
    def current_channel(self):
        return self.channels[self.num]

    # принимает 1 аргумент - число N или строку 'name' и возвращает "Yes", если канал
    # с номером N или названием 'name' существует в списке и "No" в ином случае.
    def is_exist(self, x):
        if type(x)==int:
            try:
                chan = self.channels[x]
                return 'Yes'
            except IndexError:
                return 'No'
        else:
            if x in self.channels:
                return 'Yes'
            return 'No'


CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = VoiceCommand(CHANNELS)

print(controller.first_channel())  # == "BBC"
print(controller.last_channel())  # == "TV1000"
print(controller.turn_channel(1))  # == "BBC"
print('DISCOVERY:', controller.next_channel())  # == "Discovery"
print(controller.previous_channel())  # == "BBC"
print(controller.current_channel())  # == "BBC"
print(controller.is_exist(4)) # == "No"
print(controller.is_exist("BBC")) # == "Yes"
