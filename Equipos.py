from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Conexion
from Conexion import *
import VentanaMenu
from VentanaMenu import *

"""-----------Clase de Pantalla Para Create(Ingresar), Delete(Eliminar), Update(Actualizar), Read(Consultar) Equipos-----------"""


class classEquipos(Toplevel):
    def __init__(self):
        # self.VentanaEquipos=Tk()
        # self.VentanaEquipos.attributes('-topmost', True)#establecer el atributo topmost en True dentro de la raíz. Al hacer esto, la ventana se quedará siempre encima de las otras.
        # self.VentanaEquipos.title("Liga de Futbol " )
        # self.VentanaEquipos.geometry("1450x700")
        # self.VentanaEquipos.config(bg="#F0F8FF")
        # self.VentanaEquipos.resizable(0,0)

        """Frame donde esta el entry para que ingre el nombre del equipo y el boton para guardar el equipo"""
        FrameCampos=Frame()
        FrameCampos.grid(row=3, column=5, sticky='nsew')
        FrameCampos.config(bg="#A11FFF")#color del frame
        FrameCampos.config(width="830", height="170")#Tamaño del fram, para que este surja efecto el de la self.VentanaEquipos debe estar desactivado
        FrameCampos.grid_propagate(0)
        #FrameCampos.config(bd=2)#tamaño al borde del frame
        FrameCampos.config(relief="raised")#tipo de marco para el frame

        """Frame donde se encuentra la tabla donde se mostraran los datos de al DB"""
        Frametabla=Frame()
        Frametabla.grid(row=4, column=5, sticky='nsew')
        Frametabla.config(bg="#A11FFF")#color del frame
        Frametabla.config(width="830", height="350")#Tamaño del fram, para que este surja efecto el de la self.VentanaEquipos debe estar desactivado
        Frametabla.grid_propagate(0)
        #Frametabla.config(bd=2)#tamaño al borde del frame
        Frametabla.config(relief="raised")#tipo de marco para el frame

        self.NameEQ=StringVar()

        """Marco para encerrar o enmarcar la entrada de texto"""
        marco=LabelFrame(FrameCampos, text="CRUD Equipos"   )
        marco.grid(row=13,column=7, columnspan=6, pady=10, padx=20)

        """Entrada de texto para la tabla equipos"""
        NombreEQlabel=Label(marco,text="Nombre de EQ ")
        NombreEQlabel.grid(row=14,column=7,pady=4, padx=6)
        self.txtNombreEQ=Entry(marco, textvariable=self.NameEQ)
        self.txtNombreEQ.grid(row=14,column=8,padx=8, pady=8)
        self.txtNombreEQ.focus()

        """Label que indica que debe hacer el usuario"""
        Mensanje=Label(marco, text="Ingrese el nombre del equipo ")
        Mensanje.grid(row=13,column=7,pady=4, padx=2)

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
        stilos.map("Treeview", background=[('selected', 'green')]
        )

        """Boton para guardar los Equipos"""
        ingresarUsuarios=Button(FrameCampos, text="Insertar", command=self.IngresarEQ )
        ingresarUsuarios.grid(row=15, column=7 , sticky="nes", pady=12, padx=20)
        ingresarUsuarios.config(bg="#008B8B", fg="#191970", font=("Courier", 12, "italic"))

        """Boton de funcion Editar Equipo """
        ButonEditar=Button(FrameCampos, text=" Actualizar ", command=self.EditarEquipo)
        ButonEditar.config(bg="#008B8B", fg="#191970", font=("Courier", 12, "italic"))
        ButonEditar.grid(row=15, column=8, padx=6,pady=6)

        """Creando tablas para mostrar datos de la tabla Equipos"""
        self.Tabla=ttk.Treeview(Frametabla, columns=1 )
        #self.Tabla.config(width="1700", height="700")
        self.Tabla.grid(row=16, column=7,columnspan=12, padx=10,pady=2, sticky="nsew")
        self.Tabla.bind("<Double-Button-1>", self.FuncDobleclickTabla)#El -1 es para el boton izquierdo del raton y el -2 es para el boton derecho del raton y el -3 para el boton de enmedio
        self.Tabla.heading("#0", text="Equipos", anchor=CENTER)
        self.Tabla.column("#0", width=400, anchor=E )
        self.Tabla.heading("#1", text="ID", anchor=CENTER)
        self.Tabla.column("#1", width=400, anchor=CENTER)

        """Boton de Funcion Listar Campos de la tabla Equipos"""
        botonlistar=Button(Frametabla, text="Mostrar Equipos", command=self.ListarEquipos )#crea un boton con texto dentro y se le pasa la funcion boton1
        botonlistar.config(bg="#008B8B", fg="#191970", font=("Courier", 12, "italic"))
        botonlistar.grid(row=17, column=7,pady=4,sticky="nes")

        """Boton de Funcion Borrar campos de la tabla equipos"""
        Butonborrar=Button(Frametabla, text="Borrar", command=self.Eliminar)
        Butonborrar.config(bg="#008B8B", fg="#191970", font=("Courier", 12, "italic"))
        Butonborrar.grid(row=17, column=8,pady=4, )


