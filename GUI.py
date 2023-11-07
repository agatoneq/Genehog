import random
from tkinter import *

def display_list(list1, amount, o):
    numbers = set()
    while len(numbers) < int(amount):
        numbers.add(random.randint(1, len(list1)) - 1)

    result = ""
    for i in range(int(amount)):
        result += (list1[list(numbers)[i]]) + '\n'
    if o == True:
        label_result2.config(text=result)
        label_result2.place(x=300, y=20)
    else:
        label_result1.config(text=result)
        label_result1.place(x=200, y=20)


def make_list(file_name, amount, o):
    list1 = []
    with open(file_name, 'rt') as file:
        for line in file:
            list1.append(line.strip())
    display_list(list1, amount, o)


window = Tk()
window.geometry('640x640')

def remove_widgets():
    for widget in window.winfo_children():
        widget.place_forget()

l = Label(window, text='Jakie imiona chcesz wygenerować?')
l.place(x=250, y=10)

label_result1 = Label(window, text='')
label_result2 = Label(window, text='')

#przypadek1
def f_buttonConfirmM():
    remove_widgets()
    make_list('imiona_meskie.txt', entryM.get(), False)
    #names_list= Label(window, text=make_list('imiona_meskie.txt', 4)).place(x=200, y=20)

entryM = Entry(window, width=5)
def f_buttonM():
    remove_widgets()
    labelM = Label(window, text='Wprowadź liczbę imion męskich').place(x=200, y=20)
    entryM.place(x=270, y=50)
    buttonConfirmM = Button(window, text='Zatwierdź', width=10, command=f_buttonConfirmM).place(x=350, y=50)

buttonM = Button(window, text='meskie', width=10, command=f_buttonM).place(x=200, y=50)


#przypadek2
def f_buttonConfirmO():
    remove_widgets()
    make_list('imiona_meskie.txt', entryM.get(), False)
    make_list('imiona_damskie.txt', entryD.get(), True)

def f_buttonO():
    remove_widgets()
    labelM = Label(window, text='Wprowadź liczbę imion męskich').place(x=200, y=20)
    entryM.place(x=270, y=50)
    labelD = Label(window, text='Wprowadź liczbę imion damskich').place(x=200, y=80)
    entryD.place(x=270, y=110)
    buttonConfirmO = Button(window, text='Zatwierdź', width=10, command=f_buttonConfirmO).place(x=250, y=140)

buttonO = Button(window, text='oba', width=10, command=f_buttonO).place(x=300, y=50)


#przypadek3
def f_buttonConfirmD():
    remove_widgets()
    make_list('imiona_damskie.txt', entryD.get(), False)

entryD = Entry(window, width=5)

def f_buttonD():
    remove_widgets()
    labelD = Label(window, text='Wprowadź liczbę imion damskich').place(x=200, y=20)
    entryD.place(x=270, y=50)
    buttonConfirmD = Button(window, text='Zatwierdź', width=10, command=f_buttonConfirmD).place(x=350, y=50)

buttonD = Button(window, text='damskie', width=10, command=f_buttonD).place(x=400, y=50)


window.mainloop()