import imp
from tkinter import *
from tkinter import ttk
import Conexion
from Conexion import *


"""---------------------------Clase de la Pantalla donde se mostraran las Posiciones actuales de los equipos--------------------"""
class Posicioness:
    def __init__(self):
        """Frame donde se encuentra la tabla donde se mostraran los datos de al DB"""
        self.Frameposiciones=Frame()
        self.Frameposiciones.grid(row=2, column=5)
        self.Frameposiciones.config(bg="#A11FFF")#color del frame
        self.Frameposiciones.config(width="630", height="350")#Tamaño del fram, para que este surja efecto el de la self.VentanaEquipos debe estar desactivado
        self.Frameposiciones.grid_propagate(0)
    #self.Frameposiciones.config(bd=2)#tamaño al borde del frame
        self.Frameposiciones.config(relief="raised")#tipo de marco para el frame

        """Configuracion para darle estilo a la tabla de treeview"""
        stilos=ttk.Style()
        stilos.theme_use("clam")#default,clam,alt
        stilos.configure("Treeview", 
        background="silver",
        forefround="black",
        rowheight=25,#El tamaño de la sombra que se mostrara al seleccionar un item
        fieldbackground="silver",
        font="Arial"
        )
        stilos.map("Treeview", 
        background=[('selected', 'green')]
        )

        """Creando tablas para mostrar datos de la tabla Equipos"""
        self.Tabla=ttk.Treeview(self.Frameposiciones, columns=("#1","#2","#3","#4","#5","#6","#7","#8","#9") )
        #self.Tabla.config(width="1700", height="700")
        self.Tabla.grid(row=16, column=9,columnspan=10, padx=12, pady=12, sticky="nsew")
        #self.Tabla.bind("<Double-Button-1>")#El -1 es para el boton izquierdo del raton y el -2 es para el boton derecho del raton y el -3 para el boton de enmedio
        self.Tabla.heading("#0", text="ID", anchor=CENTER)
        self.Tabla.column("#0", width=50, anchor=E )
        self.Tabla.heading("#1", text="Club", anchor=CENTER)
        self.Tabla.column("#1", width=150, anchor=CENTER)
        self.Tabla.heading("#2", text="PJ", anchor=CENTER)
        self.Tabla.column("#2", width=50, anchor=CENTER)
        self.Tabla.heading("#3", text="G", anchor=CENTER)
        self.Tabla.column("#3", width=50, anchor=CENTER)
        self.Tabla.heading("#4", text="E", anchor=CENTER)
        self.Tabla.column("#4", width=50, anchor=CENTER)
        self.Tabla.heading("#5", text="P", anchor=CENTER)
        self.Tabla.column("#5", width=50, anchor=CENTER)
        self.Tabla.heading("#6", text="GF", anchor=CENTER)
        self.Tabla.column("#6", width=50, anchor=CENTER)
        self.Tabla.heading("#7", text="GC", anchor=CENTER)
        self.Tabla.column("#7", width=50, anchor=CENTER)
        self.Tabla.heading("#8", text="DG", anchor=CENTER)
        self.Tabla.column("#8", width=50, anchor=CENTER)
        self.Tabla.heading("#9", text="Pts", anchor=CENTER)
        self.Tabla.column("#9", width=50, anchor=CENTER)

        botonviewposiciones=Button(self.Frameposiciones, text="Mostrar Equipos", command=self.TablaPosiciones )#crea un boton con texto dentro y se le pasa la funcion boton1
        botonviewposiciones.config(bg="#008B8B", fg="#191970", font=("Courier", 12, "italic"))
        botonviewposiciones.grid(row=19, column=13,pady=4,sticky="nes")

    def TablaPosiciones(self):
        Conexion.Cone = DataBase()
        #Crear Puntero
        Conexion.Cone.cursor.execute("SELECT * FROM  Posiciones ORDER BY Pts ASC")
        #Variable para guardar lo extraido de la base con el select
        valorescapturados=Conexion.Cone.cursor.fetchall()
        #----------------------------Ciclo for para  que los registros no se muestren repeditos al consultarlos
        posicionestable=self.Tabla.get_children()
        #print(registros)
        for posi in posicionestable:
            self.Tabla.delete(posi)
        #----------------------------ciclo for para mostrar los regirstros en la tabla
        for (Id,club,pj,g,e,p,gf,gc,dg,pts) in valorescapturados:
                #print(i)
                #print("Id: ", i[0], " Nombre: ", i[1], " Apellido: ",i[2], "Edad: ", i[3], "password: ", i[4])
            self.Tabla.insert('',0,  values =[club,pj,g,e,p,gf,gc,dg,pts],text=Id, )#Si le pongo 1 los muestra en orden de menor a mayor 
                #y si le pongo 0 los muestra de mayor a menor
        Conexion.Cone.connec.commit()

