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
