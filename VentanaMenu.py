from tkinter import *
from tkinter import ttk
import Conexion
from Conexion import *
#import Equipos
import Equipos
from Equipos import *
#from Equipos import posiciones
import Partidos
from Partidos import *
import Posiciones
from Posiciones import *


# img_Partidos=PhotoImage(file="Partidos.png")
# img_estadistica=PhotoImage(file="Tabla.png")


    #raiz = Tk()
# Equipos.claseEquipos=classEquipos()


class Menu(Frame):
    def __init__(self, raiz):
        LabelTitulo = Label(raiz, text="Liga de Futbol")
        LabelTitulo.grid(row=0, column=5, padx=700, pady=10, sticky='nsew')
        LabelTitulo.config(bg="#A11FFF", fg="white", font=('Lucida Sans', 25, 'bold'), borderwidth=0, activebackground='white')

        # self.menulateralFrame=Frame(self.raiz)
        # #self.menulateralFrame.grid_propagate(0)#Sirve para que el alto y el ancho del frame se establescan correctamente,#por defecto esta en 1 cuando no se declara
        # self.menulateralFrame.grid(row=1, column=0,sticky='wn')
        # self.menulateralFrame.config(width=0, height=10,relief="groove",bg='#AAA000')#Tamaño del fram, para que este surja efecto el de la self.raiz debe estar desactivado

        self.img_registrarEq = PhotoImage(file="Equipos2.png")
        self.teams = Button(raiz, text=" Insertar", compound=LEFT, image=self.img_registrarEq, command=self.openVentanaEquipos)
        self.teams.grid(row=1, column=0,  sticky="nsew", pady=40)
        self.teams.config(bg="#000000", fg="white", font=('Lucida Sans', 12, 'bold'), borderwidth=0, activebackground='black')
        # self.teams.grid_propagate(0)

        self.img_Partidos = PhotoImage(file="Partidos.png")
        self.matchday = Button(raiz, text="Partidos", compound=LEFT, image=self.img_Partidos, command=self.openPartidos)
        self.matchday.grid(row=2, column=0,  sticky='nsew', pady=30)
        self.matchday.config(bg="#000000", fg="white", font=('Lucida Sans', 12, 'bold'), borderwidth=0, activebackground='black')
        # self.matchday.grid_propagate(0)

        self.img_Estadisticas = PhotoImage(file="Tabla.png")
        self.Tabla_Posiciones = Button(raiz, text="posiciones", compound=LEFT,image=self.img_Estadisticas, command=self.openEstadisticas)
        self.Tabla_Posiciones.grid(row=3, column=0,  sticky='nsew', pady=40)
        self.Tabla_Posiciones.config(bg="#000000", fg="white", font=('Lucida Sans', 12, 'bold'), borderwidth=0, activebackground='black')
        # self.matchday.grid_propagate(0)
        # self.paginas = ttk.Notebook(self.frame_principal , style= 'TNotebook') #, style = 'TNotebook'
        # self.paginas.grid(column=0,row=0, sticky='nsew')
        # self.paginas.add(self.frame_dos)

    def openVentanaEquipos(self):
        #classEquipos()
        Equipos.classEquipos()


    def openPartidos(self):
        Partidoss()
        #Partidos.Partidoss()
        # Partidos.Partidoss.match(self)

    def openEstadisticas(self):
        Posicioness()
        #Posicioness()





if __name__ == '__main__':
    raiz = Tk()
    claseMenu = Menu(raiz)
    raiz.title("Menu")
    raiz.geometry("1920x1080")
    raiz.resizable(0, 0)
    barramenu = Menu(raiz)
    raiz.config(bg="#000000")
    #raiz.config()
    
    #claseMenu = Menu()
    #clasePosiciones=Posicioness()
    raiz.mainloop()
