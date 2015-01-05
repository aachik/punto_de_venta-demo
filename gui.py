from tkinter import Tk
from tkinter import Frame

class GUI:


	def __init__(self):
		self.cuadro = Tk()

		self.f = Frame(width = 1024, height = 768)
		self.f.pack()
		self.cuadro.mainloop()


if __name__ == "__main__": GUI()

