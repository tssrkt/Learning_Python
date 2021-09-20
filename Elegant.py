# put your python code here
# a = float(input())
# b = float(input())
# c = input()

z_div = 'Деление на 0!'
OPERATORS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y else z_div,
    "mod": lambda x, y: x % y if y else z_div,
    "div": lambda x, y: x // y if y else z_div,
    "pow": lambda x, y: x ** y
}


# print(OPERATORS[c](a, b))

# put your python code here
# x = int(input())

# if x%10==1 and (x%100)//10!=1:
#     print(str(x) + ' программист')
# elif x%10 in [2,3,4] and (x%100)//10!=1:
#     print(str(x) + ' программиста')
# elif (x%100)//10==1 or x%10 in [0,5,6,7,8,9]:
#     print(str(x) + ' программистов')

# Все исключения вместе
def printExcTree(thisclass, nest=0):
    if nest > 1:
        print(" |" * (nest - 1), end="")
    if nest > 0:
        print(" +---", end="")
    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        printExcTree(subclass, nest + 1)


printExcTree(BaseException)

###################################

heroes = {
    'Spiderman': 80,
    'Batman': 65,
    'Superman': 85,
    'Wonder Woman': 70,
    'Flash': 70,
    'Ironman': 65,
    'Thor': 90,
    'Aquaman': 65,
    'Captain America': 65,
    'Hulk': 87,
}

# Сортировка сначала по значению, потом - по ключу
for x in sorted(heroes.items(), key=lambda pair: (pair[1], pair(0))):
    print(x)

d = lambda x: 'Like' if x > 100 else ('Subscribe' if x > 0 else 'Follow')
print(d(10))
