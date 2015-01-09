#!/usr/bin/python3.4
from tkinter import *

vl = Tk()
vl.title("AbsNet Bot - Log - in")

Label(vl, text="Nombre de usuario:").grid(row=0, sticky=W)
Label(vl, text="Password:").grid(row=1, sticky=W)

e1 = Entry(vl)
e2 = Entry(vl)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b =  Button(vl,text="Iniciar sesion").grid(sticky=E, row=3)
vl.mainloop()

# Trabajo pediente
#	* Orientarlo ha objetos