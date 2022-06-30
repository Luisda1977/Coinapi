from tkinter import *
from tkinter import ttk


root = Tk()

marco = ttk.Frame(root, padx=20)
marco.grid()

etiqueta = Label(root, text="Hola Tkinter", padx=50, pady=25)
etiqueta.grid(row=0, column=0)

otra = Label(root, text="Soy otra etiqueta", fg="blue", bg="black")
otra.grid(row=5, column=0, columnspan=4)

vacia = Label(marco, text="", padx=50, pady=50)
vacia.grid(row=3, column=1)

root.mainloop()
