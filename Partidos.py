from cProfile import label
from tkcalendar import Calendar
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Conexion
from Conexion import *

"""-----------------Clase de la Pantalla donde se asignaran los partidos que se disputaran-----------------------------------------------"""
"""-----------------esto se debe hacer automatico cumpliendo la norma de dos partidos entre equipos, y si ya se enfrentaron 
--------------------no pueden volver a jugar entre ellos, debe tener la posibilidad que si el partido no se puede jugar en 
--------------------la fecha establecida debe reprogamarse"""

class Partidoss(Toplevel):
    def __init__(self):
        self.Framepartidos = Frame()
        self.Framepartidos.grid(row=2, column=5, sticky='e', padx=40)
        self.Framepartidos.config(bg="#A11FFF")  # color del frame
        # Tamaño del fram, para que este surja efecto el de la self.VentanaEquipos debe estar desactivado
        self.Framepartidos.config(width="830", height="370")
        self.Framepartidos.grid_propagate(0)
        self.Framepartidos.grid_propagate(0)
        # tipo de marco para el frame
        self.Framepartidos.config(relief="raised")

        """Configuracion para darle estilo a la tabla de treeview"""
        stilos=ttk.Style()
        stilos.theme_use("clam")#default,clam,alt
        stilos.configure("Treeview", 
        background="pink",
        forefround="black",
        rowheight=25,#El tamaño de la sombra que se mostrara al seleccionar un item
        fieldbackground="silver",
        font="Arial"
        )
        stilos.map("Treeview", 
        background=[('selected', 'green')]
        )
        """Creando tablas para mostrar datos de la tabla Equipos"""
        self.Tablapartidos=ttk.Treeview(self.Framepartidos, columns=("#1","#2","#3","#4") )
        #self.TabTablapartidosla.config(width="1700", height="700")
        self.Tablapartidos.grid(row=4, column=7,columnspan=12, padx=10,pady=2, sticky="nsew")
        #self.Tablapartidos.bind("<Double-Button-1>", self.FuncDobleclickTabla)#El -1 es para el boton izquierdo del raton y el -2 es para el boton derecho del raton y el -3 para el boton de enmedio
        self.Tablapartidos.heading("#0", text="ID", anchor=CENTER)
        self.Tablapartidos.column("#0", width=60, anchor=E )
        self.Tablapartidos.heading("#1", text="Equipo1", anchor=CENTER)
        self.Tablapartidos.column("#1", width=250, anchor=CENTER)
        self.Tablapartidos.heading("#2", text="Equipo2", anchor=CENTER)
        self.Tablapartidos.column("#2", width=250, anchor=CENTER)
        self.Tablapartidos.heading("#3", text="Fecha", anchor=CENTER)
        self.Tablapartidos.column("#3", width=160, anchor=CENTER)
        self.Tablapartidos.heading("#4", text="Jornada", anchor=CENTER)
        self.Tablapartidos.column("#4", width=85, anchor=CENTER)

        guardarEQBT = Button(self.Framepartidos,text="Ingresar Partido", command=self.match)
        guardarEQBT.grid(row=10, column=7, sticky='s', pady=6)
        guardarEQBT.config(bg="#000000", fg="white", font=('Lucida Sans', 12, 'bold'), borderwidth=2, activebackground='black')


    def match(self):
        Conexion.Cone = DataBase()
        #Consulta a la base
        Conexion.Cone.cursor.execute("SELECT * FROM  Equipos")
        #Variable para guardar lo extraido de la base con el select
        valoresextraidos=Conexion.Cone.cursor.fetchall()
        #----------------------------Ciclo for para  que los registros no se muestren repeditos al consultarlos
        registros=self.Tablapartidos.get_children()
        #print(registros)
        for registro in registros:
            self.Tablapartidos.delete(registro)
        #----------------------------ciclo for para mostrar los regirstros en la tabla
        for (Id,Nombre) in valoresextraidos:
            self.Tablapartidos.insert('',0, text=Id, values=Nombre )#Si le pongo 1 los muestra en orden de menor a mayor 
                #y si le pongo 0 los muestra de mayor a menor
        Conexion.Cone.connec.commit()
        

        """Para poder ingresar un partido debo obetener el EQ1 y el EQ2, Ponerle Fecha, la jornada que se esta jugando,
        Que se haga automaticamente que los empareje y los inserte en la tabla, asi ya no tendra que ingresar nada el usuario
        Obtener de la tabla Equipos los ids de los dos equipos que se van a enfrentar e insertar en la tabla obtener 
        el primero y el ultimo y asi sucesivamente Ingresar  la fecha con la jornada son diez juegos por dia osea por jornada """


    """Una ves ingresados los equipos en la tabla se debe poder modificar la fecha de juego y jornada ademas de poder buscar equipos por nombre"""



        # cal = Calendar(self.Framepartidos, selectmode='day',year=2022, month=1, day=22)
        # cal.grid(row=7, column=5, pady=6, padx=5)

        # self.equipo1LB = Label(self.Framepartidos, text="Seleccionar Equipos")
        # self.equipo1LB.grid(row=3, column=0)
        # self.equipo1LB.config(bg="#8A2BE2", fg="#000000", font="italic")

        # self.Equipo1 = ttk.Combobox(self.Framepartidos)
        # self.Equipo1["values"] = ["Barcelona","Real Madrid", "Osasuna", "Atletico de Madrid"]
        # self.Equipo1.current(0)
        # self.Equipo1.grid(row=3, column=1, pady=4)

        # self.LBVersus = Label(self.Framepartidos, text=" VS ")
        # self.LBVersus.grid(row=3, column=2)
        # self.LBVersus.config(bg="#8A2BE2", fg="#000000", font="italic")

        # self.Equipo2 = ttk.Combobox(self.Framepartidos)
        # self.Equipo2["values"] = ["Barcelona","Real Madrid", "Osasuna", "Atletico de Madrid"]
        # self.Equipo2.current(3)
        # self.Equipo2.grid(row=3, column=3, padx=6)
        # guardarEQBT = Button(self.Framepartidos,text="Ingresar Partido", command=self.match)
        # guardarEQBT.grid(row=3, column=5,  sticky="nsew")
        # guardarEQBT.config(bg="#000000", fg="white", font=(
        #     'Lucida Sans', 12, 'bold'), borderwidth=0, activebackground='black')