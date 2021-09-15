class Point:
    x = 0
    y = 0

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, a):
        if isinstance(a, Point):
            x1 = self.x
            y1 = self.y

            x2 = a.x
            y2 = a.y

            return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        else:
            print("Передана не точка")


p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
print(p1.get_distance(p2))


#####################################

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


jack = Dog("Jack", 4)

print(jack.description())  # распечатает 'Jack is 4 years old'
print(jack.speak("Woof Woof"))  # распечатает 'Jack says Woof Woof'
print(jack.speak("Bow Wow"))


################################

class Stack:

    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        try:
            return self.values.pop()
        except IndexError:
            print("Empty Stack")

    def peek(self):
        try:
            return self.values[-1]
        except IndexError:
            print("Empty Stack")
            return None

    def is_empty(self):
        if self.values:
            return False
        return True

    def size(self):
        return len(self.values)


"""    Создайте класс UserMail, у которого есть:
конструктор __init__, принимающий 2 аргумента: логин и почтовый адрес. 
Их необходимо сохранить в экземпляр как атрибуты login и __email 
(обратите внимание, защищенный атрибут)
метод геттер get_email, которое возвращает защищенный атрибут __email ;
метод сеттер set_email, которое принимает в виде строки новую почту. 
Метод должен проверять, что в новой почте есть только один символ @ и после нее 
есть точка. Если данные условия выполняются, новая почта сохраняется в атрибут 
__email, в противном случае выведите сообщение "Ошибочная почта";
создайте свойство email, у которого геттером будет метод get_email, 
а сеттером - метод set_email """


class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if email.count('@') == 1 and email.find('.', email.find('@')) != -1:
            self.__email = email
        else:
            print("Ошибочная почта")

    email = property(fget=get_email, fset=set_email)


"""
Создайте класс Money, у которого есть:
конструктор __init__, принимающий 2 аргумента: dollars, cents. 
По входным аргументам вам необходимо создать атрибут экземпляра total_cents. 
свойство геттер dollars, которое возвращает количество имеющихся долларов;
свойство сеттер dollars, которое принимает целое неотрицательное число - 
количество долларов и устанавливает при помощи него новое значение в атрибут 
экземпляра total_cents, при этом значение центов должно сохранятся. В случае, 
если в сеттер передано число, не удовлетворяющее условию, нужно печатать на экран 
сообщение "Error dollars";
свойство геттер cents, которое возвращает количество имеющихся центов;
свойство сеттер cents, которое принимает целое неотрицательное число меньшее 100 - 
количество центов и устанавливает при помощи него новое значение в атрибут 
экземпляра total_cents, при этом значение долларов должно сохранятся. 
В случае, если в сеттер передано число, не удовлетворяющее условию, нужно печатать 
на экран сообщение "Error cents";
метод __str__ (информация по данному методу), который возвращает строку вида 
"Ваше состояние составляет {dollars} долларов {cents} центов". Для нахождения 
долларов и центов в методе __str__ пользуйтесь свойствами
В экземпляр класса кроме атрибута total_cents сохранять ничего не нужно!
"""

print('*' * 50)
print('MONEY')


class Money:

    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, x):
        if isinstance(x, (int)) and x >= 0:
            self.total_cents = self.total_cents % 100 + x * 100
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, x):
        if isinstance(x, (int)) and 0 <= x < 100:
            self.total_cents = (self.total_cents - self.total_cents % 100) + x
        else:
            print("Error cents")

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов

##############################################
print('*' * 50)
print('ROBOT')

"""
атрибут класса population. В этом атрибуте будет хранится общее количество роботов, 
изначально принимает значение 0; конструктор __init__, принимающий 1 аргумент name. 
Данный метод должен сохранять атрибут name и печатать сообщение вида "Робот <name> 
был создан". Помимо инициализации робота данный метод должен увеличивать популяцию 
роботов на единицу;
метод destroy, должен уменьшать популяцию роботов на единицу и печатать сообщение 
вида "Робот <name> был уничтожен"
метод say_hello, которой печатает сообщение вида "Робот <name> приветствует тебя, 
особь человеческого рода" метод класса  how_many, который печатает сообщение вида
"<population>, вот сколько нас еще осталось"
"""


class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population = Robot.population + 1
        print(f"Робот {name} был создан")

    def destroy(self):
        Robot.population = Robot.population - 1
        print(f"Робот {self.name} был уничтожен")

    def say_hello(self):
        print(f"Робот {self.name} приветствует тебя, особь человеческого рода")

    @classmethod
    def how_many(cls):
        print(f"{cls.population}, вот сколько нас еще осталось")


r2 = Robot("R2-D2")  # печатает "Робот R2-D2 был создан"
r2.say_hello()  # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many()  # печатает "1, вот сколько нас еще осталось"
r2.destroy()  # печатает "Робот R2-D2 был уничтожен"

##########################################

