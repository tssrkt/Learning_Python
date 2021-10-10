import re

text = 'map google, gooogle, goooooogle 0xf, 0xa, 0x5 12 35 4 2'
# print(re.findall(r'\map\b', text))
print(re.findall(r'[0123456789][0123456789]', text)) # two numbers one by one
print(re.findall(r'[0-9]', text))  # numbers
print(re.findall(r'[^0-9]', text))  # everything except numbers
print(re.findall(r'[a-z]', text))  # all letters lowercase
print(re.findall(r'[a-zA-Z]', text))  # all letter upper and lower
print(re.findall(r'[a-zA-Z0-9]', text))  # letters and numbers
print(re.findall(r'\w', text))  # words
print(re.findall(r'\w', text, re.ASCII))  # numbers only
print(re.findall(r'0x[\da-fA-F]', text))
print(re.findall(r'o{2,5}', text))  # o repeating from 2 to 5 times
print(re.findall(r'o{2,5}?', text))  # minor
print(re.findall(r'o{2,}', text))  # repeat from 2 and more times
print(re.findall(r'o{,2}', text))  # not more 2 repeats
print(re.findall(r'8\d{10}', text))  # first 8 and then 10 numbers
# print(re.findall(r'{0,}', text))  # from 0 to infinite
# print(re.findall(r'{,1}', text))  # from 0 to 1
print(re.findall(r'mann?er', text))  # n before ? is not strict
print(re.findall(r'\w+\s*=\s*[^;]+', text))  # word maybe space = maybe space ...
print(re.findall(r'', text))
print()
print('START')
print(re.findall(r'[\w\W\s]', 'somefile.txt'))
