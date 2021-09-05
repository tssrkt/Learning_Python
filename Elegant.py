# put your python code here
a = float(input())
b = float(input())
c = input()

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
print(OPERATORS[c](a, b))

# put your python code here
x = int(input())

if x%10==1 and (x%100)//10!=1:
    print(str(x) + ' программист')
elif x%10 in [2,3,4] and (x%100)//10!=1:
    print(str(x) + ' программиста')
elif (x%100)//10==1 or x%10 in [0,5,6,7,8,9]:
    print(str(x) + ' программистов')