""" Создайте класс Person, у которого есть:
конструктор __init__, принимающий 3 аргумента: name, surname, gender. 
Атрибут gender может принимать только 2 значения: "male" и "female", по умолчанию "male". 
Если в атрибут gender передается любое другое значение, печатать сообщение: "Не знаю, что вы имели ввиду? 
Пусть это будет мальчик!" и проставить атрибут gender значением "male"
переопределить метод __str__ следующим образом: 
если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>
если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>
"""


class Person:

    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname

        if gender != 'male' and gender != 'female' and gender != '':
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.gender = 'male'
        else:
            self.gender = gender

    def __str__(self):
        if self.gender == 'male':
            return f"Гражданин {self.surname} {self.name}"
        else:
            return f"Гражданка {self.surname} {self.name}"


p1 = Person('Chuck', 'Norris')
print(p1)  # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2)  # печатает "Гражданка Kunis Mila"
p3 = Person('Оби-Ван', 'Кеноби', True)  # печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
print(p3)  # печатает "Гражданин Кеноби Оби-Ван"

""" Создайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
конструктор __init__, принимающий произвольное количество аргументов. Среди всех переданных аргументов 
необходимо оставить только целые числа и сохранить их в атрибут values в виде списка;
переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом: 
"Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой. При этом значения должны быть 
упорядочены по возрастанию (будьте аккуратнее с пробелами, они стоят только после запятых, см. пример ниже);
"Пустой вектор", если наш вектор не хранит в себе значения """


class Vector:

    def __init__(self, *args):
        self.values = [x for x in args if type(x) == int]

    def __str__(self):
        if self.values == []:
            return "Пустой вектор"
        s = "Вектор("
        self.values.sort()
        return "Вектор(" + ','.join([str(x) for x in self.values]) + ')'


v1 = Vector(1, 2, 3)
print(v1)  # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2)  # печатает "Пустой вектор"

#####################################################################
print()
print('VECTOR 2')
print()


class Vector:
    def __init__(self, *args):
        self.values = sorted([x for x in args if type(x) == int])

    def __str__(self):
        if self.values == []:
            return "Пустой вектор"
        return "Вектор(" + ', '.join([str(x) for x in self.values]) + ')'

    def __add__(self, v):
        if type(v) == int:
            return Vector(*[x + v for x in self.values])
        elif type(v) == Vector:
            if len(self.values) != len(v.values):
                return "Сложение векторов разной длины недопустимо"
            n = [x for x in v.values if type(x) != int]
            if n != []:
                return f"Вектор нельзя сложить с {n[0]}"
        else:
            return f"Вектор нельзя сложить с {v}"
        return Vector(*[w[0] + w[1] for w in list(zip(self.values, v.values))])

    def __mul__(self, v):
        if type(v) == int:
            return Vector(*[x * v for x in self.values])
        elif type(v) == Vector:
            if len(self.values) != len(v.values):
                return "Умножение векторов разной длины недопустимо"
            n = [x for x in v.values if type(x) != int]
            if n != []:
                return f"Вектор нельзя умножать с {n[0]}"
        else:
            return f"Вектор нельзя умножать с {v}"
        return Vector(*[w[0] * w[1] for w in list(zip(self.values, v.values))])


v1 = Vector(1, 2, 3)
print(v1)  # печатает "Вектор(1, 2, 3)"

v2 = Vector(3, 4, 5)
print(v2)  # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3)  # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4)  # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5)  # печатает "Вектор(2, 4, 6)"
print(v5 + 'hi')  # печатает "Вектор нельзя сложить с hi"
print(v5 + [3, 4])
print(v5 + 'hello')


###############################################################################################

class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.rating == other
        elif isinstance(other, ChessPlayer):
            return self.rating == other.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.rating > other
        elif isinstance(other, ChessPlayer):
            return self.rating > other.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.rating < other
        elif isinstance(other, ChessPlayer):
            return self.rating < other.rating
        else:
            return 'Невозможно выполнить сравнение'


print()
print('CHESS CLASS')
magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000)  # False
print(ian == 2789)  # True
print(magnus == ian)  # False
print(magnus > ian)  # True
print(magnus < ian)  # False
print(magnus < [1, 2])  # печатает "Невозможно выполнить сравнениe"


###############################################################################################

class City:

    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return self.name[-1] not in 'aeiou'


p1 = City('new york')
print(p1)  # печатает "New York"
print(bool(p1))  # печатает "True"
p2 = City('SaN frANCISco')
print(p2)  # печатает "San Francisco"
print(p2 == True)  # печатает "False"


#####################################################################################################


class Quadrilateral:

    def __init__(self, width=None, height=None):
        self.width = height if width == None else width
        self.height = width if height == None else height

    def __str__(self):
        if self.width == self.height:
            return f'Куб размером {self.width}х{self.height}'
        return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return self.width == self.height


