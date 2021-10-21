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

x = 512
y = len(f'{x - 1:b}')
print(y)
print(2 ** y)

print(f'{31:010b}')
print(f'{31:015b}')
print(f'{31.743:0.2f}')
print(f'*{31:^10}*')
print(f'*{31:!=10}*')
print(f'*{31:x}*')
print(f'*{65:c}*')
a, b = 71, 13
print(f'*{a:0{b}b}*')
aaa, bbb = 71, 13
print(f'*{aaa:0{bbb}b}*--*{bbb:^20}*')

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

for i in range(9)[::-1]:
    row, col = divmod(i, 3)
    if not matrix[row][col]:
        matrix[row][col] = 2
        break

line = sum(matrix,[])[::-1]
row, col = divmod(8 - line.index(0), 3)
matrix[row][col] = 2


