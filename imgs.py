from tkinter import *
from tkinter import ttk

raiz=Tk()
raiz.title("Menu")
raiz.geometry("1800x700")
raiz.config(bg="#111111")
raiz.resizable(0,0)


menulateralFrame=Frame(raiz)
menulateralFrame.grid_propagate(0)#Sirve para que el alto y el ancho del frame se establescan correctamente,#por defecto esta en 1 cuando no se declara
menulateralFrame.grid(column=0, row=1, sticky='nsew')
menulateralFrame.config(bg="#E98232")#color del frame
menulateralFrame.config(width="1450", height="200")#Tamaño del fram, para que este surja efecto el de la raiz debe estar desactivado
menulateralFrame.config(bd=2)#tamaño al borde del frame
menulateralFrame.config(relief="raised")#tipo de marco para el frame



img_registrarEq=PhotoImage(file="Equipos2.png")
#labelimg=Label(menulateralFrame,image=img_registrarEq)
#labelimg.grid(column=0,row=1)
Butt=Button(menulateralFrame,image=img_registrarEq)
Butt.grid(column=0, row=1)

raiz.mainloop()