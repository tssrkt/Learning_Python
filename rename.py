import os
from tkinter import *
from tkinter import filedialog as fd

def selectDir():
    return fd.askdirectory()+'/'

def startRename(directory):
    directory1=directory.replace('/', '\\')
    ext = ent1.get()
    files=sorted([path for path in os.listdir(directory) if os.path.isfile(directory+path) and path.endswith(ext)])
    i=1

    while files:
        file=files[0]
        if not os.path.isfile(f'{directory}{i}.{ext}'):
            name = f'{i}.{ext}'
            os.rename(directory1+file, directory1+name)
            del files[0]
        i+=1


root = Tk()
root.geometry('350x75')

l1=Label(text='Расширение файла (без точки)')
l1.grid(row=0, column=0)

ent1 = Entry()
ent1.grid(row=1, column=0)

b1 = Button(text='Выбрать папку', command=lambda: startRename(selectDir()))
b1.grid(row=0,column=1)

root.mainloop()
