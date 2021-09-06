"""
Режимы открытия файлов:
r - чтение
w - перезапись
a - добввление записи в файл
b - бинарный режим
"""

# Рекурсывный обход файлов

import os

path = 'C:\\Movies'
print(os.listdir(path))

def obxodFile(path, level=1):
    print('Level=', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            print('Going down', path+'\\'+i)
            obxodFile(path+'\\'+i,level+1)
            print('Going back', path)

        print(i, type(i), path+'\\'+i, os.path.isdir(path+'\\'+i)) # is this directory?

#

file = open(r'myfile.txt', encoding='utf-8')
print(file.read(50)) # read 50 symbols
file.seek() # go back to start of the file
print(file.readline()) # read one line

for row in file:
    for letter in row:
        print(letter)
file.close()

file2 = open('myfile.txt', 'w', encoding='utf-8') # write in file (clean writen before)
file2.write('hello\n')
file2.write('what is your name?\n')
file2.close()

file3 = open('myfile.txt', 'a', encoding='utf-8') # write in file not cleaning writen before
file3.write('This is second note')
file3.close() # if error before file will not be closed

# JSON
import json

str_json="""
    И тут дофига текста
"""
data = json.loads(str_json)
print(type(data)) # dictionary
print(data['key of dictionary']['next key']) # get value
for i in data['key']['key 2']:
    print(i['some key'], i['some key'])
    del data('id')
    item['likes']=randint(100,200)

new_json = json.dumps(data, indent=2) # data to json

with open('my.json', 'w') as file:
    json.dump(data, file) # write data in json file

with open('my.json', 'r') as f:
    data = json.load(f)

print(data)
print(type(data))







