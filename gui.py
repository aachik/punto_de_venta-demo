#!/usr/bin/python3.4
from tkinter import Tk
from tkinter import Entry
from tkinter import Button
from tkinter import Label
from tkinter import Text
from tkinter import Frame
from tkinter import END


class GUI:


	def __init__(self):
		self.cuadro = Tk()
		cuadro.title("AbNet Bot - Punto de venta")


		self.f = Frame(width = 1024, height = 768)
		self.f.pack()

		self.label = Label(frame, text="GUI del programa")
	    self.label.pack()
		
		self.cuadro.mainloop()

	def LogIn():
    	username = input("Por favor introdusca su nombre de usuario")
    	password = input("Por favor introdusca su password:")
   
 x


if __name__ == "__main__": GUI()
