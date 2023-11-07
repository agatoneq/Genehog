from tkinter import *

window = Tk()
window.geometry('640x640')

def remove_widgets():
    for widget in window.winfo_children():
        widget.destroy()

l = Label(window, text='Jakie imiona chcesz wygenerować?')
l.place(x=250, y=10)

def f_buttonM():
    remove_widgets()
    entryM = Entry(window, width=5)
    entryM.place(x=200, y=50)

buttonM = Button(window, text='meskie', width=10, command=f_buttonM)
buttonM.place(x=200, y=50)

def f_buttonO():
    f_buttonM()
    entryD = Entry(window, width=5)
    entryD.place(x=200, y=80)

buttonO = Button(window, text='oba', width=10, command=f_buttonO)
buttonO.place(x=300, y=50)

def f_buttonD():
    remove_widgets()
    entryD = Entry(window, width=5)
    entryD.place(x=200, y=50)

buttonD = Button(window, text='damskie', width=10, command=f_buttonD)
buttonD.place(x=400, y=50)



#, command=f_button1

window.mainloop()