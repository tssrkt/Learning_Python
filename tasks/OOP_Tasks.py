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

print(jack.description()) # распечатает 'Jack is 4 years old'
print(jack.speak("Woof Woof")) # распечатает 'Jack says Woof Woof'
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
        if email.count('@')==1 and email.find('.', email.find('@'))!=-1:
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

print('*'*50)
print('MONEY')


class Money:

    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, x):
        if isinstance(x, (int)) and x>=0:
            self.total_cents = self.total_cents % 100 + x * 100
        else:
            print("Error dollars")


    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, x):
        if isinstance(x, (int)) and 0<=x< 100:
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
print('*'*50)
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

r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many() # печатает "1, вот сколько нас еще осталось"
r2.destroy() # печатает "Робот R2-D2 был уничтожен"