q1 = Quadrilateral(10)
print(q1)  # печатает "Куб размером 10х10"
print(bool(q1))  # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)  # печатает "Прямоугольник размером 3х5"
print(q2 == True)  # печатает "False"


################################################################################

class NewInt(int):

    def __init__(self, num):
        self.num = num

    def repeat(self, n=2):
        return int(str(self.num) * n)

    def to_bin(self):
        return int((bin(self.num))[2:])


a = NewInt(9)
print(a.repeat())  # печатает число 99
d = NewInt(a + 5)
print(d.repeat(3))  # печатает число 141414
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin())  # печатает 100011 - двоичное представление числа 35


################################################################################################

class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f"Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч"


class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue=0):
        super().__init__(brand, max_speed)
        self.kind = 'Car'
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f"Осталось бензина на {self.__gasoline_residue} км"

    @gasoline.setter
    def gasoline(self, value):
        if not isinstance(value, int):
            print('Ошибка заправки автомобиля')
        else:
            self.__gasoline_residue += value
            print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')


class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed)
        self.kind = 'Boat'
        self.owners_name = owners_name

    def __str__(self):
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'


class Plane(Transport):
    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed)
        self.kind = 'Plane'
        self.capacity = capacity

    def __str__(self):
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'


transport = Transport('Telega', 10)
print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
bike = Transport('shkolnik', 20, 'bike')
print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч
first_plane = Plane('Virgin Atlantic', 700, 450)
print(first_plane)  # Самолет марки Virgin Atlantic вмещает в себя 450 людей
first_car = Car('BMW', 230, 75000, 300)
print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
print(first_car.gasoline)  # Осталось бензина на 300 км
first_car.gasoline = 20  # Печатает 'Объем топлива увеличен на 20 л и составляет 320 л'
print(first_car.gasoline)  # Осталось бензина на 320 км
second_car = Car('Audi', 230, 70000, 130)
second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
first_boat = Boat('Yamaha', 40, 'Petr')
print(first_boat)  # Этой лодкой марки Yamaha владеет Petr


##################################################################################################


class Initialization:
    def __init__(self, capacity, food):
        if not isinstance(capacity, int):
            print('Количество людей должно быть целым числом')
        else:
            self.capacity = capacity
            self.food = food


class Vegetarian(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}"


class MeatEater(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'


class SweetTooth(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'

    def __eq__(self, other):
        if isinstance(other, int):
            return self.capacity == other
        elif isinstance(other, (MeatEater, Vegetarian)):
            return self.capacity == other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.capacity < other
        elif isinstance(other, (MeatEater, Vegetarian)):
            return self.capacity < other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'

    def __gt__(self, other):
        if isinstance(other, int):
            return self.capacity > other
        elif isinstance(other, (MeatEater, Vegetarian)):
            return self.capacity > other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'


v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом
m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
print(s_first > v_first)  # True
print(30000 == s_first)  # True
print(s_first == 25000)  # False
print(100000 < s_first)  # False
print(100 < s_first)  # True

##################################################################################################


class Wallet:

    def __init__(self, currency, balance):
        if type(currency)!=str:
            raise TypeError('Неверный тип валюты')
        elif type(currency)==str and len(currency)!=3:
            raise NameError('Неверная длина названия валюты')
        elif type(currency)==str and len(currency)==3 and any([x for x in currency if x.islower()]):
            raise ValueError('Название должно состоять только из заглавных букв')
        else:
            self.currency = currency
        self.balance = balance

    def __eq__(self, other):
        if type(other)!=Wallet:
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')
        elif self.currency!=other.currency:
            raise ValueError('Нельзя сравнить разные валюты')
        else:
            return self.balance==other.balance

    def __add__(self, other):
        if type(other)!=Wallet or self.currency!=other.currency:
            raise ValueError(f'Данная операция запрещена')
        else:
            return Wallet(self.currency, self.balance+other.balance)

    def __sub__(self, other):
        if type(other)!=Wallet or self.currency!=other.currency:
            raise ValueError(f'Данная операция запрещена')
        else:
            return Wallet(self.currency, self.balance-other.balance)


print()
print('*'*50)
print('WALLET')
wallet1 = Wallet('USD', 50)
wallet2 = Wallet('RUB', 100)
wallet3 = Wallet('RUB', 150)
wallet4 = Wallet(12, 150)  # исключение TypeError('Неверный тип валюты')
wallet5 = Wallet('qwerty', 150)  # исключение NameError('Неверная длина названия валюты')
wallet6 = Wallet('abc', 150)  # исключение ValueError('Название должно состоять только из заглавных букв')
print(wallet2 == wallet3)  # False
print(wallet2 == 100)  # TypeError('Wallet не поддерживает сравнение с 100')
print(wallet2 == wallet1)  # ValueError('Нельзя сравнить разные валюты')
wallet7 = wallet2 + wallet3
print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
wallet2 + 45  # ValueError('Данная операция запрещена')