#----------Funcion para ingresar Equipos -----------------------
    def IngresarEQ(self):
        #cursor.execute("INSERT INTO Equipos VALUES (NULL,?,?)", lista)
        Conexion.Cone = DataBase()
        lista=[self.txtNombreEQ.get()]
        """ConexionDB.Cone.cursor.execute("INSERT INTO Equipos VALUES (NULL,'" + NameEQ.get()+
        "','" + Capitan.get() +"')")"""
        #Conexion.Cone.cursor.execute("INSERT INTO Equipos VALUES (NULL,'" + NameEQ.get()+"')")
        if len(self.txtNombreEQ.get())!=0:
            Conexion.Cone.cursor.execute("INSERT INTO Equipos VALUES (NULL,%s)", lista)
            Conexion.Cone.connec.commit()
            messagebox.showinfo("INFO", "Equipo ingresado Exitosamente")
            self.ListarEquipos()
        else:
            messagebox.showinfo("Campos Vacios", "Los campos no puede quedar vacios")
            #self.NameEQ.set("")    ##Metodo .set para limpiar los entry
            self.txtNombreEQ.delete(0,END)
            self.txtNombreEQ.focus()
            self.ListarEquipos()

    def ListarEquipos(self):
        #Abrir y crear Conexion a la base de sql lite
        Conexion.Cone = DataBase()
        #Crear Puntero
        Conexion.Cone.cursor.execute("SELECT * FROM  Equipos")
        #Variable para guardar lo extraido de la base con el select
        valoresextraidos=Conexion.Cone.cursor.fetchall()
        #width = 5
        #----------------------------Ciclo for para  que los registros no se muestren repeditos al consultarlos
        registros=self.Tabla.get_children()
        #print(registros)
        for registro in registros:
            self.Tabla.delete(registro)
        #----------------------------ciclo for para mostrar los regirstros en la tabla
        for (Id,Nombre) in valoresextraidos:
                #print(i)
                #print("Id: ", i[0], " Nombre: ", i[1], " Apellido: ",i[2], "Edad: ", i[3], "password: ", i[4])
            self.Tabla.insert('',0, text=Nombre, values = Id )#Si le pongo 1 los muestra en orden de menor a mayor 
                #y si le pongo 0 los muestra de mayor a menor
        Conexion.Cone.connec.commit()

#-------------------Funcion para Editar y actualizar los campos de la tabla Equipos------------------------------------
    def EditarEquipo(self):
        #Abrir y crear Conexion a la base de sql lite
        Conexion.Cone = DataBase()
        Conexion.Cone.cursor.execute("UPDATE Equipos SET Nombre_EQ='" + self.txtNombreEQ.get()+"' WHERE Id_Equipo='" + 
        self.id_Equipos +"'")
        #messagebox.showinfo("BBDD", "Equipo Actualizado")
        self.txtNombreEQ.delete(0,END)
        #self.limpiarCampos()
        #limpiarCampos()
        self.txtNombreEQ.focus()
        Conexion.Cone.connec.commit()
        self.ListarEquipos()

#----------------------Limpiar los campos-----------------
    def limpiarCampos(self):
                    self.NameEQ.set("")

#-----------------Funcion para la Actualizacion de la tabla--------------------------------
    def FuncDobleclickTabla(self,event):
        self.id_Equipos = str(self.Tabla.item(self.Tabla.selection())["values"][0])#Toma el ID de la tabla como indice cero
        #print(text)
        self.txtNombreEQ.delete(0,END)
        #self.limpiarCampos()
        #ingresarUsuarios["state"]="disable"#Deshabilitar el boton ingresar users
        #ButonEditar["state"]="normal"#Poner estado normal activo al boton editar cuando se selecciono un registro y aparesca en los entry
        self.txtNombreEQ.insert(0,str(self.Tabla.item(self.Tabla.selection())["text"]))#Inserta el registro actualizado en la tabla
        #print(type( dato))      
        #Insertar los registros con values para que se
        # muestre ponga cada valor donde corresponda en los entry 

    def Eliminar(self):
        #Abrir y crear Conexion a la base 
        Conexion.Cone = DataBase()
        Conexion.Cone.cursor.execute("DELETE FROM Equipos WHERE Nombre_EQ='" + self.txtNombreEQ.get() +"'")
        Conexion.Cone.connec.commit()
        self.txtNombreEQ.delete(0,END)
        #self.limpiarCampos()
        #messagebox.showinfo("INFO", "Equipo Eliminado")
        self.txtNombreEQ.focus()
        self.ListarEquipos()
        #self.VentanaEquipos.mainloop()

    # def pantalla_datos(self):
    #           self.paginas.select([self.frame_dos])
    #           self.frame_dos.columnconfigure(0, weight=1)
    #           self.frame_dos.columnconfigure(1, weight=1)
    #           self.frame_dos.rowconfigure(2, weight=1)
    #           self.frame_tabla_uno.columnconfigure(0, weight=1)
    #           self.frame_tabla_uno.rowconfigure(0, weight=1)












#claseposiciones=posiciones()
#claseEquipos=classEquipos()







#mensaje=Label(FrameCampos)#Label para mostrar lo que el usuario ha seleccionado
#mensaje.grid(row=5,column=0)

# ###Crear listas desplegables 
# Lista_desplegable=ttk.Combobox(FrameCampos, width=17)
# Lista_desplegable.grid(row=6, column=0)
# opciones=["Opcion 1", "Opcion 2", "Opcion 3"]
# Lista_desplegable['values']=opciones