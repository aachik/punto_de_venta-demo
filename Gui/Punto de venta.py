#!/usr/bin/python3.4
from tkinter import *

pvv = Tk()
pvv.title("AbsNet Bot - Punto de venta")
pvv.geometry("800x600")


# Esto es para centrar la ventana
pvv.withdraw()
pvv.update_idletasks()  
x = (pvv.winfo_screenwidth() - pvv.winfo_reqwidth()) / 4
y = (pvv.winfo_screenheight() - pvv.winfo_reqheight()) / 7
pvv.geometry("+%d+%d" % (x, y))


pvv.deiconify()

#La lista, que no se como ponerle un titulo
option = OptionMenu(pvv,"Tipo" ,"Menudeo", "Mayorista")
option.grid(row=0, sticky=W)

#Boton de Cerras sesion
logoutbutton = Button(pvv, text="Cerrar sesion")
logoutbutton.grid(row=0, sticky=E,column=4)

#El primer frame
f = Frame(pvv)
f.grid(row=1)

#scrollbar = Scrollbar(f, orient="vertical")

nombrearticulos = Listbox(f,width=20, height=35, )#yscrollcommand=scrollbar.set)
nombrearticulos.grid(row=0, column=0)
nombrearticulos.insert(END, "")

#No se como poner el scroll con grid
#scrollbar.config(command=nombrearticulos.yview)
#scrollbar.grid(row=0,column=1, sticky=W)


precioarticulos = Listbox(f,width=20, height=35, )#yscrollcommand=scrollbar.set)
precioarticulos.grid(row=0, column=1)
precioarticulos.insert(END, "")
#No se como poner el scroll con grid
#scrollbar.config(command=precioarticulos.yview)
#scrollbar.grid(row=0,column=3)

cantidadarticulos = Listbox(f,width=20, height=35,)# yscrollcommand=scrollbar.set)
cantidadarticulos.grid(row=0, column=2)
cantidadarticulos.insert(END, "")

#No se como poner el scroll con grid
#scrollbar.config(command=nombrearticulos.yview)
#scrollbar.grid(row=0,column=5)

#La entrada de efectivo
Label(f, text="Efectivo:").grid(row=1, sticky=W)
e1 = Entry(f)
e1.grid(row=1, column=1)



#Segundo Frame
f2 = Frame(pvv)
f2.grid(row=1, column=2)


#No tengo bien definido con que metodo quiero hacer el total, asi que por ahora lo hice asi
Label(f2, text="Total:").grid(row=2,column=1)
Total = Label(f2, text="Suma")
Total.grid(row=2,column=2)

# Trabajo pediente
#	* Hacerlo mas bonito
#	* Orientarlo ha objetos
#	* Definir el total
#	* Saber usar el Scrollbar

pvv.mainloop()