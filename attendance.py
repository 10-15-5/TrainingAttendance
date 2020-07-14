import csv
from tkinter import *
import tkinter.messagebox as tm
import os

root = Tk()


def welcomescreen():
    root.title('Welcome!')
    fr = Frame(root)

    message = "Welcome the hurling attendance program!\nThis program is still under construction but please" \
              " enjoy it in it's current state.\nAny feedback is appreciated."

    Label(root, text=message).pack()
    Button(fr, text='Quit', command=root.quit).grid(row=3)
    Button(fr, text='Go', command=readfile).grid(row=3, column=1)

    fr.pack()
    fr.mainloop()


def readfile():
    with open ("hurling.csv") as file:
        f = file.read()
        file.close()

        print(f)




welcomescreen()